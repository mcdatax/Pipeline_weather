# twilio_config.py
# Este archivo carga las credenciales desde variables de entorno de forma segura

# Importar la librería 'os' para acceder a las variables de entorno del sistema
import os

# Importar 'load_dotenv' para cargar el archivo .env automáticamente
from dotenv import load_dotenv

# Cargar las variables del archivo .env al entorno del sistema
# Esto lee el archivo .env y hace disponibles las variables
load_dotenv()

# Obtener cada credencial desde las variables de entorno
# os.getenv('NOMBRE_VARIABLE') busca la variable en el entorno
# Si no la encuentra, devuelve None (o el valor por defecto que indiques)

# Credencial 1: Account SID de Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')

# Credencial 2: Token de autenticación de Twilio  
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# Credencial 3: Número de teléfono de Twilio (formato E.164)
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Credencial 4: API Key de Weather API
API_KEY_WAPI = os.getenv('API_KEY_WAPI')

# Credencial 5: Número de teléfono de destino (a quien enviarás los mensajes)
PHONE_NUMBER_DESTINATION = os.getenv('PHONE_NUMBER_DESTINATION')

# Opcional: Verificar que todas las credenciales fueron cargadas correctamente
# Esto te avisará si falta alguna variable en tu archivo .env
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, API_KEY_WAPI, PHONE_NUMBER_DESTINATION]):
    print("⚠️  ADVERTENCIA: Faltan algunas credenciales en tu archivo .env")
    print("Asegúrate de que tu archivo .env contiene todas las variables necesarias")
