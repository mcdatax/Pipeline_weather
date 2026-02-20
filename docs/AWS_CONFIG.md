# 🔐 Configuración AWS - Guía Rápida

## ✅ YA ESTÁ TODO CONFIGURADO

He creado la carpeta `.ssh/` en tu proyecto y actualizado `.gitignore` para protegerla.

---

## 📋 PASOS SIGUIENTES (SIMPLE)

### **1. Copia tu archivo `.pem` a la carpeta `.ssh/`**

```bash
# Opción 1: Arrastrarlo con Finder
# - Abre Finder
# - Ve a tu carpeta Pipeline_weather/.ssh/
# - Arrastra tu archivo .pem ahí

# Opción 2: Desde terminal
cp ~/Downloads/tu-archivo.pem /Users/mane/Documents/Pipeline_weather/.ssh/
```

### **2. Ajusta los permisos (OBLIGATORIO)**

```bash
cd /Users/mane/Documents/Pipeline_weather
chmod 400 .ssh/tu-archivo.pem
```

**¿Qué hace `chmod 400`?**
- Solo TÚ puedes leer el archivo
- Nadie más puede ver ni modificar
- SSH lo requiere por seguridad

### **3. Conectar a AWS**

```bash
ssh -i .ssh/tu-archivo.pem ubuntu@tu-ip-ec2
```

Reemplaza:
- `tu-archivo.pem` → Nombre real de tu archivo
- `ubuntu` → Usuario de tu instancia (puede ser `ec2-user`)
- `tu-ip-ec2` → IP pública de tu instancia EC2

---

## 📁 Cómo Quedará tu Proyecto

```
Pipeline_weather/
├── .ssh/                      ← Carpeta PROTEGIDA (no se sube a Git)
│   ├── README.md              
│   └── mi-instancia.pem       ← TU ARCHIVO .pem AQUÍ
│
├── .env                       ← Credenciales Twilio (protegido)
├── .gitignore                 ← Protege .ssh/ y .env ✅
├── twilio_config.py
└── twilio_messages.ipynb
```

---

## 🔒 Seguridad Verificada

He actualizado `.gitignore` con:
```
.ssh/
*.pem
*.key
```

Esto significa:
- ✅ Git **NUNCA** subirá archivos de la carpeta `.ssh/`
- ✅ Git **NUNCA** subirá archivos `.pem` o `.key`
- ✅ Igual que con `.env`, tus claves están protegidas

---

## 🧪 Verificar Seguridad

```bash
# Ver qué archivos Git ignora
git status --ignored

# Deberías ver .ssh/ en la lista
```

---

## 🆘 Si tienes problemas:

### Error: "Permission denied (publickey)"
```bash
# Verifica permisos
ls -la .ssh/tu-archivo.pem

# Debe mostrar: -r-------- (solo lectura para ti)
# Si no, ejecuta:
chmod 400 .ssh/tu-archivo.pem
```

### Error: "Bad permissions"
```bash
# Mismo problema, ajusta permisos:
chmod 400 .ssh/tu-archivo.pem
```

---

## 💡 Resumen (3 pasos)

1. **Copia** tu `.pem` a la carpeta `.ssh/`
2. **Ajusta permisos:** `chmod 400 .ssh/tu-archivo.pem`
3. **Conéctate:** `ssh -i .ssh/tu-archivo.pem ubuntu@ip`

¡Listo! Simple y seguro 🎯
