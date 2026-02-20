# 📚 Documentación del Proyecto - Pipeline Weather SMS

## 🎯 Índice de Guías

### 🔐 Seguridad y Credenciales
**[01_GESTION_CREDENCIALES_AWS.md](01_GESTION_CREDENCIALES_AWS.md)**
- ✅ Cómo manejar credenciales de forma segura
- ✅ Por qué usar archivo `.env` (la mejor práctica)
- ✅ Comparación de opciones (variables de entorno vs gestores de secretos)
- ✅ Qué hacen las empresas profesionales
- ✅ Cómo persisten las variables después de reiniciar EC2

**Temas cubiertos:**
- Archivo `.env` con python-dotenv ⭐ RECOMENDADO
- Variables de entorno del sistema
- AWS Secrets Manager (nivel enterprise)
- Mejores prácticas profesionales

---

### 🖥️ Conceptos de AWS
**[02_TEORIA_AWS_INSTANCIAS.md](02_TEORIA_AWS_INSTANCIAS.md)**
- ✅ ¿Qué es una instancia EC2?
- ✅ ¿Es lo mismo que una máquina virtual o VPS?
- ✅ Cómo funciona la virtualización
- ✅ Diferencias entre tu Mac y una instancia EC2
- ✅ Para qué sirve y cómo se cobra

**Temas cubiertos:**
- Servidores físicos vs máquinas virtuales
- Hypervisor y virtualización
- Tipos de instancias (t2.micro, t2.small, etc.)
- Regiones y datacenters de AWS
- SSH y archivos `.pem`
- Casos de uso prácticos

---

### 🚀 Despliegue Completo
**[03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md)**
- ✅ Guía paso a paso completa
- ✅ Desde código local hasta automatización en AWS
- ✅ Configuración de CRON para tareas programadas
- ✅ Monitoreo y logs
- ✅ Troubleshooting común

**Pasos cubiertos:**
1. Preparar proyecto local
2. Subir a GitHub (sin credenciales)
3. Configurar acceso SSH a EC2
4. Instalar dependencias en EC2
5. Configurar variables de entorno (.env)
6. Automatizar con CRON
7. Verificación y monitoreo
8. Mantenimiento

---

### 🔑 Configuración AWS
**[AWS_CONFIG.md](AWS_CONFIG.md)**
- ✅ Dónde poner tu archivo `.pem`
- ✅ Configuración de permisos
- ✅ Instrucciones de conexión SSH
- ✅ Verificación de seguridad

---

## 🗂️ Organización de Archivos del Proyecto

```
Pipeline_weather/
├── docs/                              ← 📚 TODA LA DOCUMENTACIÓN
│   ├── README.md                      ← Este archivo (índice maestro)
│   ├── 01_GESTION_CREDENCIALES_AWS.md ← Seguridad y variables de entorno
│   ├── 02_TEORIA_AWS_INSTANCIAS.md    ← Conceptos de AWS EC2
│   ├── 03_DESPLIEGUE_AWS_EC2.md       ← Deployment paso a paso
│   └── AWS_CONFIG.md                  ← Configuración de .pem y SSH
│
├── .ssh/                              ← 🔐 Claves SSH (protegido)
│   ├── README.md                      ← Instrucciones de uso
│   └── tu-archivo.pem                 ← Tu clave AWS
│
├── .env                               ← 🔑 Credenciales (protegido)
├── .env.example                       ← Plantilla para documentación
├── .gitignore                         ← Protege .env y .ssh/
│
├── twilio_config.py                   ← Gestión de credenciales
├── weather_sms.py                     ← Script ejecutable
├── twilio_messages.ipynb              ← Notebook de desarrollo
├── guia_json_requests.ipynb           ← Guía educativa JSON
│
└── README.md                          ← Documentación principal
```

---

## 🎓 Flujo de Aprendizaje Recomendado

### **Si eres principiante:**

1. **Empieza con:** [02_TEORIA_AWS_INSTANCIAS.md](02_TEORIA_AWS_INSTANCIAS.md)
   - Entender qué es una instancia EC2
   - Conceptos básicos de cloud

2. **Continúa con:** [01_GESTION_CREDENCIALES_AWS.md](01_GESTION_CREDENCIALES_AWS.md)
   - Cómo manejar credenciales de forma segura
   - Por qué usar `.env`

3. **Practica con:** [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md)
   - Paso a paso para desplegar tu proyecto
   - Automatización con CRON

### **Si tienes experiencia:**

Ve directo a: [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md)

---

## 🔍 Búsqueda Rápida de Temas

### ¿Cómo...?

**...manejar credenciales de forma segura?**
→ [01_GESTION_CREDENCIALES_AWS.md](01_GESTION_CREDENCIALES_AWS.md) - Sección "Solución Recomendada"

**...conectarme a mi instancia EC2?**
→ [AWS_CONFIG.md](AWS_CONFIG.md) - Sección "Conectar a AWS"

**...automatizar mi script diariamente?**
→ [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md) - Paso 6 "Automatizar con CRON"

**...evitar que mis credenciales se suban a Git?**
→ [01_GESTION_CREDENCIALES_AWS.md](01_GESTION_CREDENCIALES_AWS.md) - Sección "Mejores Prácticas"

**...entender qué es una máquina virtual?**
→ [02_TEORIA_AWS_INSTANCIAS.md](02_TEORIA_AWS_INSTANCIAS.md) - Sección "Conceptos Básicos"

---

## 📊 Comparación de Opciones

### Gestión de Credenciales

| Método | Seguridad | Facilidad | Persiste | Costo | Recomendado |
|--------|-----------|-----------|----------|-------|-------------|
| `.env` + dotenv | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ | $0 | ✅ **SÍ** |
| `export` en terminal | ⭐⭐⭐ | ⭐⭐⭐ | ❌ | $0 | ❌ |
| AWS Secrets Manager | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ | $0.40/mes | Para empresas |
| Hardcoded | ⭐ | ⭐⭐⭐⭐⭐ | ✅ | $0 | ❌ **NUNCA** |

---

## 🆘 Soporte y Troubleshooting

### Errores Comunes

**"No module named 'dotenv'"**
→ [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md) - Sección "Troubleshooting"

**"Permission denied" al conectar SSH**
→ [AWS_CONFIG.md](AWS_CONFIG.md) - Sección "Verificar Seguridad"

**CRON no ejecuta mi script**
→ [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md) - Paso 6.4 "Verificar CRON"

**Las variables de entorno no se cargan**
→ [01_GESTION_CREDENCIALES_AWS.md](01_GESTION_CREDENCIALES_AWS.md) - Sección "Troubleshooting"

---

## ✅ Checklist de Seguridad

Antes de subir tu código a GitHub:

- [ ] `.env` está en `.gitignore`
- [ ] `.ssh/` está en `.gitignore`
- [ ] `*.pem` está en `.gitignore`
- [ ] No hay credenciales hardcodeadas en el código
- [ ] El archivo `.env.example` solo tiene placeholders
- [ ] Ejecutaste `git status` para verificar qué se va a subir
- [ ] Los permisos de `.pem` son 400 (`chmod 400`)
- [ ] Los permisos de `.env` son 600 (`chmod 600`)

---

## 📖 Glosario

| Término | Definición | Documento |
|---------|------------|----------|
| **EC2** | Elastic Compute Cloud (servicio de AWS) | [02_TEORIA](02_TEORIA_AWS_INSTANCIAS.md) |
| **Instancia** | Máquina virtual en AWS | [02_TEORIA](02_TEORIA_AWS_INSTANCIAS.md) |
| **.env** | Archivo con variables de entorno | [01_GESTION](01_GESTION_CREDENCIALES_AWS.md) |
| **python-dotenv** | Librería para cargar .env | [01_GESTION](01_GESTION_CREDENCIALES_AWS.md) |
| **.pem** | Archivo de llave privada SSH | [AWS_CONFIG](AWS_CONFIG.md) |
| **SSH** | Secure Shell (conexión remota) | [02_TEORIA](02_TEORIA_AWS_INSTANCIAS.md) |
| **CRON** | Programador de tareas en Linux | [03_DESPLIEGUE](03_DESPLIEGUE_AWS_EC2.md) |
| **.gitignore** | Archivo que dice a Git qué ignorar | [01_GESTION](01_GESTION_CREDENCIALES_AWS.md) |

---

## 🎯 Objetivo del Proyecto

**Crear un sistema automatizado que:**
1. Consulta el clima de Madrid cada mañana
2. Detecta si va a llover
3. Te envía un SMS con la alerta
4. Todo sin intervención manual
5. Ejecutándose en AWS EC2 24/7

**Tecnologías usadas:**
- Python 3
- Twilio API (SMS)
- Weather API (pronóstico)
- AWS EC2 (servidor)
- CRON (automatización)
- Git/GitHub (control de versiones)

---

## 📝 Notas Finales

### Archivos que SÍ se suben a Git:
- ✅ `twilio_config.py` (sin credenciales)
- ✅ `weather_sms.py`
- ✅ `.gitignore`
- ✅ `.env.example`
- ✅ `README.md`
- ✅ Toda la carpeta `docs/`

### Archivos que NO se suben a Git:
- ❌ `.env` (protegido por .gitignore)
- ❌ `.ssh/` (protegido por .gitignore)
- ❌ `*.pem` (protegido por .gitignore)
- ❌ `.venv/` (protegido por .gitignore)
- ❌ `__pycache__/` (protegido por .gitignore)

---

## 🚀 Próximos Pasos

1. Lee la documentación en orden
2. Sigue [03_DESPLIEGUE_AWS_EC2.md](03_DESPLIEGUE_AWS_EC2.md)
3. Configura tu instancia EC2
4. Automatiza con CRON
5. ¡Disfruta de tus alertas automáticas!

---

**¿Preguntas? Revisa la sección de Troubleshooting en cada guía.** 📚
