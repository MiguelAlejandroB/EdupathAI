# 🧠 Modelos de Machine Learning y Causalidad

> *"Pasar de la correlación a la causalidad es lo que transforma un tablero de métricas en una herramienta de Inteligencia de Decisión."*

El núcleo algorítmico de **edUPath IM** se basa en un pipeline de tres etapas: **Predicción Robusta, Explicabilidad Ética e Inferencia Causal**. A continuación, detallamos la arquitectura técnica de cada componente.

---

## 1. Predicción de Riesgo Estacional: CatBoost

Para la predicción base de deserción (horizonte a 12 meses), utilizamos **CatBoost** (Categorical Boosting).

### ¿Por qué CatBoost?
Los datos educativos tabulares están repletos de variables categóricas de alta cardinalidad (ej. ID del colegio, barrio, nivel socioeconómico de los padres). CatBoost maneja estas variables de forma nativa mediante *target encoding* u *ordered boosting*, evitando el sobreajuste masivo que generarían técnicas como el *One-Hot Encoding* tradicional, y lidiando excelentemente con valores nulos (típicos en bases de datos gubernamentales).

### Implementación Base (Ejemplo)

```python
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split

# 1. Definición de variables categóricas
categorical_features = ['grado', 'institucion_id', 'estrato_socioeconomico', 'zona_residencia']

# 2. Creación del Pool de datos
train_pool = Pool(data=X_train, label=y_train, cat_features=categorical_features)
test_pool = Pool(data=X_test, label=y_test, cat_features=categorical_features)

# 3. Inicialización y entrenamiento del modelo predictivo
model_predictivo = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    loss_function='Logloss',
    eval_metric='AUC',
    early_stopping_rounds=50,
    random_seed=42,
    verbose=100
)

model_predictivo.fit(train_pool, eval_set=test_pool)

```

---

## 2. Explicabilidad Ética: SHAP (SHapley Additive exPlanations)

El sector público y social no puede tomar decisiones basadas en "Cajas Negras". Utilizamos **SHAP**, fundamentado en la teoría de juegos cooperativos, para calcular la contribución marginal de cada variable en la predicción de riesgo de un estudiante específico.

### Explicabilidad Local (Individual)

Para un estudiante , SHAP nos permite descomponer su predicción de riesgo  en la suma de los efectos de sus características individuales :

Donde  es el riesgo base (esperado) de toda la población.

### Integración en edUPath IM

Cuando el Agente de IA detecta un pico de riesgo en el **Q2**, consulta el `TreeExplainer` de SHAP para retornar en lenguaje natural *por qué* está ocurriendo (ej. "Inasistencias acumuladas" + "Baja nota en matemáticas").

```python
import shap

# Inicializar el explicador basado en el modelo CatBoost entrenado
explainer = shap.TreeExplainer(model_predictivo)

# Calcular valores SHAP para el estudiante consultado
shap_values = explainer.shap_values(estudiante_X)

# Generar gráfico de fuerza (Force Plot) para la interfaz de Streamlit
shap.force_plot(
    explainer.expected_value, 
    shap_values[0,:], 
    estudiante_X.iloc[0,:]
)

```

---

## 3. Inferencia Causal: DoWhy (Microsoft)

Este es el verdadero diferenciador (Nivel 6) de edUPath IM: el simulador de escenarios contrafactuales o motor **"What-If"**.

Mientras que el ML tradicional encuentra correlaciones, la inferencia causal nos permite estimar el **Efecto Promedio del Tratamiento (ATE - Average Treatment Effect)** y el **Efecto del Tratamiento Individual (ITE)**. Matemáticamente, buscamos estimar la diferencia en el resultado probabilístico  si aplicamos un tratamiento  (ej. Beca Alimentaria):

Dado que no podemos observar ambos estados simultáneamente (el problema fundamental de la inferencia causal), utilizamos el framework **DoWhy** para modelar el grafo causal y estimar este efecto eliminando variables de confusión (*confounders*).

### Pipeline de DoWhy en edUPath

```python
import dowhy
from dowhy import CausalModel

# Paso 1: Modelar el problema causal (Grafo Dirigido Acíclico - DAG)
model_causal = CausalModel(
    data=df_historico,
    treatment='recibio_transporte_escolar', # La intervención a simular
    outcome='deserto_q4',                   # Nuestro target predictivo
    common_causes=['estrato', 'distancia_colegio', 'notas_previas'] # Confounders
)

# Paso 2: Identificar el efecto (Criterio Backdoor)
identified_estimand = model_causal.identify_effect(proceed_when_unidentifiable=True)

# Paso 3: Estimar el efecto causal (Ej: Propensity Score Matching)
estimate = model_causal.estimate_effect(
    identified_estimand,
    method_name="backdoor.propensity_score_matching"
)

# Paso 4: Refutar la estimación (Validación de robustez)
refute_results = model_causal.refute_estimate(
    identified_estimand, 
    estimate,
    method_name="random_common_cause"
)

print(f"Efecto Causal Estimado (Reducción de Riesgo): {estimate.value}")

```

!!! success "Impacto en la Interfaz"
El valor de `estimate.value` es lo que se traduce visualmente en la **línea verde punteada** de nuestra plataforma, mostrando a los tomadores de decisión exactamente cuántos puntos porcentuales bajará el riesgo de deserción si invierten en esa intervención.

```
