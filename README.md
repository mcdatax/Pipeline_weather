<div align="center">

# 🌤️ Pipeline Weather

### Alertas automáticas de lluvia vía SMS
*Sistema de notificaciones meteorológicas usando WeatherAPI y Twilio*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Twilio](https://img.shields.io/badge/Twilio-SMS-red?logo=twilio&logoColor=white)](https://www.twilio.com/)
[![WeatherAPI](https://img.shields.io/badge/WeatherAPI-Free-orange)](https://www.weatherapi.com/)

[Características](#-características) • [Instalación](#-instalación) • [Uso](#-uso) • [Configuración](#️-configuración)

</div>

---

## 📋 Descripción

**Pipeline Weather** es un script de Python que consulta el pronóstico del clima de una ciudad y envía alertas SMS cuando se pronostica lluvia durante el día. Utiliza la API gratuita de WeatherAPI para obtener datos meteorológicos y Twilio para enviar notificaciones a tu teléfono móvil.

### 🎯 Objetivo

Recibir alertas automáticas por SMS con las horas exactas en que se pronostica lluvia, para que puedas planificar tu día y no olvidar el paraguas.

---

## ✨ Características

- 🌧️ **Detección de lluvia**: Identifica automáticamente las horas con pronóstico de lluvia
- 📱 **Alertas SMS**: Envía notificaciones a tu teléfono móvil
- ⏰ **Horario inteligente**: Solo alerta sobre lluvia entre las 6 AM y 10 PM
- 🌍 **Cualquier ciudad**: Configurable para consultar cualquier ubicación
- 📊 **Procesamiento con Pandas**: Organiza y filtra datos meteorológicos
- 🎨 **Interfaz amigable**: Barra de progreso con tqdm

---

## 🛠️ Tecnologías

| Componente | Tecnología |
|-----------|------------|
| **Lenguaje** | Python 3.8+ |
| **API Clima** | WeatherAPI (gratuita) |
| **SMS** | Twilio |
| **Procesamiento** | Pandas |
| **HTTP** | Requests |
| **Variables de entorno** | python-dotenv |

---

## 📁 Estructura del Proyecto

```
Pipeline_weather/
│
├── twilio_script.py          # Script principal
├── utils.py                  # Funciones auxiliares
├── twilio_config.py          # Configuración y credenciales
├── requirements.txt          # Dependencias del proyecto
├── .env                      # Variables de entorno (no incluido)
└── README.md                 # Este archivo
```

---

## 🚀 Instalación

### Prerrequisitos

1. **Python 3.8 o superior**
2. **Cuenta Twilio** (gratuita para pruebas)
   - Regístrate en [twilio.com](https://www.twilio.com/try-twilio)
   - Obtén tu Account SID y Auth Token
   - Obtén un número de teléfono Twilio
3. **API Key de WeatherAPI** (gratuita)
   - Regístrate en [weatherapi.com](https://www.weatherapi.com/)
   - Obtén tu API key gratuita

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/mcdatax/Pipeline_weather.git
cd Pipeline_weather
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto:

```env
# Credenciales de Twilio
TWILIO_ACCOUNT_SID=tu_account_sid_aqui
TWILIO_AUTH_TOKEN=tu_auth_token_aqui
TWILIO_PHONE_NUMBER=+1234567890

# API Key de WeatherAPI
API_KEY_WAPI=tu_api_key_aqui

# Número de destino (tu teléfono)
PHONE_NUMBER_DESTINATION=+34612345678
```

---

## 💻 Uso

### Ejecución básica

```bash
python twilio_script.py
```

### Cambiar la ciudad

Edita el archivo `twilio_script.py`:

```python
city = 'Barcelona'  # Cambia a la ciudad que desees
```

### Ejemplo de salida

Si hay lluvia pronosticada:
```
100%|████████████████████| 24/24 [00:00<00:00, 48.23it/s]
SM1234567890abcdef1234567890abcdef
```

**SMS recibido:**
```
Alerta Madrid: Lluvia a las 14, 15, 18 horas
```

Si no hay lluvia:
```
Hoy no va a llover, disfruta del buen clima !
```

---

## ⚙️ Configuración

### Datos meteorológicos extraídos

El script consulta el pronóstico cada hora (24 horas) y extrae:

- **date**: Fecha del pronóstico
- **hour**: Hora del día (0-23)
- **condition**: Descripción del clima
- **temp_c**: Temperatura en Celsius
- **will_it_rain**: Si lloverá (0/1)
- **chance_of_rain**: Probabilidad de lluvia (%)

### Filtros aplicados

- Solo considera lluvia entre **6 AM y 10 PM**
- Solo envía alerta si `will_it_rain == 1`
- Ordena las horas de forma ascendente

### Personalización

En `utils.py` puedes modificar:

```python
# Cambiar el rango de horas
df_rain = df[(df['will_it_rain']==1) & (df['hour']>6) & (df['hour']< 22)]
```

---

## 📦 Dependencias

```
twilio>=8.0.0              # API para enviar SMS
pandas>=1.5.0              # Procesamiento de datos
requests>=2.28.0           # Peticiones HTTP
beautifulsoup4>=4.11.0     # Parsing HTML
tqdm>=4.64.0               # Barra de progreso
python-dotenv>=0.21.0      # Variables de entorno
```

---

## 🔧 Funciones principales

### `request_wapi(api_key, city)`
Consulta la API de WeatherAPI y obtiene el pronóstico de 24 horas.

### `get_forecast_data(response, i)`
Extrae los datos meteorológicos de una hora específica.

### `create_df(data)`
Crea un DataFrame de pandas y filtra las horas con lluvia.

### `send_message(...)`
Envía el SMS con la alerta de lluvia usando Twilio.

---

## 🚀 Automatización

Para ejecutar automáticamente todos los días:

### Linux/Mac (cron)

```bash
# Editar crontab
crontab -e

# Ejecutar todos los días a las 7 AM
0 7 * * * cd /ruta/al/proyecto && /ruta/al/venv/bin/python twilio_script.py
```

### Windows (Task Scheduler)

1. Abre el Programador de tareas
2. Crea una tarea básica
3. Configura el trigger (ej: diario a las 7 AM)
4. Acción: ejecutar `python.exe` con el script como argumento

---

## 💰 Costos

- **WeatherAPI**: Gratis hasta 1M llamadas/mes
- **Twilio**: 
  - $15 USD de crédito inicial
  - ~$0.0075 por SMS (varía según país)
  - Un SMS diario = ~$0.23/mes

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📝 Mejoras futuras

- [ ] Soporte para múltiples ciudades
- [ ] Alertas de temperatura extrema
- [ ] Integración con AWS Lambda para ejecución serverless
- [ ] Dashboard web simple
- [ ] Histórico de alertas enviadas
- [ ] Tests unitarios

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**mcdatax**

- GitHub: [@mcdatax](https://github.com/mcdatax)
- Proyecto: [Pipeline_weather](https://github.com/mcdatax/Pipeline_weather)

---

## 🙏 Agradecimientos

- [WeatherAPI](https://www.weatherapi.com/) por su API gratuita
- [Twilio](https://www.twilio.com/) por facilitar el envío de SMS
- Comunidad de Python por las excelentes librerías

---

<div align="center">

**⭐ Si te resulta útil, considera darle una estrella ⭐**

[Reportar Bug](https://github.com/mcdatax/Pipeline_weather/issues) • [Solicitar Feature](https://github.com/mcdatax/Pipeline_weather/issues)

</div>