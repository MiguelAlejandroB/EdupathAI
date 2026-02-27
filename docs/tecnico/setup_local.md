# ⚙️ Guía de Instalación Local

> *Esta guía está diseñada para que cualquier desarrollador, científico de datos o jurado técnico pueda levantar el entorno de **edUPath IM** en su máquina local en menos de 5 minutos.*

El proyecto está construido principalmente en **Python 3.10+** y utiliza **Streamlit** para la interfaz de usuario, orquestado por **LangChain**.

---

## 📋 1. Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema antes de comenzar:

* [Python 3.10 o superior](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* *(Opcional)* [Docker](https://www.docker.com/) si prefieres correrlo en contenedores.

---

## 🚀 2. Instalación Paso a Paso

Sigue estas instrucciones en tu terminal (Command Prompt, PowerShell o Terminal de MacOS/Linux).

### Paso 1: Clonar el repositorio
Descarga el código fuente a tu máquina local:
```bash
git clone [https://github.com/tu-usuario/edUPath_MVP.git](https://github.com/tu-usuario/edUPath_MVP.git)
cd edUPath_MVP

```

### Paso 2: Crear un entorno virtual (Recomendado)

Para evitar conflictos de dependencias con otros proyectos de Python, crea y activa un entorno virtual.

**En Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

**En macOS y Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

!!! success "Entorno Activado"
Sabrás que funcionó porque verás `(venv)` al inicio de la línea de tu terminal.

### Paso 3: Instalar las dependencias

Instala todas las librerías necesarias (CatBoost, SHAP, LangChain, Streamlit, etc.) usando el archivo `requirements.txt`.

```bash
pip install -r requirements.txt

```

### Paso 4: Configurar Variables de Entorno

Para que el Orquestador de IA funcione, necesitas configurar tus llaves de API.

1. Copia el archivo de ejemplo:

```bash
cp .env.example .env

```

2. Abre el archivo `.env` en tu editor de código y agrega tus credenciales:

```text
# Archivo .env
OPENAI_API_KEY="sk-tu-api-key-aqui"
DATABASE_URL="postgresql://usuario:password@localhost:5432/edupath"

```

!!! danger "Seguridad"
**Nunca** subas el archivo `.env` a GitHub. Asegúrate de que `.env` esté incluido en tu archivo `.gitignore`.

---

## 🏃 3. Ejecutar la Aplicación

¡Ya está todo listo! Para levantar la interfaz de usuario de Streamlit, ejecuta:

```bash
streamlit run app/main.py

```

Esto abrirá automáticamente una pestaña en tu navegador web por defecto en `http://localhost:8501`.

---

## 🐳 Alternativa: Despliegue con Docker (Production-Ready)

Si no quieres lidiar con versiones de Python o dependencias locales, hemos preparado el proyecto para correr en un contenedor aislado.

```bash
# Construir y levantar el contenedor en segundo plano
docker-compose up --build -d

```

Una vez que termine, la aplicación estará disponible en el mismo puerto `8501`.

---

## 🛠️ Solución de Problemas Comunes (Troubleshooting)

* **Error `ModuleNotFoundError: No module named 'catboost'**`: Asegúrate de haber activado el entorno virtual (`Paso 2`) antes de hacer la instalación.
* **Error de Streamlit `Address already in use**`: Significa que tienes otra aplicación corriendo en el puerto 8501. Cierra el proceso o corre Streamlit en otro puerto: `streamlit run app/main.py --server.port 8502`.
* **El Chat de IA no responde**: Verifica que tu `OPENAI_API_KEY` en el archivo `.env` sea válida y tenga créditos disponibles.

```