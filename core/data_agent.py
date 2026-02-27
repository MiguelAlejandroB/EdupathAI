import pandas as pd
import numpy as np

class DataAgent:
    """
    Agente responsable de la recopilación, limpieza y normalización de los datos.
    Sigue el principio de Responsabilidad Única (SRP): Solo maneja datos, no modelos.
    """
    
    def __init__(self):
        # Semilla para que los datos aleatorios sean siempre los mismos 
        # y los resultados sean reproducibles frente al jurado.
        np.random.seed(42)

    # =================================================================
    # 🚀 FASE 1 (MVP actual): GENERACIÓN DE DATOS SINTÉTICOS
    # =================================================================
    def generate_synthetic_data(self, num_students=500) -> pd.DataFrame:
        """
        Genera un dataset sintético con correlación lógica y estacionalidad.
        """
        data = []
        for i in range(1, num_students + 1):
            student_id = f"STU-{i:04d}"
            name = f"Estudiante {i}"
            
            # Variable base: Nivel Socioeconómico afecta el punto de partida
            ses = np.random.choice(['Bajo', 'Medio', 'Alto'], p=[0.5, 0.3, 0.2])
            base_att = {'Bajo': 85, 'Medio': 90, 'Alto': 95}[ses]
            base_grade = {'Bajo': 3.2, 'Medio': 3.8, 'Alto': 4.2}[ses]

            # --- TRIMESTRE 1 (Q1) ---
            att_q1 = min(100, max(0, np.random.normal(base_att, 5)))
            grade_q1 = min(5.0, max(0.0, np.random.normal(base_grade, 0.5)))
            int_q1 = 0 # 0 = Sin intervención

            # --- TRIMESTRE 2 (Q2) ---
            # Correlación: Si la asistencia en Q1 fue mala (< 80%), las notas de Q2 bajan.
            grade_penalty_q2 = 0.5 if att_q1 < 80 else 0
            grade_q2 = min(5.0, max(0.0, np.random.normal(base_grade - grade_penalty_q2, 0.5)))
            att_q2 = min(100, max(0, np.random.normal(att_q1, 5))) 
            int_q2 = 0

            # --- TRIMESTRE 3 (Q3) ---
            # Correlación: Si las notas en Q2 son malas (< 3.0), baja la motivación y cae la asistencia.
            att_penalty_q3 = 15 if grade_q2 < 3.0 else 0
            att_q3 = min(100, max(0, np.random.normal(att_q2 - att_penalty_q3, 5)))
            grade_q3 = min(5.0, max(0.0, np.random.normal(grade_q2, 0.6)))
            int_q3 = 0

            # --- TRIMESTRE 4 (Q4) ---
            att_penalty_q4 = 20 if att_q3 < 75 else 0
            att_q4 = min(100, max(0, np.random.normal(att_q3 - att_penalty_q4, 5)))
            grade_q4 = min(5.0, max(0.0, np.random.normal(grade_q3, 0.6)))
            int_q4 = 0

            # --- TARGET: DESERCIÓN ---
            # Regla lógica: Alta probabilidad de deserción si la asistencia de cierre es baja 
            # o el promedio anual es deficiente.
            prob_dropout = 0.05
            if att_q4 < 70:
                prob_dropout += 0.6
            if (grade_q1 + grade_q2 + grade_q3 + grade_q4) / 4 < 2.5:
                prob_dropout += 0.3

            prob_dropout = min(1.0, prob_dropout)
            target = np.random.binomial(1, prob_dropout)

            data.append([
                student_id, name, ses,
                round(att_q1, 1), round(grade_q1, 1), int_q1,
                round(att_q2, 1), round(grade_q2, 1), int_q2,
                round(att_q3, 1), round(grade_q3, 1), int_q3,
                round(att_q4, 1), round(grade_q4, 1), int_q4,
                target
            ])

        columns = [
            'ID', 'Nombre', 'Nivel_Socioeconomico',
            'Asistencia_Q1', 'Calificacion_Q1', 'Intervencion_Q1',
            'Asistencia_Q2', 'Calificacion_Q2', 'Intervencion_Q2',
            'Asistencia_Q3', 'Calificacion_Q3', 'Intervencion_Q3',
            'Asistencia_Q4', 'Calificacion_Q4', 'Intervencion_Q4',
            'Desercion_Target'
        ]

        df = pd.DataFrame(data, columns=columns)
        
        # Guardamos un respaldo físico en la carpeta data/
        # df.to_csv('data/estudiantes_sinteticos.csv', index=False)
        return df

    # =================================================================
    # 🏢 FASE 2 (Producción futura): CONEXIÓN A DATOS REALES
    # =================================================================
    
    def fetch_real_data(self, db_connection_string: str) -> pd.DataFrame:
        """
        TODO (Fase Post-MVP): Reemplazará a 'generate_synthetic_data'.
        Aquí nos conectaremos a la base de datos de la escuela (SQL, MongoDB, API).
        
        Ejemplo de implementación futura:
        import sqlalchemy
        engine = sqlalchemy.create_engine(db_connection_string)
        query = "SELECT * FROM sistema_academico.estudiantes WHERE año = '2023'"
        return pd.read_sql(query, engine)
        """
        raise NotImplementedError("Conexión a BD real pendiente de credenciales.")

    def normalize_real_data(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        """
        TODO (Fase Post-MVP): Los datos reales siempre vienen sucios.
        Esta función centralizará la limpieza para que el modelo ML no falle.
        
        Tareas a implementar aquí:
        1. Imputación de nulos (ej: raw_df['Asistencia'].fillna(raw_df['Asistencia'].mean()))
        2. Mapeo de variables categóricas a numéricas.
        3. Agrupación temporal (Convertir registros diarios en trimestrales Q1, Q2, Q3, Q4).
        """
        raise NotImplementedError("Reglas de normalización pendientes de estructura de datos reales.")

# --- Código de prueba rápida (Solo se ejecuta si corres este archivo directamente) ---
if __name__ == "__main__":
    agent = DataAgent()
    dataset = agent.generate_synthetic_data(10) # Probamos con 10
    print("Muestra del Dataset Sintético Generado:")
    print(dataset[['ID', 'Nivel_Socioeconomico', 'Asistencia_Q4', 'Desercion_Target']].head())