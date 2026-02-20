# 🚀 Despliegue Completo en AWS EC2 - Guía Paso a Paso

## 📋 Pre-requisitos

- ✅ Cuenta AWS (nivel gratuito)
- ✅ Instancia EC2 creada
- ✅ Archivo `.pem` descargado
- ✅ IP pública de tu instancia
- ✅ Código funcionando en local

---

## 🎯 Objetivo Final

Automatizar tu script de clima para que:
- Se ejecute cada mañana a las 7 AM
- Consulte el clima de Madrid
- Te envíe SMS si va a llover
- Todo automático, sin intervención manual

---

## 📝 PASO 1: Preparar tu Proyecto Local

### **1.1 Organizar Archivos**

```bash
# Tu estructura actual
Pipeline_weather/
├── .env                    # Credenciales (NO se sube)
├── .gitignore              # Protege secretos
├── .ssh/                   # Claves AWS (NO se sube)
│   └── tu-archivo.pem
├── twilio_config.py        # Carga variables de .env
├── twilio_messages.ipynb   # Notebook de desarrollo
└── docs/                   # Documentación
```

### **1.2 Crear Script Python Ejecutable**

Necesitas convertir tu notebook en un script `.py`:

```bash
# Crear archivo weather_sms.py
touch weather_sms.py
```

**Contenido de `weather_sms.py`:**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para enviar alerta de clima por SMS usando Twilio
Ejecutar diariamente a las 7 AM via CRON
"""

import os
import requests
import pandas as pd
from twilio.rest import Client
from twilio_config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    API_KEY_WAPI,
    PHONE_NUMBER_DESTINATION
)

def get_forecast_data(response, i):
    """Extrae datos de pronóstico de la API"""
    date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
    hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text'].strip()
    temp_c = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    will_it_rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    chance_of_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
    
    return date, hour, condition, temp_c, will_it_rain, chance_of_rain

def main():
    """Función principal"""
    # Configuración
    city = 'Madrid'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY_WAPI}&q={city}&days=1&aqi=no&alerts=no'
    
    # Obtener datos del clima
    response = requests.get(url).json()
    
    # Procesar datos
    datos = []
    for i in range(len(response['forecast']['forecastday'][0]['hour'])):
        forecast_data = get_forecast_data(response, i)
        datos.append(forecast_data)
    
    # Crear DataFrame
    cols = ['date', 'hour', 'condition', 'temp_c', 'will_it_rain', 'chance_of_rain']
    df = pd.DataFrame(datos, columns=cols)
    
    # Filtrar horas de lluvia (6am - 8pm)
    df_rain = df[(df['will_it_rain'] == 1) & (df['hour'] >= 6) & (df['hour'] <= 20)]
    
    # Crear mensaje
    if not df_rain.empty:
        # HAY LLUVIA
        horas_lluvia = ", ".join(df_rain['hour'].astype(str))
        mensaje_sms = f"Alerta Madrid: Lluvia a las {horas_lluvia} horas"
    else:
        # NO HAY LLUVIA
        mensaje_sms = "Hoy no va a llover, disfruta del buen clima!"
    
    # Enviar SMS
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=mensaje_sms,
        from_=TWILIO_PHONE_NUMBER,
        to=PHONE_NUMBER_DESTINATION
    )
    
    # Confirmar envío
    print(f"✅ SMS enviado exitosamente!")
    print(f"📋 SID: {message.sid}")
    print(f"📊 Estado: {message.status}")
    print(f"📱 Mensaje: {mensaje_sms}")

if __name__ == "__main__":
    main()
```

### **1.3 Subir a GitHub**

```bash
cd /Users/mane/Documents/Pipeline_weather

# Inicializar Git (si no lo has hecho)
git init

# Agregar archivos
git add .

# Commit
git commit -m "Proyecto clima automatizado"

# Crear repositorio en GitHub
# Ve a: https://github.com/new
# Crea repositorio "pipeline-weather"

# Conectar con GitHub
git remote add origin https://github.com/TU-USUARIO/pipeline-weather.git
git branch -M main
git push -u origin main
```

**Verificar que .env NO se subió:**
```bash
git ls-files | grep .env
# No debe mostrar nada
```

---

## 🔐 PASO 2: Configurar Acceso a EC2

### **2.1 Mover archivo .pem**

```bash
# Copiar tu .pem a la carpeta .ssh/
cp ~/Downloads/tu-archivo.pem /Users/mane/Documents/Pipeline_weather/.ssh/

# Ajustar permisos (OBLIGATORIO)
chmod 400 .ssh/tu-archivo.pem

# Verificar
ls -la .ssh/
# Debe mostrar: -r-------- tu-archivo.pem
```

### **2.2 Primera Conexión SSH**

```bash
# Conectarte a tu instancia
ssh -i .ssh/tu-archivo.pem ubuntu@TU-IP-PUBLICA

# Si sale warning de "fingerprint":
# Escribe: yes

# Deberías ver:
# Welcome to Ubuntu...
# ubuntu@ip-xxx-xxx-xxx-xxx:~$
```

**Si hay error "Permission denied":**
```bash
chmod 400 .ssh/tu-archivo.pem
```

**Si hay error "Connection refused":**
- Verifica que la IP sea correcta
- Verifica Security Group en AWS (debe permitir SSH port 22)

---

## 📦 PASO 3: Configurar Instancia EC2

### **3.1 Actualizar Sistema**

```bash
# Ya conectado en EC2
sudo apt update && sudo apt upgrade -y
```

### **3.2 Instalar Python y Pip**

```bash
# Instalar Python 3 y pip
sudo apt install python3 python3-pip -y

# Verificar instalación
python3 --version  # Debe mostrar: Python 3.x.x
pip3 --version     # Debe mostrar: pip 2x.x.x
```

### **3.3 Instalar Git**

```bash
# Instalar Git
sudo apt install git -y

# Verificar
git --version
```

---

## 📥 PASO 4: Clonar tu Proyecto

### **4.1 Clonar Repositorio**

```bash
# Clonar desde GitHub
git clone https://github.com/TU-USUARIO/pipeline-weather.git

# Entrar al directorio
cd pipeline-weather

# Ver archivos
ls -la
```

### **4.2 Instalar Dependencias**

```bash
# Instalar paquetes Python
pip3 install python-dotenv twilio requests pandas beautifulsoup4 tqdm

# Verificar instalación
pip3 list | grep twilio
```

---

## 🔑 PASO 5: Configurar Variables de Entorno

### **5.1 Crear archivo .env**

```bash
# Crear .env en EC2
nano .env
```

Pega tus credenciales:
```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+15822334031
API_KEY_WAPI=xxxxxxxxxxxxxxxxxxxxx
PHONE_NUMBER_DESTINATION=+34606864731
```

**Guardar:**
- Presiona `Ctrl+O` (escribir)
- Presiona `Enter` (confirmar)
- Presiona `Ctrl+X` (salir)

### **5.2 Ajustar Permisos**

```bash
# Solo tú puedes leer .env
chmod 600 .env

# Verificar
ls -la .env
# Debe mostrar: -rw------- .env
```

### **5.3 Verificar que funciona**

```bash
# Probar script
python3 weather_sms.py

# Deberías recibir un SMS y ver:
# ✅ SMS enviado exitosamente!
# 📋 SID: SMxxxxxxx
# 📊 Estado: queued
```

---

## ⏰ PASO 6: Automatizar con CRON

### **6.1 Entender CRON**

CRON es el programador de tareas de Linux:

```
┌─────────── minuto (0-59)
│ ┌────────── hora (0-23)
│ │ ┌──────── día del mes (1-31)
│ │ │ ┌────── mes (1-12)
│ │ │ │ ┌──── día de la semana (0-7, 0=domingo)
│ │ │ │ │
│ │ │ │ │
* * * * * comando a ejecutar
```

**Ejemplos:**
- `0 7 * * *` → Cada día a las 7:00 AM
- `30 8 * * *` → Cada día a las 8:30 AM
- `0 7 * * 1-5` → Lunes a Viernes a las 7:00 AM
- `0 */6 * * *` → Cada 6 horas

### **6.2 Crear Script Wrapper**

```bash
# Crear script wrapper
nano /home/ubuntu/run_weather.sh
```

Contenido:
```bash
#!/bin/bash
# Script wrapper para ejecutar weather_sms.py

# Ir al directorio del proyecto
cd /home/ubuntu/pipeline-weather

# Ejecutar script
/usr/bin/python3 weather_sms.py >> /home/ubuntu/weather.log 2>&1

# Agregar timestamp
echo "Ejecutado: $(date)" >> /home/ubuntu/weather.log
```

Guardar: `Ctrl+O`, `Enter`, `Ctrl+X`

```bash
# Dar permisos de ejecución
chmod +x /home/ubuntu/run_weather.sh

# Probar
/home/ubuntu/run_weather.sh

# Ver log
cat /home/ubuntu/weather.log
```

### **6.3 Configurar CRON**

```bash
# Abrir editor de crontab
crontab -e

# Si pregunta editor, elige: nano (opción 1)
```

Agregar al final del archivo:
```bash
# Enviar alerta de clima cada día a las 7:00 AM
0 7 * * * /home/ubuntu/run_weather.sh

# Opcional: También a las 3 PM
0 15 * * * /home/ubuntu/run_weather.sh
```

Guardar: `Ctrl+O`, `Enter`, `Ctrl+X`

### **6.4 Verificar CRON**

```bash
# Ver tareas programadas
crontab -l

# Ver logs de cron
grep CRON /var/log/syslog | tail -20

# Ver tu log personalizado
tail -f /home/ubuntu/weather.log
```

---

## ✅ PASO 7: Verificación Final

### **7.1 Checklist de Seguridad**

```bash
# 1. Verificar que .env no está en Git
git ls-files | grep .env
# No debe mostrar nada

# 2. Verificar permisos de .env
ls -la .env
# Debe ser: -rw-------

# 3. Verificar que credenciales funcionan
python3 -c "from twilio_config import *; print('✅ Credenciales OK')"

# 4. Ver tareas CRON
crontab -l
```

### **7.2 Monitoreo**

```bash
# Ver logs en tiempo real
tail -f /home/ubuntu/weather.log

# Ejecutar manualmente para probar
/home/ubuntu/run_weather.sh
```

---

## 🔄 PASO 8: Mantenimiento

### **8.1 Actualizar Código**

```bash
# Conectarte a EC2
ssh -i .ssh/tu-archivo.pem ubuntu@TU-IP

# Actualizar desde GitHub
cd /home/ubuntu/pipeline-weather
git pull origin main

# Si modificaste .env, no se sobrescribirá (está en .gitignore)
```

### **8.2 Ver Logs**

```bash
# Ver últimas 50 líneas del log
tail -50 /home/ubuntu/weather.log

# Ver logs de hoy
grep "$(date +%Y-%m-%d)" /home/ubuntu/weather.log

# Limpiar logs antiguos
> /home/ubuntu/weather.log
```

### **8.3 Reiniciar Instancia**

```bash
# Desde AWS Console o desde SSH
sudo reboot

# Reconectar después de 1-2 minutos
ssh -i .ssh/tu-archivo.pem ubuntu@TU-IP

# Verificar que CRON sigue activo
crontab -l
```

**¿CRON persiste?** ✅ SÍ  
**¿.env persiste?** ✅ SÍ  
**¿Código persiste?** ✅ SÍ

---

## 🆘 Troubleshooting

### **Error: "No module named 'dotenv'"**
```bash
pip3 install python-dotenv
```

### **Error: "No module named 'twilio'"**
```bash
pip3 install twilio
```

### **CRON no ejecuta el script**
```bash
# Ver errores de cron
grep CRON /var/log/syslog

# Verificar permisos del script
chmod +x /home/ubuntu/run_weather.sh

# Verificar rutas absolutas en crontab
which python3  # Copiar esta ruta
crontab -e     # Usar ruta absoluta
```

### **No recibes SMS**
```bash
# Ejecutar manualmente y ver errores
python3 weather_sms.py

# Ver si hay errores en log
cat /home/ubuntu/weather.log
```

---

## 💡 Optimizaciones Opcionales

### **1. Usar Entorno Virtual**
```bash
cd /home/ubuntu/pipeline-weather
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **2. Crear requirements.txt**
```bash
# En tu Mac, exportar dependencias
pip freeze > requirements.txt

# En EC2, instalar desde archivo
pip3 install -r requirements.txt
```

### **3. Agregar Notificaciones de Error**
```python
# Modificar weather_sms.py para enviar errores por SMS
try:
    main()
except Exception as e:
    client.messages.create(
        body=f"❌ Error en script clima: {str(e)}",
        from_=TWILIO_PHONE_NUMBER,
        to=PHONE_NUMBER_DESTINATION
    )
```

---

## 📊 Resumen de Comandos Útiles

```bash
# Conectarse a EC2
ssh -i .ssh/tu-archivo.pem ubuntu@IP

# Ver logs
tail -f /home/ubuntu/weather.log

# Ejecutar manualmente
/home/ubuntu/run_weather.sh

# Editar CRON
crontab -e

# Ver tareas CRON
crontab -l

# Actualizar código
git pull origin main

# Salir de EC2
exit
```

---

## ✅ ¡Listo!

Tu sistema está completamente automatizado:
- ✅ Código en GitHub (sin credenciales)
- ✅ Instancia EC2 configurada
- ✅ Variables de entorno seguras (.env)
- ✅ CRON ejecutando diariamente
- ✅ Logs para monitoreo
- ✅ Todo persiste después de reiniciar

**Cada mañana a las 7 AM recibirás automáticamente tu alerta de clima!** 🎯
