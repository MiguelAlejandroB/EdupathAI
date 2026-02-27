import pandas as pd

class ChatHandler:
    """
    Controlador del Chat.
    Responsabilidad Única: Interpretar el texto del usuario, orquestar los agentes del Core,
    y devolver una respuesta estructurada (Texto + Datos de Gráfica).
    """
    def __init__(self, data_df, ml_agent, simulator):
        self.df = data_df
        self.ml_agent = ml_agent
        self.simulator = simulator

    def process_message(self, user_message: str) -> dict:
        """
        Procesa el mensaje del usuario y devuelve la respuesta del asistente.
        """
        msg_lower = user_message.lower()
        
        # ---------------------------------------------------------
        # INTENCIÓN 1: Análisis de Riesgo (Ej: "Analiza a Juan")
        # ---------------------------------------------------------
        if "analiza" in msg_lower or "juan" in msg_lower:
            # Simulamos que Juan es nuestro primer estudiante del dataset
            estudiante = self.df.iloc[[0]]
            nombre = estudiante['Nombre'].values[0]
            
            # 1. Calculamos trayectoria
            trayectoria = self.ml_agent.predict_trajectory(estudiante)
            
            # 2. Sacamos explicabilidad con SHAP
            shap_impacts = self.ml_agent.explain_prediction(estudiante)
            
            # 3. Armamos la respuesta en Lenguaje Natural (Mock de LLM)
            riesgo_final = trayectoria['Q4']
            
            # Extraer las 2 razones principales según SHAP
            top_variables = list(shap_impacts.keys())[:2]
            razon_1 = top_variables[0].replace('_', ' ')
            razon_2 = top_variables[1].replace('_', ' ')
            
            respuesta_texto = (
                f"**Análisis completado para {nombre}.**\n\n"
                f"🚨 He detectado un riesgo de deserción proyectado del **{riesgo_final}%** para el final del año (Q4).\n\n"
                f"**¿Por qué está pasando esto? (Análisis SHAP):**\n"
                f"Las variables que más están empujando este riesgo hacia arriba son:\n"
                f"1. **{razon_1}**\n"
                f"2. **{razon_2}**\n\n"
                f"💡 *Sugerencia:* ¿Te gustaría que simule el impacto de aplicar una 'Ruta Escolar' o 'Beca' desde el Q2?"
            )
            
            return {
                "text": respuesta_texto,
                "plot_data": {
                    "base_risk": trayectoria,
                    "simulated_risk": None,
                    "intervention_q": None
                }
            }
            
        # ---------------------------------------------------------
        # INTENCIÓN 2: Simulación Contrafactual (Ej: "Simula ruta escolar")
        # ---------------------------------------------------------
        elif "simula" in msg_lower or "ruta" in msg_lower or "beca" in msg_lower:
            estudiante = self.df.iloc[[0]]
            
            # Detectar qué intervención pidió
            tipo_intervencion = 'Ruta Escolar' if 'ruta' in msg_lower else 'Beca'
            trimestre_inicio = 2 # Simulamos que arranca en Q2
            
            # Ejecutar el simulador
            resultados = self.simulator.simulate_intervention(estudiante, tipo_intervencion, trimestre_inicio)
            
            riesgo_original = resultados['baseline']['Q4']
            riesgo_nuevo = resultados['simulated']['Q4']
            reduccion = round(riesgo_original - riesgo_nuevo, 1)
            
            respuesta_texto = (
                f"✅ **Simulación Exitosa: {tipo_intervencion} aplicada en Q{trimestre_inicio}.**\n\n"
                f"El escenario contrafactual muestra resultados muy positivos. "
                f"El riesgo de deserción de final de año caería drásticamente del **{riesgo_original}%** al **{riesgo_nuevo}%** "
                f"(Una reducción de {reduccion} puntos porcentuales).\n\n"
                f"Mira el impacto visual en el área sombreada verde de la gráfica."
            )
            
            return {
                "text": respuesta_texto,
                "plot_data": {
                    "base_risk": resultados['baseline'],
                    "simulated_risk": resultados['simulated'],
                    "intervention_q": f'Q{trimestre_inicio}'
                }
            }
            
        # ---------------------------------------------------------
        # FALLBACK: Saludo general
        # ---------------------------------------------------------
        else:
            return {
                "text": "¡Hola! Soy edUPath IM. Puedes pedirme que analice el riesgo de un estudiante (ej. 'Analiza a Juan Pérez') o que simule intervenciones.",
                "plot_data": None
            }