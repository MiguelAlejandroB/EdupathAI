# 🎨 Experiencia de Usuario (UX) y Narrativa de Datos

> *El objetivo de nuestro prototipo no es mostrar "tablas de Excel" incomprensibles, sino contar la historia de riesgo del estudiante a través de una **Narrativa de Datos**.*

Para asegurar que la herramienta sea adoptada por los usuarios finales (Docentes, Psico-orientadores y Trabajadores Sociales con perfil no técnico), hemos diseñado una interfaz bajo principios de minimalismo, limpieza visual y alto contraste para las alertas tempranas.

---

## 🗺️ Flujo de Usuario (User Journey)

El recorrido está diseñado para reducir la carga cognitiva al mínimo indispensable, operando bajo el ciclo: **Pregunta $\rightarrow$ Visualización $\rightarrow$ Acción**.

```mermaid
graph TD
    A[Inicio: Chat Conversacional] -->|Ingresa nombre estudiante| B[Dashboard: Línea de Tiempo]
    B -->|Click en Trimestre Q2| C[Pop-up: Explicabilidad SHAP]
    B -->|Seleccionar 'Simular'| D[Panel de Intervenciones]
    D -->|Activar 'Ruta Escolar'| E[Visualización Contrafactual]
    E -->|Comparar Curvas| F[Exportar Reporte PDF]