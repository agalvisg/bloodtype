# Calculadora de Probabilidades de Grupos Sanguíneos 

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Matplotlib](https://img.shields.io/badge/Matplotlib-required-orange.svg)

---

## Descripción

Este proyecto calcula los posibles grupos sanguíneos de un descendiente a partir del grupo sanguíneo de los padres.  
Incluye:

- Cálculo de probabilidades de grupos sanguíneos según herencia Mendeliana.
- Representación de resultados en **porcentajes** y en **gráficos circulares tipo pie**.
- Lectura de archivos JSON con registros de padres.
- Gestión de carpetas para archivos pendientes, procesados y resultados.
- Control de errores y normalización de datos.

---

## Estructura de Carpetas
data/
├─ pending/ # Archivos JSON pendientes de procesar
├─ done/ # Archivos JSON procesados
├─ results/ # Resultados generados en formato JSON
logs/
└─ analisis.log # Registro de errores durante la ejecución

---

## Requisitos

- Python 3.10 o superior  
- `matplotlib`  

Instalación rápida:

```bash
pip install matplotlib

{
  "parents": [
    {
      "father": {"gs": "A", "rh": "+"},
      "mother": {"gs": "B", "rh": "-"}
    },
    {
      "father": {"gs": "O", "rh": "+"},
      "mother": {"gs": "AB", "rh": "+"}
    }
  ]
}

gs → Grupo sanguíneo (A, B, AB, O)

rh → Factor Rh (+ o -)
