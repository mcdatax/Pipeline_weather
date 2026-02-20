<div align="center">

# 🌤️ Pipeline Weather

### Pipeline automatizado de datos meteorológicos
*Extracción, transformación y análisis de datos climáticos en tiempo real*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/mcdatax/Pipeline_weather)

[Características](#-características) •
[Tecnologías](#️-tecnologías) •
[Instalación](#-instalación) •
[Uso](#-uso) •
[Arquitectura](#-arquitectura)

</div>

---

## 📋 Descripción

**Pipeline Weather** es un sistema ETL (Extract, Transform, Load) automatizado para la recolección, procesamiento y análisis de datos meteorológicos en tiempo real. El proyecto extrae información de APIs públicas de clima, procesa los datos y los almacena de forma estructurada para análisis posteriores y visualización.

### 🎯 Objetivo

Proporcionar una solución completa y escalable para:
- **Extracción** automatizada de datos meteorológicos de múltiples fuentes
- **Transformación** y limpieza de datos en formatos consistentes
- **Almacenamiento** eficiente en bases de datos para análisis históricos
- **Visualización** de tendencias y patrones climáticos

---

## ✨ Características

- 🔄 **Pipeline ETL Automatizado**: Extracción programada de datos cada hora
- 🌍 **Multi-ubicación**: Recolección de datos de múltiples ciudades simultáneamente
- 📊 **Transformación de Datos**: Limpieza, validación y estandarización
- 💾 **Almacenamiento Persistente**: Base de datos relacional optimizada
- 📈 **Visualización**: Dashboards interactivos con métricas clave
- ⚡ **Procesamiento en Tiempo Real**: Actualizaciones continuas
- 🔔 **Alertas**: Notificaciones ante condiciones climáticas extremas
- 📝 **Logging Completo**: Trazabilidad de todas las operaciones

---

## 🛠️ Tecnologías

<div align="center">

| Categoría | Tecnologías |
|-----------|-------------|
| **Lenguaje** | Python 3.8+ |
| **Orquestación** | Apache Airflow / Prefect |
| **APIs** | OpenWeatherMap API, WeatherAPI |
| **Base de Datos** | PostgreSQL / MySQL |
| **Procesamiento** | Pandas, NumPy |
| **Visualización** | Matplotlib, Plotly, Grafana |
| **Contenedores** | Docker, Docker Compose |
| **Control de Versiones** | Git, GitHub |

</div>

---

## 📁 Estructura del Proyecto

```
Pipeline_weather/
│
├── dags/                       # DAGs de Airflow
│   ├── weather_etl_dag.py     # Pipeline principal
│   └── config/                # Configuraciones
│
├── src/                       # Código fuente
│   ├── extract/              # Módulos de extracción
│   │   ├── api_client.py     # Cliente API
│   │   └── data_fetcher.py   # Extractor de datos
│   │
│   ├── transform/            # Módulos de transformación
│   │   ├── cleaner.py        # Limpieza de datos
│   │   └── validator.py      # Validación
│   │
│   └── load/                 # Módulos de carga
│       ├── db_loader.py      # Carga a DB
│       └── storage.py        # Almacenamiento
│
├── database/                  # Scripts de base de datos
│   ├── schema.sql            # Esquema de tablas
│   └── migrations/           # Migraciones
│
├── notebooks/                 # Jupyter notebooks
│   └── analysis.ipynb        # Análisis exploratorio
│
├── tests/                     # Tests unitarios
│   └── test_pipeline.py
│
├── config/                    # Configuraciones
│   ├── config.yaml           # Configuración general
│   └── cities.json           # Ciudades a monitorear
│
├── docker-compose.yml         # Orquestación Docker
├── requirements.txt           # Dependencias Python
├── .env.example              # Variables de entorno
└── README.md                 # Este archivo
```

---

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- Docker y Docker Compose
- API Key de OpenWeatherMap (gratuita)
- PostgreSQL 13+ (o usar Docker)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/mcdatax/Pipeline_weather.git
cd Pipeline_weather
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

5. **Configurar base de datos**
```bash
# Si usas Docker
docker-compose up -d postgres

# Ejecutar migraciones
python database/init_db.py
```

6. **Iniciar el pipeline**
```bash
# Con Docker
docker-compose up -d

# O manualmente
airflow db init
airflow webserver -p 8080
airflow scheduler
```

---

## 💻 Uso

### Configuración Básica

1. **Obtener API Key**
   - Regístrate en [OpenWeatherMap](https://openweathermap.org/api)
   - Copia tu API key al archivo `.env`

2. **Configurar ciudades**
   - Edita `config/cities.json` con las ubicaciones deseadas:
   ```json
   {
     "cities": [
       {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
       {"name": "Barcelona", "lat": 41.3851, "lon": 2.1734}
     ]
   }
   ```

3. **Ejecutar el pipeline**
```bash
# Ejecución manual
python src/main.py

# Con Airflow (automático)
# Accede a http://localhost:8080 y activa el DAG
```

### Consultas a la Base de Datos

```sql
-- Ver últimas lecturas
SELECT * FROM weather_data 
ORDER BY timestamp DESC 
LIMIT 10;

-- Temperatura promedio por ciudad
SELECT city, AVG(temperature) as avg_temp
FROM weather_data
WHERE timestamp > NOW() - INTERVAL '24 HOURS'
GROUP BY city;
```

---

## 🏗️ Arquitectura

```
┌─────────────────┐
│   APIs Clima    │
│  (OpenWeather)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Extracción    │
│  (API Client)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Transformación │
│ (Limpieza/Val.) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│      Carga      │
│   (PostgreSQL)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Visualización  │
│   (Dashboard)   │
└─────────────────┘
```

### Flujo del Pipeline

1. **Extracción**: Consulta APIs cada hora para obtener datos actuales
2. **Validación**: Verifica integridad y calidad de datos
3. **Transformación**: Normaliza unidades y formatos
4. **Carga**: Almacena en PostgreSQL con timestamps
5. **Análisis**: Genera métricas y alertas automáticas

---

## 📊 Datos Recolectados

El pipeline extrae las siguientes métricas:

| Métrica | Descripción | Unidad |
|---------|-------------|--------|
| Temperatura | Temperatura actual | °C |
| Sensación Térmica | Temperatura percibida | °C |
| Humedad | Humedad relativa | % |
| Presión | Presión atmosférica | hPa |
| Velocidad del Viento | Velocidad del viento | m/s |
| Dirección del Viento | Dirección en grados | ° |
| Nubosidad | Cobertura de nubes | % |
| Precipitación | Lluvia en última hora | mm |
| Visibilidad | Distancia de visibilidad | metros |
| Índice UV | Radiación ultravioleta | 0-11+ |

---

## 🔍 Ejemplos de Análisis

### Análisis de Temperatura

```python
import pandas as pd
from src.analytics import WeatherAnalyzer

# Cargar datos
analyzer = WeatherAnalyzer()
df = analyzer.load_data(city='Madrid', days=30)

# Calcular estadísticas
stats = analyzer.temperature_stats(df)
print(f"Temp. Media: {stats['mean']:.1f}°C")
print(f"Temp. Máxima: {stats['max']:.1f}°C")
print(f"Temp. Mínima: {stats['min']:.1f}°C")

# Generar gráfico
analyzer.plot_temperature_trend(df, save_path='temp_trend.png')
```

### Dashboard en Tiempo Real

Accede al dashboard en `http://localhost:3000` para visualizar:
- Temperatura actual en múltiples ciudades
- Gráficos de tendencias históricas
- Alertas de condiciones extremas
- Comparativas entre ubicaciones

---

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest tests/

# Con cobertura
pytest --cov=src tests/

# Tests específicos
pytest tests/test_extract.py -v
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. Commit tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)
5. Abre un Pull Request

---

## 📝 To-Do

- [ ] Integrar más APIs de clima (WeatherAPI, Visual Crossing)
- [ ] Implementar predicciones con Machine Learning
- [ ] Añadir soporte para datos históricos (años anteriores)
- [ ] Crear API REST para consultas
- [ ] Implementar sistema de cache con Redis
- [ ] Añadir tests de integración
- [ ] Dockerizar completamente el proyecto
- [ ] Crear documentación interactiva con Sphinx

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

- [OpenWeatherMap](https://openweathermap.org/) por proporcionar la API gratuita
- Apache Airflow por la orquestación de pipelines
- La comunidad de Python por las increíbles bibliotecas

---

<div align="center">

**⭐ Si este proyecto te resulta útil, considera darle una estrella ⭐**

[Reportar Bug](https://github.com/mcdatax/Pipeline_weather/issues) •
[Solicitar Feature](https://github.com/mcdatax/Pipeline_weather/issues) •
[Contribuir](https://github.com/mcdatax/Pipeline_weather/pulls)

</div>