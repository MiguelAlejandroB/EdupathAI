import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
import xgboost as xgb
import shap

class PredictiveAgent:
    """
    Agente Predictivo (ML Core).
    Responsabilidad Única (SRP): Solo entrena, predice y explica. No interactúa con la UI.
    Principio Abierto/Cerrado (OCP): Soporta CatBoost y XGBoost dinámicamente.
    """
    
    def __init__(self, model_type='catboost'):
        """
        Inicializa el agente.
        :param model_type: 'catboost' o 'xgboost'
        """
        self.model_type = model_type.lower()
        self.model = None
        self.explainer = None
        
        # Definimos las características esperadas para asegurar consistencia
        self.features = [
            'Asistencia_Q1', 'Calificacion_Q1', 'Intervencion_Q1',
            'Asistencia_Q2', 'Calificacion_Q2', 'Intervencion_Q2',
            'Asistencia_Q3', 'Calificacion_Q3', 'Intervencion_Q3',
            'Asistencia_Q4', 'Calificacion_Q4', 'Intervencion_Q4',
            'Nivel_Socioeconomico_Alto', 'Nivel_Socioeconomico_Bajo', 'Nivel_Socioeconomico_Medio'
        ]

    def _preprocess(self, df: pd.DataFrame) -> tuple:
        """
        Método privado para normalizar datos antes de entrenar/predecir.
        Convierte variables categóricas para que XGBoost y CatBoost funcionen igual.
        """
        df_proc = df.copy()
        
        # One-Hot Encoding para el nivel socioeconómico si existe la columna
        if 'Nivel_Socioeconomico' in df_proc.columns:
            df_proc = pd.get_dummies(df_proc, columns=['Nivel_Socioeconomico'])
            
        # Asegurarnos de que todas las columnas existan (rellenamos con 0 si faltan)
        for col in self.features:
            if col not in df_proc.columns:
                df_proc[col] = 0
                
        # Aseguramos el orden estricto de las columnas
        X = df_proc[self.features].astype(float)
        
        y = df_proc['Desercion_Target'] if 'Desercion_Target' in df_proc.columns else None
        return X, y

    def train(self, df: pd.DataFrame):
        """
        Entrena el modelo seleccionado usando el dataset de DataAgent.
        """
        X, y = self._preprocess(df)
        
        if self.model_type == 'catboost':
            # CatBoost es excelente sin tunear mucho y muy rápido
            self.model = CatBoostClassifier(iterations=150, learning_rate=0.1, depth=5, silent=True)
            self.model.fit(X, y)
            
        elif self.model_type == 'xgboost':
            # XGBoost como alternativa robusta agregada
            self.model = xgb.XGBClassifier(n_estimators=150, learning_rate=0.1, max_depth=5, use_label_encoder=False, eval_metric='logloss')
            self.model.fit(X, y)
        else:
            raise ValueError("Modelo no soportado. Usa 'catboost' o 'xgboost'.")

        # Configurar SHAP para la explicabilidad (Explainable AI - XAI)
        self.explainer = shap.TreeExplainer(self.model)

    def predict_trajectory(self, student_df: pd.DataFrame) -> dict:
        """
        Calcula el riesgo acumulado en Q1, Q2, Q3 y Q4.
        Lógica MVP: En Q1, asumimos que Q2, Q3 y Q4 tendrán el mismo comportamiento que Q1.
        """
        if self.model is None:
            raise Exception("El modelo no ha sido entrenado aún.")
            
        X, _ = self._preprocess(student_df)
        
        # Tomamos solo la primera fila (estamos analizando un estudiante)
        x_base = X.iloc[[0]].copy()
        trajectory = {}

        # Simulación Q1 (Ocultamos Q2, Q3, Q4 copiando los datos de Q1 hacia el futuro)
        x_q1 = x_base.copy()
        for q in [2, 3, 4]:
            x_q1[f'Asistencia_Q{q}'] = x_q1['Asistencia_Q1']
            x_q1[f'Calificacion_Q{q}'] = x_q1['Calificacion_Q1']
        trajectory['Q1'] = round(self.model.predict_proba(x_q1)[0][1] * 100, 2)

        # Simulación Q2 (Conocemos Q1 y Q2. Ocultamos Q3 y Q4 copiando Q2)
        x_q2 = x_base.copy()
        for q in [3, 4]:
            x_q2[f'Asistencia_Q{q}'] = x_q2['Asistencia_Q2']
            x_q2[f'Calificacion_Q{q}'] = x_q2['Calificacion_Q2']
        trajectory['Q2'] = round(self.model.predict_proba(x_q2)[0][1] * 100, 2)

        # Simulación Q3 (Conocemos hasta Q3. Ocultamos Q4)
        x_q3 = x_base.copy()
        x_q3['Asistencia_Q4'] = x_q3['Asistencia_Q3']
        x_q3['Calificacion_Q4'] = x_q3['Calificacion_Q3']
        trajectory['Q3'] = round(self.model.predict_proba(x_q3)[0][1] * 100, 2)

        # Simulación Q4 (Conocemos la historia completa)
        trajectory['Q4'] = round(self.model.predict_proba(x_base)[0][1] * 100, 2)

        return trajectory

    def explain_prediction(self, student_df: pd.DataFrame) -> dict:
        """
        Usa SHAP para explicar cuáles fueron las variables que más impactaron
        en la decisión del modelo para este estudiante específico.
        """
        X, _ = self._preprocess(student_df)
        x_student = X.iloc[[0]]
        
        # Calcular los valores SHAP
        shap_values = self.explainer.shap_values(x_student)
        
        # SHAP en clasificación binaria a veces devuelve una lista, otras un array directo
        if isinstance(shap_values, list):
            sv = shap_values[1][0] # Impacto hacia la clase positiva (Deserción)
        else:
            sv = shap_values[0]
            
        # Crear un diccionario ordenado de mayor a menor impacto absoluto
        feature_impacts = {feat: val for feat, val in zip(self.features, sv)}
        # Ordenar por valor absoluto para ver qué importa más
        sorted_impacts = dict(sorted(feature_impacts.items(), key=lambda item: abs(item[1]), reverse=True))
        
        # Devolvemos el top 5 para no saturar la UI
        return dict(list(sorted_impacts.items())[:5])

# --- Código de prueba rápida ---
if __name__ == "__main__":
    import data_agent
    
    # 1. Traer datos
    agent_datos = data_agent.DataAgent()
    df_sintetico = agent_datos.generate_synthetic_data(100)
    
    # 2. Inicializar ML con XGBoost (¡Como lo solicitaste!)
    ml_agent = PredictiveAgent(model_type='xgboost')
    ml_agent.train(df_sintetico)
    
    # 3. Probar con un estudiante específico (el primero)
    estudiante = df_sintetico.iloc[[0]]
    print(f"Estudiante ID: {estudiante['ID'].values[0]}")
    
    # 4. Ver su trayectoria
    trayectoria = ml_agent.predict_trajectory(estudiante)
    print("Trayectoria de Riesgo (%):", trayectoria)
    
    # 5. Ver por qué tiene ese riesgo
    explicacion = ml_agent.explain_prediction(estudiante)
    print("Top 5 Variables de Impacto (SHAP):", explicacion)