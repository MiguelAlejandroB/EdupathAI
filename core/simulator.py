import pandas as pd
import copy

class InterventionSimulator:
    """
    Agente de Intervención (Simulator Core).
    Responsabilidad Única (SRP): Generar escenarios contrafactuales ("What-If").
    Toma el modelo ML entrenado y altera los datos de entrada para ver cómo cambia el futuro.
    """

    def __init__(self, predictive_agent):
        """
        Inyectamos la dependencia del agente predictivo para poder recalcular.
        :param predictive_agent: Instancia de PredictiveAgent ya entrenada.
        """
        if predictive_agent.model is None:
            raise ValueError("El PredictiveAgent debe estar entrenado antes de simular.")
        self.ml_agent = predictive_agent

    def simulate_intervention(self, student_df: pd.DataFrame, intervention_type: str, quarter_applied: int) -> dict:
        """
        Aplica una intervención en un trimestre específico y proyecta el nuevo riesgo.
        
        :param student_df: DataFrame con los datos de un estudiante.
        :param intervention_type: 'Beca', 'Tutoría', 'Ruta Escolar'.
        :param quarter_applied: Trimestre en el que inicia la ayuda (1, 2, 3 o 4).
        :return: Diccionario con la trayectoria original y la simulada.
        """
        # 1. Calcular la línea base (Lo que pasaría si no hacemos nada)
        base_trajectory = self.ml_agent.predict_trajectory(student_df)

        # 2. Crear el escenario contrafactual (Copia de los datos)
        simulated_df = student_df.copy()

        # 3. Reglas Heurísticas Causales (MVP)
        # TODO (Post-MVP): Reemplazar esta heurística con Microsoft DoWhy para inferencia causal estricta.
        
        # Iteramos sobre los trimestres a partir de cuando se aplicó la intervención
        for q in range(quarter_applied, 5):
            # Dejamos un registro de que la intervención estuvo activa
            if f'Intervencion_Q{q}' in simulated_df.columns:
                simulated_df[f'Intervencion_Q{q}'] = 1

            # Efecto Causal 1: Ruta Escolar mejora drásticamente la asistencia.
            if intervention_type == 'Ruta Escolar':
                current_att = simulated_df[f'Asistencia_Q{q}'].values[0]
                # Sube la asistencia un 25%, con tope en 100%
                simulated_df[f'Asistencia_Q{q}'] = min(100.0, current_att * 1.25)

            # Efecto Causal 2: Tutoría mejora las calificaciones gradualmente.
            elif intervention_type == 'Tutoría':
                current_grade = simulated_df[f'Calificacion_Q{q}'].values[0]
                # Sube la nota un 20%, con tope en 5.0
                simulated_df[f'Calificacion_Q{q}'] = min(5.0, current_grade * 1.20)

            # Efecto Causal 3: Beca quita presión económica (Impacta ambas variables levemente)
            elif intervention_type == 'Beca':
                current_att = simulated_df[f'Asistencia_Q{q}'].values[0]
                current_grade = simulated_df[f'Calificacion_Q{q}'].values[0]
                simulated_df[f'Asistencia_Q{q}'] = min(100.0, current_att * 1.10)
                simulated_df[f'Calificacion_Q{q}'] = min(5.0, current_grade * 1.10)
                
                # Si el estudiante es de nivel bajo, el impacto de la beca es el doble
                if 'Nivel_Socioeconomico' in simulated_df.columns and simulated_df['Nivel_Socioeconomico'].values[0] == 'Bajo':
                     simulated_df[f'Asistencia_Q{q}'] = min(100.0, current_att * 1.20)

        # 4. Recalcular el futuro con los datos alterados usando el mismo modelo ML
        simulated_trajectory = self.ml_agent.predict_trajectory(simulated_df)

        return {
            "baseline": base_trajectory,
            "simulated": simulated_trajectory
        }

# --- Código de prueba rápida ---
if __name__ == "__main__":
    from data_agent import DataAgent
    from ml_predictive import PredictiveAgent
    
    # 1. Preparar datos y modelo
    agent_datos = DataAgent()
    df_sintetico = agent_datos.generate_synthetic_data(100)
    
    ml_agent = PredictiveAgent(model_type='catboost')
    ml_agent.train(df_sintetico)
    
    # 2. Inicializar el Simulador
    simulator = InterventionSimulator(ml_agent)
    
    # 3. Buscar un estudiante en riesgo (ej. el primero)
    estudiante_en_riesgo = df_sintetico.iloc[[0]]
    print(f"Estudiante ID: {estudiante_en_riesgo['ID'].values[0]}")
    print(f"Asistencia original Q3: {estudiante_en_riesgo['Asistencia_Q3'].values[0]}")
    
    # 4. Simular darle una "Ruta Escolar" a partir del Trimestre 2
    resultados = simulator.simulate_intervention(
        student_df=estudiante_en_riesgo, 
        intervention_type='Ruta Escolar', 
        quarter_applied=2
    )
    
    print("\nResultados de la Simulación ('What-If'):")
    print("Riesgo Original (Sin ayuda):", resultados['baseline'])
    print("Riesgo Simulado (Con Ruta Escolar desde Q2):", resultados['simulated'])