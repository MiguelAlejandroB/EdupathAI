import plotly.graph_objects as go
import streamlit as st

def render_risk_timeline(base_risk: dict, simulated_risk: dict = None, intervention_q: str = None):
    """
    Dibuja una línea de tiempo profesional e interactiva con Plotly.
    
    :param base_risk: Diccionario con el riesgo original (ej. {'Q1': 20, 'Q2': 45, ...})
    :param simulated_risk: Diccionario con el riesgo simulado (opcional).
    :param intervention_q: String indicando dónde empezó la ayuda (ej. 'Q2').
    """
    
    # Extraemos los ejes X (Trimestres) y Y (Valores)
    quarters = list(base_risk.keys())
    base_values = list(base_risk.values())
    
    # Inicializamos la figura de Plotly
    fig = go.Figure()

    # 1. Trazar la Línea Base (Roja y Continua)
    fig.add_trace(go.Scatter(
        x=quarters, 
        y=base_values,
        mode='lines+markers',
        name='Riesgo Original',
        line=dict(color='#E63946', width=4), # Rojo elegante
        marker=dict(size=10, symbol='circle', line=dict(color='white', width=2)),
        hovertemplate="<b>%{x}</b><br>Riesgo: %{y}%<extra></extra>"
    ))

    # 2. Trazar la Línea Simulada (Verde, Punteada y con sombreado)
    if simulated_risk:
        sim_values = list(simulated_risk.values())
        
        fig.add_trace(go.Scatter(
            x=quarters, 
            y=sim_values,
            mode='lines+markers',
            name='Riesgo con Intervención',
            line=dict(color='#2A9D8F', width=4, dash='dash'), # Verde esmeralda, punteada
            marker=dict(size=10, symbol='diamond', line=dict(color='white', width=2)),
            fill='tonexty', # Sombrea el espacio entre la línea roja y la verde
            fillcolor='rgba(42, 157, 143, 0.2)', # Verde transparente
            hovertemplate="<b>%{x}</b><br>Riesgo Reducido: %{y}%<extra></extra>"
        ))

    # 3. Marcar el momento exacto de la intervención
    if intervention_q and intervention_q in quarters:
        fig.add_vline(
            x=intervention_q, 
            line_width=2, 
            line_dash="dot", 
            line_color="#E9C46A", # Amarillo mostaza
            annotation_text="Punto de Intervención", 
            annotation_position="top right"
        )

    # 4. Diseño del Layout (Dashboard Profesional)
    fig.update_layout(
        title={
            'text': "<b>Proyección Temporal de Riesgo de Deserción</b>",
            'y':0.9, 'x':0.5,
            'xanchor': 'center', 'yanchor': 'top'
        },
        xaxis_title="Trimestres del Año Lectivo",
        yaxis_title="Probabilidad de Deserción (%)",
        yaxis=dict(range=[-5, 105], ticksuffix="%"), # Eje Y fijo de 0 a 100
        template="plotly_white", # Fondo limpio y profesional
        hovermode="x unified", # Al pasar el mouse, compara ambos valores en el mismo globo
        legend=dict(
            orientation="h", # Leyenda horizontal abajo para ahorrar espacio
            yanchor="bottom", y=-0.3,
            xanchor="center", x=0.5
        ),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # 5. Renderizar nativamente en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# --- Código de prueba rápida (Solo si corres este archivo solo) ---
if __name__ == "__main__":
    st.set_page_config(page_title="Test Gráfica", layout="wide")
    st.title("Prueba de UI: Línea de Tiempo")
    
    # Datos falsos para probar cómo se ve
    riesgo_original = {'Q1': 15.5, 'Q2': 45.2, 'Q3': 70.8, 'Q4': 88.3}
    riesgo_salvado = {'Q1': 15.5, 'Q2': 45.2, 'Q3': 30.1, 'Q4': 18.5}
    
    render_risk_timeline(
        base_risk=riesgo_original, 
        simulated_risk=riesgo_salvado, 
        intervention_q='Q2'
    )