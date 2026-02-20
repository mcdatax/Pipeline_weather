# 📁 Estructura del Proyecto - Pipeline Weather

## 📋 Descripción de Archivos

### 🔐 Configuración y Seguridad

- **`.env`** - Tus credenciales REALES (NUNCA compartir ni subir a GitHub)
  - Contiene: API keys, tokens, números de teléfono
  - ⚠️ Este archivo está protegido por `.gitignore`

- **`.env.example`** - Plantilla de ejemplo para credenciales
  - Muestra qué variables necesitas sin exponer tus datos reales
  - ✅ SÍ puedes subirlo a GitHub como documentación

- **`.gitignore`** - Protege archivos sensibles
  - Evita que `.env` y otros archivos se suban a GitHub

- **`twilio_config.py`** - Carga las credenciales desde variables de entorno
  - Lee el archivo `.env` automáticamente
  - Exporta las variables para usar en tus notebooks

---

### 📓 Notebooks

#### **`twilio_messages.ipynb`** - 🚀 Notebook Principal (Trabajo)
Tu notebook de trabajo donde desarrollas tu proyecto.
- Mantén aquí solo el código de tu pipeline
- Limpio y enfocado en avanzar tu proyecto
- Este es el que subirás a GitHub

#### **`guia_json_requests.ipynb`** - 📚 Notebook de Guía (Referencia)
Tu guía de consulta rápida para recordar conceptos.
- Teoría sobre JSON y requests
- Ejemplos ejecutables con comentarios
- Mejores prácticas y cheat sheets
- Consúltalo cuando necesites recordar cómo hacer algo
- También puedes subirlo a GitHub como documentación

---

## 🎯 Flujo de Trabajo Recomendado

1. **Trabaja en:** `twilio_messages.ipynb`
2. **Consulta cuando necesites:** `guia_json_requests.ipynb`
3. **Nunca compartas:** `.env` (tus credenciales reales)
4. **SÍ comparte:** `.env.example`, `.gitignore`, ambos notebooks

---

## 🔄 Regla de Organización

**De ahora en adelante:**
- ✅ Código de proyecto → `twilio_messages.ipynb`
- ✅ Ejemplos educativos → `guia_json_requests.ipynb` (a menos que indiques lo contrario)
- ✅ Credenciales → `.env` (nunca en el código)

---

## 📌 Recordatorios

- Antes de hacer `git push`, verifica que `.env` NO esté en staging
- Si necesitas nuevas credenciales, agrégalas al `.env` Y al `.env.example` (sin el valor real)
- Mantén tu notebook principal limpio y enfocado en tu proyecto

---

**¡Buena suerte con tu proyecto! 🚀**
