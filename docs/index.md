
<div align="center">
# 🏛️ edUPath IM

### Sistema de Inteligencia de Decisión para la Retención Escolar

[![Versión MVP](https://img.shields.io/badge/Versi%C3%B3n-1.0.0--MVP-blue.svg?style=for-the-badge)](#)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OdiseIA 4Good](https://img.shields.io/badge/OdiseIA-Finalista_4Good-FFD700.svg?style=for-the-badge&logo=hackerrank&logoColor=black)](#)

> *"El abandono escolar no es una fatalidad, es un fallo predecible del sistema. edUPath IM transforma el gasto público reactivo en inversión social predictiva."*

---

## 🚀 Bienvenido a edUPath IM

> **Transformando la reacción en prevención a través de la Inteligencia de Decisión.**

**edUPath IM** no es un tablero de control tradicional. Es una plataforma operativa de Inteligencia Artificial diseñada para anticipar, comprender y mitigar la deserción escolar antes de que ocurra. 

Pasamos de analizar el pasado (Business Intelligence) a simular el futuro (**Decision Intelligence**), optimizando la asignación de recursos públicos y sociales donde realmente generan impacto.

> 🏆 **Finalistas OdiseIA 4Good:** Este proyecto es uno de los 88 finalistas seleccionados para presentar su solución de impacto. Nuestra misión: demostrar que la IA puede mantener a los jóvenes en las aulas y romper los ciclos de pobreza.

### 🎯 Nuestra Propuesta de Valor

El sistema educativo actual es reactivo y genérico. Nosotros proponemos un enfoque basado en tres pilares:

1. 🔮 **Anticipación Inteligente:** Capacidad de predecir el riesgo de deserción de un estudiante con hasta **1 año de antelación**, permitiendo intervenciones tempranas.
2. 🔀 **Simulación Contrafactual:** Resolvemos la pregunta *"¿Qué pasaría con la trayectoria de este estudiante si aplicamos la intervención X hoy?"* validando estrategias antes de gastar recursos.
3. ⚖️ **Enfoque Ético:** Evitamos el sesgo de la "caja negra". Cada predicción viene acompañada de una explicación clara de sus factores de riesgo.

---

## 🗺️ ¿Cómo navegar por esta documentación?

Hemos estructurado esta documentación en módulos para adaptarse a tu perfil. Selecciona la ruta que mejor se ajuste a lo que buscas:

* **📊 Para Perfiles de Negocio y Jurado Social:** [El Problema y Solución](negocio/problema_solucion.md) • [Business Model Canvas](negocio/modelo_canvas.md) • [UX y Narrativa](negocio/ux_experiencia.md)
* **⚙️ Para Perfiles Técnicos y Desarrolladores:** [Arquitectura del Sistema](tecnico/arquitectura.md) • [Modelos de ML](tecnico/modelos_ml.md) • [Agentes IA](tecnico/agentes_ia.md) • [Setup Local](tecnico/setup_local.md)
* **🏆 Área Interna (OdiseIA):** [Estrategia Pitch Final](odiseia/pitch_final.md)

---

## 📑 Detalles del Proyecto (Quick Look)

* [1. Resumen Ejecutivo](#1-resumen-ejecutivo)
* [2. El Caso de Negocio (Business Case)](#2-el-caso-de-negocio-business-case)
* [3. Arquitectura Tecnológica e Innovación](#3-arquitectura-tecnológica-e-innovación)
* [4. Módulo Predictivo y Explicabilidad (SHAP)](#4-módulo-predictivo-y-explicabilidad-shap)
* [5. Simulador Contrafactual (Causalidad)](#5-simulador-contrafactual-causalidad)
* [6. Guía Rápida de Despliegue](#6-guía-rápida-de-despliegue-quick-start)
* [7. Manual de Usuario: Flujo de Operación](#7-manual-de-usuario-flujo-de-operación)
* [8. Privacidad, Ética y Cumplimiento](#8-privacidad-ética-y-cumplimiento)
* [9. Hoja de Ruta (Roadmap)](#9-hoja-de-ruta-roadmap-técnico)

---

## 🏢 1. Resumen Ejecutivo

**edUPath IM (Intelligence Management)** es una plataforma SaaS B2G/B2NGO diseñada para revolucionar la forma en que los Estados y las instituciones educativas gestionan la deserción escolar.

A diferencia de los sistemas de Business Intelligence tradicionales, utilizamos modelos avanzados de Machine Learning combinados con inferencia causal para crear un "gemelo digital" del comportamiento estudiantil, permitiendo a los tomadores de decisiones anticipar el fracaso y simular la efectividad de sus políticas antes de financiarlas.

## 📉 2. El Caso de Negocio (Business Case)

El paradigma actual de la administración pública frente a la deserción escolar sufre de un grave sesgo de latencia. Las intervenciones se activan cuando la desconexión del estudiante es irreversible.

**Coste del Status Quo:**
* **Inversión Ciega:** Asignación de recursos sin validación de impacto individual.
* **Costo Social:** Aumento del paro juvenil y riesgo psicosocial.
* **Costo Fiscal:** Cada estudiante que abandona representa cientos de miles de euros en futuros gastos penales, subsidios y pérdida de recaudación.

**La Solución: Retorno de Prevención (RoP)**

| Dimensión | Sistema Tradicional | edUPath IM |
| :--- | :--- | :--- |
| **Enfoque Temporal** | Reactivo (Post-mortem) | Preventivo (T-12 meses) |
| **Asignación de Capital** | Basado en intuición | Basado en simulación contrafactual |
| **Nivel de Acción** | Cohortes generales | Hiper-segmentado por individuo |
| **Transparencia** | Cajas negras o reglas simples | Valores SHAP (Auditable y explicable) |

> **Métrica Clave:** Validar una intervención de 500€ hoy a través de edUPath IM evita incurrir en costes reactivos exponenciales mañana.

## ⚙️ 3. Arquitectura Tecnológica e Innovación

El sistema está diseñado bajo una arquitectura modular de agentes inteligentes. En su fase MVP, opera a través de un monolito eficiente en Python, estructurado en 4 capas lógicas.

```text
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

```

## 🧠 4. Módulo Predictivo y Explicabilidad (SHAP)

Los docentes y trabajadores sociales no confían en algoritmos que no pueden entender. Por ello, optamos por **Árboles de Decisión con Gradiente (XGBoost)** potenciados por **Valores Shapley (SHAP)**.

**¿Cómo funciona la Explicabilidad?**
Por cada predicción de riesgo, el sistema genera un desglose de las fuerzas que actúan sobre el estudiante:

* 🟥 **Fuerzas de Riesgo:** (Ej. Inasistencias Q3: +25% de riesgo).
* 🟩 **Fuerzas de Retención:** (Ej. Participación extracurricular: -10% de riesgo).

Esta explicabilidad es fundamental para el cumplimiento de normativas europeas sobre IA (AI Act).

## 🔮 5. Simulador Contrafactual (Causalidad)

La correlación no implica causalidad. El Simulador permite a las instituciones responder a preguntas tipo *What-If*.

**Catálogo de Intervenciones Modeladas (MVP):**

* **Beca de Transporte:** Reducción de inasistencias geográficas.
* **Tutoría Académica:** Curva de recuperación en calificaciones (GPA).
* **Apoyo Socioeconómico:** Impacto cruzado con ponderación especial para bajo Nivel Socioeconómico (NSE).

## 💻 6. Guía Rápida de Despliegue (Quick Start)

**Pasos de Ejecución Local:**

```bash
# 1. Clonar el repositorio
git clone [https://github.com/MiguelAlejandroB/EdupathAI.git](https://github.com/MiguelAlejandroB/EdupathAI.git)
cd EdupathAI

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar el servidor
streamlit run app/main.py

```

*El sistema inicializará el pipeline, entrenará el modelo y desplegará la interfaz en `http://localhost:8501`.*

## 👨‍💻 7. Manual de Usuario: Flujo de Operación

**Paso 1: Diagnóstico**

* **Operador:** *"Analiza el caso del estudiante Juan Pérez"*
* **Sistema:** Extrae ID, proyecta trayectoria, calcula riesgo futuro y despliega auditoría SHAP.

**Paso 2: Simulación de Intervención**

* **Operador:** *"Simula aplicarle una beca desde el trimestre 2"*
* **Sistema:** Clona el perfil (Gemelo Digital), inyecta la intervención y recalcula el riesgo. Superpone una curva verde demostrando la caída del riesgo (Ej. de 87% a 18%).

## 🛡️ 8. Privacidad, Ética y Cumplimiento

Diseñado bajo el principio de *Privacy by Design*:

* **Sin PII:** Solo procesa IDs hasheados. Nombres jamás tocan los modelos de ML.
* **LLM Aislado:** El procesamiento de lenguaje natural (NLP) se usa solo para orquestación, no para entrenamiento.
* **Auditoría Transparente:** Todas las decisiones son justificables gracias a SHAP.

## 🗺️ 9. Hoja de Ruta (Roadmap Técnico)

**Hito 1: MVP (Actual - Completado)**

* [x] Pipeline de datos sintéticos realistas.
* [x] Inferencia en memoria (CatBoost/XGBoost).
* [x] Explicabilidad SHAP y simulaciones visuales.

**Hito 2: Beta Institucional (B2G Pilot)**

* [ ] Integración causal algorítmica (DoWhy / EconML).
* [ ] Conexión a bases relacionales (PostgreSQL).
* [ ] Autenticación OAuth2/SSO y Dockerización.

**Hito 3: IA Orquestadora Autónoma**

* [ ] Integración de LangChain (ReAct). Optimización de presupuesto institucional para maximizar retención a gran escala.

---

<div align="center">
<h3>👥 Equipo Fundador</h3>
Nuestra fortaleza radica en la sinergia entre la tecnología y el impacto social: 





<b>Juan Camilo Bermúdez</b>: Ingeniería, IA y Data-Driven Decisions. 




<b>Miguel Alejandro Bermúdez</b>: Administración, Economía y Modelos Sostenibles. 





<hr width="50%">

<b>edUPath IM</b>




<i>Ingeniería colombiana para la resolución de retos globales.</i>




© 2026 Todos los derechos reservados.

</div>

