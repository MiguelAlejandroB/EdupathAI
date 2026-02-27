<div align="center">
<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="separator">

<h1>🏛️ edUPath IM</h1>
<h3>Sistema de Inteligencia de Decisión para la Retención Escolar</h3>
<p><b>Manual de Operaciones y Documentación Técnica</b></p>

<p>
<a href="#"><img alt="Versión MVP" src="https://www.google.com/search?q=https://img.shields.io/badge/Versi%25C3%25B3n-1.0.0--MVP-blue.svg%3Fstyle%3Dfor-the-badge"></a>
<a href="https://www.python.org/"><img alt="Python" src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.13%2B-3776AB.svg%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite"></a>
<a href="https://streamlit.io/"><img alt="Streamlit" src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-FF4B4B.svg%3Fstyle%3Dfor-the-badge%26logo%3Dstreamlit%26logoColor%3Dwhite"></a>
<a href="#"><img alt="OdiseIA 4Good" src="https://www.google.com/search?q=https://img.shields.io/badge/OdiseIA-Finalista_4Good-FFD700.svg%3Fstyle%3Dfor-the-badge%26logo%3Dhackerrank%26logoColor%3Dblack"></a>
</p>

<p>
<a href="#-1-resumen-ejecutivo"><b>Resumen</b></a> •
<a href="#-3-arquitectura-tecnológica-e-innovación"><b>Arquitectura</b></a> •
<a href="#-6-guía-rápida-de-despliegue-quick-start"><b>Despliegue</b></a> •
<a href="#%EF%B8%8F-8-privacidad-ética-y-cumplimiento"><b>Privacidad</b></a>
</p>

<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" alt="separator">

"El abandono escolar no es una fatalidad, es un fallo predecible del sistema. edUPath IM transforma el gasto público reactivo en inversión social predictiva."

</div>

📑 Tabla de Contenidos

Resumen Ejecutivo

El Caso de Negocio (Business Case)

Arquitectura Tecnológica e Innovación

Módulo Predictivo y Explicabilidad (SHAP)

Simulador Contrafactual (Causalidad)

Guía Rápida de Despliegue (Quick Start)

Manual de Usuario: Flujo de Operación

Privacidad, Ética y Cumplimiento

Hoja de Ruta (Roadmap Técnico)

🏢 1. Resumen Ejecutivo

edUPath IM (Intelligence Management) es una plataforma SaaS B2G/B2NGO diseñada para revolucionar la forma en que los Estados y las instituciones educativas gestionan la deserción escolar.

A diferencia de los sistemas de Business Intelligence tradicionales que se limitan a mostrar datos históricos de estudiantes que ya han abandonado el sistema, edUPath IM aplica principios de Decision Intelligence. Utilizamos modelos avanzados de Machine Learning combinados con inferencia causal para crear un "gemelo digital" del comportamiento estudiantil, permitiendo a los tomadores de decisiones anticipar el fracaso hasta con 12 meses de antelación y simular la efectividad de sus políticas antes de financiarlas.

📉 2. El Caso de Negocio (Business Case)

El paradigma actual de la administración pública frente a la deserción escolar sufre de un grave sesgo de latencia. Las intervenciones (subsidios, programas de apoyo) se activan cuando la desconexión del estudiante es irreversible.

Coste del Status Quo

Inversión Ciega: Asignación de recursos (ej. "Café para todos") sin validación de impacto individual.

Costo Social: Aumento del paro juvenil y riesgo psicosocial.

Costo Fiscal: Cada estudiante que abandona el sistema educativo representa cientos de miles de euros en futuros gastos penales, subsidios de desempleo y pérdida de recaudación fiscal.

La Solución: Retorno de Prevención (RoP)

| Dimensión | Sistema Tradicional | edUPath IM |
| Enfoque Temporal | Reactivo (Post-mortem) | Preventivo (T-12 meses) |
| Asignación de Capital | Basado en intuición | Basado en simulación contrafactual |
| Nivel de Acción | Cohortes generales | Hiper-segmentado por individuo |
| Transparencia | Cajas negras o reglas simples | Valores SHAP (Auditable y explicable) |

Métrica Clave: Validar una intervención de 500€ hoy a través de edUPath IM evita incurrir en costes reactivos exponenciales mañana.

⚙️ 3. Arquitectura Tecnológica e Innovación

El sistema está diseñado bajo una arquitectura modular de agentes inteligentes. En su fase MVP, opera a través de un monolito eficiente en Python, estructurado en 4 capas lógicas.

┌───────────────────────────────────────────────────────────────────────┐
│                       ARQUITECTURA EDUPATH IM                         │
├─────────────────┬─────────────────────────────────────────────────────┤
│ 1. PRESENTACIÓN │ 💬 UI Conversacional (Streamlit)                    │
│                 │ 📊 Visualización Dinámica (Plotly)                  │
├─────────────────┼─────────────────────────────────────────────────────┤
│ 2. ORQUESTACIÓN │ 🤖 Gestor de Intenciones (NLP Parsing)              │
│                 │ 🔄 Enrutador de Agentes                             │
├─────────────────┼─────────────────────────────────────────────────────┤
│                 │ 📈 Predictive Agent: XGBoost / CatBoost             │
│ 3. INTELIGENCIA │ 🔍 XAI Agent: Análisis SHAP (Explainable AI)        │
│                 │ 🔬 Simulator Agent: Motor Contrafactual             │
├─────────────────┼─────────────────────────────────────────────────────┤
│ 4. DATOS        │ 🗄️ Motor de Datos Sintéticos (Temporal Q1-Q4)       │
└─────────────────┴─────────────────────────────────────────────────────┘



🧠 4. Módulo Predictivo y Explicabilidad (SHAP)

Los docentes y trabajadores sociales no confían en algoritmos que no pueden entender. Por ello, edUPath IM rechaza los modelos de "caja negra" (como las redes neuronales densas) para este dominio, optando por Árboles de Decisión con Gradiente (XGBoost) potenciados por Valores Shapley (SHAP).

¿Cómo funciona la Explicabilidad?

Por cada predicción de riesgo, el sistema genera un desglose exacto de las fuerzas que actúan sobre el estudiante:

🟥 Fuerzas de Riesgo: (Ej. Inasistencias Q3: +25% de riesgo, Caída en matemáticas: +15% de riesgo).

🟩 Fuerzas de Retención: (Ej. Participación en extracurriculares: -10% de riesgo).

Esta explicabilidad es fundamental para el cumplimiento de normativas europeas sobre IA (AI Act) respecto a la toma de decisiones automatizada en sectores críticos.

🔮 5. Simulador Contrafactual (Causalidad)

La correlación no implica causalidad. Que un estudiante asista a tutorías no garantiza que su riesgo baje. El Simulador Contrafactual permite a las instituciones responder a preguntas tipo What-If (¿Qué pasaría si...?).

Catálogo de Intervenciones Modeladas (MVP):

Beca de Transporte: Simula el impacto directo en la reducción de inasistencias geográficas.

Tutoría Académica: Modela la curva de recuperación en calificaciones (GPA).

Apoyo Socioeconómico (Beca Integral): Impacto cruzado con ponderación especial para estudiantes de bajo Nivel Socioeconómico (NSE).

💻 6. Guía Rápida de Despliegue (Quick Start)

Para ingenieros y evaluadores técnicos, el MVP está empaquetado para despliegue local inmediato.

Requisitos del Sistema

SO: Windows, macOS, Linux

Python: >= 3.9

Memoria RAM: Mínimo 4GB (para procesamiento SHAP en memoria)

Pasos de Ejecución

# 1. Clonar el repositorio oficial
git clone [https://github.com/MiguelAlejandroB/EdupathAI.git](https://github.com/MiguelAlejandroB/EdupathAI.git)

# 2. Navegar al directorio raíz
cd EdupathAI

# 3. Instalar las dependencias del entorno
pip install -r requirements.txt

# 4. Iniciar el servidor de la aplicación (Decision Core)
streamlit run app/main.py



El sistema inicializará el pipeline de datos, entrenará el modelo en tiempo real y desplegará la interfaz en http://localhost:8501.

👨‍💻 7. Manual de Usuario: Flujo de Operación

La curva de aprendizaje de edUPath es nula gracias a su interfaz basada en lenguaje natural.

Paso 1: Diagnóstico (Evaluación de Estado)

Operador ingresa: "Analiza el caso del estudiante Juan Pérez"

Sistema ejecuta: 1. Extrae el ID del estudiante.
2. Proyecta su trayectoria histórica (Trimestres 1 a 3).
3. Proyecta el riesgo futuro para el Trimestre 4 (Ej. 87% Riesgo Crítico).
4. Despliega la auditoría SHAP explicando el porqué.

Paso 2: Simulación de Intervención (Inferencia)

Operador ingresa: "Simula aplicarle una beca desde el trimestre 2"

Sistema ejecuta:

Clona el perfil del estudiante (Gemelo Digital).

Inyecta los parámetros de la "Beca" en los datos históricos.

Recalcula el modelo hacia el futuro.

Output Visual: Superpone una curva verde sobre la gráfica original, demostrando la caída del riesgo (Ej. de 87% a 18%).

🛡️ 8. Privacidad, Ética y Cumplimiento

edUPath IM está diseñado bajo el principio de Privacy by Design:

Sin PII (Personally Identifiable Information): El motor predictivo solo procesa IDs hasheados, métricas académicas y conductuales. Nombres y direcciones jamás tocan los modelos de Machine Learning.

LLM Aislado: El procesamiento de lenguaje natural se usa estrictamente para interpretar la intención del usuario (orquestación), no para entrenar modelos con los datos de los menores.

Auditoría Transparente: Todas las decisiones del sistema son justificables ante padres, docentes y la ley gracias al módulo SHAP integrado.

🗺️ 9. Hoja de Ruta (Roadmap Técnico)

El desarrollo del MVP actual sienta las bases para un escalamiento de grado empresarial.

Hito 1: MVP (Actual - Completado)

$$x$$

 Pipeline de datos sintéticos con correlaciones realistas.

$$x$$

 CatBoost/XGBoost Agent con inferencia en memoria.

$$x$$

 Motor de explicabilidad SHAP.

$$x$$

 Interfaz de simulación y gráficas interactivas.

Hito 2: Beta Institucional (B2G Pilot)

$$$$

 Integración de inferencia causal algorítmica usando Microsoft DoWhy o EconML.

$$$$

 Conexión a bases de datos relacionales institucionales (PostgreSQL).

$$$$

 Autenticación segura (OAuth2 / SSO para instituciones públicas).

$$$$

 Dockerización completa para despliegues on-premise en servidores del Estado.

Hito 3: IA Orquestadora Autónoma

$$$$

 Integración de LangChain (ReAct).

$$$$

 El sistema no solo responderá simulaciones, sino que propondrá el portafolio óptimo de intervenciones maximizando un presupuesto fijo (Ej. "Tienes 10,000€. Asigna tutorías a estos 5 alumnos y becas a estos 2 para salvar el mayor número de trayectorias").

<div align="center">

<b>edUPath IM</b>

<i>Ingeniería colombiana para la resolución de retos globales.</i>

Contacto: Juan Camilo Bermúdez | Miguel Alejandro Bermúdez

© 2024 Todos los derechos reservados.

</div>
