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
