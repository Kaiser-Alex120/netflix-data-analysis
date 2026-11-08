# Netflix Data Analysis

Análisis exploratorio de datos (EDA) del catálogo de Netflix: limpieza de datos, 
visualizaciones e insights sobre contenido, países, géneros y tendencias.

## Dataset
Fuente: [Netflix Movies and TV Shows - Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
8,807 títulos con información de tipo, director, cast, país, fecha agregada, 
clasificación, duración y géneros.

## Estructura del proyecto
├── data/
│   ├── raw/            # Dataset original sin modificar
│   └── processed/       # Dataset limpio + tablas resumen
├── notebooks/            # Análisis exploratorio (EDA)
├── src/transformation/   # Script de limpieza de datos
├── outputs/              # Gráficos generados
└── requirements.txt

## Insights principales

### Movies vs TV Shows
[descripción breve + imagen]

### Top países productores de contenido
[descripción breve + imagen]

### Crecimiento del catálogo por año
[descripción breve + imagen]

### Géneros más comunes
[descripción breve + imagen]

## Cómo correrlo
```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/transformation/cleaner.py
