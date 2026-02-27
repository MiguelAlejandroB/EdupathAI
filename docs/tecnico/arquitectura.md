# 🏗️ Arquitectura Técnica

> *edUPath IM está diseñado bajo una arquitectura modular, orientada a microservicios y lista para producción (Production-Ready) en entornos ligeros.*

Para cumplir con nuestro objetivo de procesar datos, predecir con modelos de Machine Learning y orquestar respuestas con Inteligencia Artificial, hemos dividido la plataforma en capas claramente definidas.

---

## 🧩 Diagrama de Arquitectura del Sistema

El siguiente diagrama muestra cómo interactúa la interfaz de usuario con nuestro ecosistema de IA y bases de datos.

```mermaid
graph TD
    subgraph Frontend [Capa de Presentación]
        UI[Streamlit UI]
        Chat[Chatbot Interface]
        Graphs[Plotly Timelines]
    end

    subgraph Backend [Capa de Lógica y Orquestación]
        API[FastAPI Wrapper]
        LC[LangChain Orchestrator]
    end

    subgraph Agentes IA [Ecosistema Multi-Agente]
        Agent1[Data Agent]
        Agent2[ML Predictor]
        Agent3[Causal Simulator]
    end

    subgraph Modelos Core [Capa de Machine Learning]
        CatB[(CatBoost)]
        SHAP[(SHAP Explainer)]
        DoW[(DoWhy / EconML)]
    end

    subgraph Datos [Capa de Persistencia]
        DB[(PostgreSQL / MongoDB)]
    end

    %% Conexiones
    UI -->|HTTP Requests| API
    Chat -->|Prompts| LC
    API <--> LC
    LC <--> Agent1
    LC <--> Agent2
    LC <--> Agent3
    
    Agent1 <--> DB
    Agent2 <--> CatB
    Agent2 <--> SHAP
    Agent3 <--> DoW

🛠️ Stack Tecnológico Elegido
Cada tecnología en nuestro stack fue seleccionada cuidadosamente para optimizar la velocidad de iteración y la robustez del modelo.

1. Frontend (Interfaz de Usuario)
Framework: Streamlit.

Justificación: Permite una iteración rápida y soporte nativo para el desarrollo de dashboards analíticos y componentes de chat (st.chat_input). Ideal para nuestro MVP en OdiseIA.

Visualización: Plotly y Altair para la renderización de las líneas de tiempo interactivas (Curvas de Riesgo) sin perder rendimiento.

2. Backend & Orquestación
API y Microservicios: FastAPI.

Justificación: Exponemos nuestros modelos predictivos como APIs asíncronas de alto rendimiento.

Orquestación de IA: LangChain.

Justificación: Maneja la lógica conversacional, el historial del chat y el enrutamiento hacia nuestras "herramientas" (el modelo de predicción o el simulador causal).

3. Modelos Machine Learning (Core)
Predicción de Riesgo: CatBoost. Elegido por su altísimo rendimiento nativo con datos tabulares y variables categóricas (comunes en bases de datos educativas).

Explicabilidad: SHAP (SHapley Additive exPlanations) para "abrir la caja negra" e indicar por qué un estudiante está en riesgo.

Inferencia Causal: DoWhy (Microsoft) para el motor de simulación contrafactual ("What-If").

4. Infraestructura y Despliegue
Base de Datos: PostgreSQL (vía Supabase) o MongoDB Atlas.

Contenedores: Docker para asegurar que la aplicación funcione idénticamente en el entorno local y en el servidor.

Hosting / Despliegue: Render, AWS (EC2/Lambda) o Streamlit Community Cloud (para el MVP).

📂 Estructura del Proyecto (Repositorio)
Para mantener un código limpio y escalable, el proyecto sigue esta estructura estándar de ingeniería de software:

Plaintext
edUPath_MVP/
│
├── app/                        # 🖥️ Código del Frontend y Backend API
│   ├── main.py                 # Punto de entrada de Streamlit
│   ├── api.py                  # Endpoints de FastAPI
│   └── components/             # Componentes UI (gráficos, chat)
│
├── agents/                     # 🤖 Lógica de LangChain y Agentes
│   ├── orchestrator.py         # Manejador principal de prompts
│   ├── data_agent.py           # Conexión con DB y limpieza
│   ├── ml_agent.py             # Llamadas a CatBoost y SHAP
│   └── causal_agent.py         # Llamadas a DoWhy
│
├── models/                     # 🧠 Modelos ML y entrenamiento
│   ├── train.py                # Script de entrenamiento
│   ├── weights/                # Archivos .cbm o .pkl guardados
│   └── data/                   # Datasets (piloto/sintético)
│
├── docs/                       # 📚 Documentación MkDocs (Tú estás aquí)
│
├── Dockerfile                  # 🐳 Configuración de contenedor
├── requirements.txt            # 📦 Dependencias de Python
└── mkdocs.yml                  # ⚙️ Configuración de la documentación
!!! tip "Escalabilidad Futura"
Aunque para la demostración en OdiseIA el código puede correr monolíticamente en Streamlit, esta separación en carpetas (app/, agents/, models/) garantiza que si el proyecto recibe inversión y necesita escalar, FastAPI y Streamlit pueden separarse en contenedores Docker distintos inmediatamente.