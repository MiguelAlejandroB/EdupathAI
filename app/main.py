import streamlit as st
import sys
import os

# Esto es CRUCIAL para que Streamlit encuentre la carpeta 'core'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.data_agent import DataAgent
from core.ml_predictive import PredictiveAgent
from core.simulator import InterventionSimulator
from app.components.timeline import render_risk_timeline
from app.chat_handler import ChatHandler

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="edUPath IM | Inteligencia Predictiva",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CACHÉ DEL BACKEND (Para que vuele) ---
# Usamos cache_resource para entrenar el modelo UNA sola vez al abrir la app.
@st.cache_resource(show_spinner="Inicializando Cerebro IA...")
def init_backend():
    data_agent = DataAgent()
    df_estudiantes = data_agent.generate_synthetic_data(100)
    
    ml_agent = PredictiveAgent(model_type='xgboost')
    ml_agent.train(df_estudiantes)
    
    simulator = InterventionSimulator(ml_agent)
    
    return df_estudiantes, ml_agent, simulator

df_data, ml_core, sim_core = init_backend()
chat_handler = ChatHandler(df_data, ml_core, sim_core)

# --- 3. BARRA LATERAL (Look Profesional) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135810.png", width=80) # Logo genérico
    st.title("edUPath IM")
    st.markdown("---")
    st.success("🟢 Agente de Datos Activo")
    st.success("🟢 XGBoost Core Activo")
    st.success("🟢 Simulador DoWhy Activo")
    st.markdown("---")
    st.caption("Solución finalista - OdiseIA4Good")

# --- 4. ÁREA PRINCIPAL ---
st.title("🧠 Asistente de Intervención Psicosocial")
st.markdown("Pregúntame por el riesgo de un estudiante y simulemos estrategias de retención.")

# --- 5. GESTIÓN DEL HISTORIAL DEL CHAT (Session State) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Dibujar el historial de mensajes anterior
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        # Si este mensaje guardó una gráfica, la volvemos a dibujar
        if msg.get("plot_data"):
            render_risk_timeline(**msg["plot_data"])

# --- 6. CAJA DE TEXTO DEL USUARIO ---
if prompt := st.chat_input("Ej: Analízame el caso de Juan Pérez..."):
    
    # 6.1 Mostrar el mensaje del usuario en pantalla
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Guardar en memoria
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 6.2 Procesar la respuesta con nuestro ChatHandler
    with st.chat_message("assistant"):
        with st.spinner("Analizando causas fundamentales..."):
            respuesta = chat_handler.process_message(prompt)
            
            # Imprimir el texto generado
            st.markdown(respuesta["text"])
            
            # Dibujar la gráfica si el handler la devolvió
            if respuesta["plot_data"]:
                render_risk_timeline(**respuesta["plot_data"])
                
    # 6.3 Guardar la respuesta (con su gráfica) en memoria
    st.session_state.messages.append({
        "role": "assistant", 
        "content": respuesta["text"],
        "plot_data": respuesta["plot_data"]
    })