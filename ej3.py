import os
import json
from datetime import datetime
from persona import Persona
from genetica import generar_combinaciones, calcular_probabilidades
from graficos import graficar_porcentajes

# Carpetas de flujo
PENDING_DIR = "data/pending"
DONE_DIR = "data/done"
RESULTS_DIR = "data/results"
LOG_FILE = "logs/analisis.log"

# Crear carpetas si no existen
for carpeta in [PENDING_DIR, DONE_DIR, RESULTS_DIR, os.path.dirname(LOG_FILE)]:
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def registrar_log(mensaje):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {mensaje}\n")
    print(mensaje)

def procesar_archivo(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            registrar_log(f"Error leyendo JSON {filepath}: {e}")
            return

    resultados_archivo = []

    for i, caso in enumerate(data.get("parents", []), start=1):
        padre_data = caso.get("father", {})
        madre_data = caso.get("mother", {})

        # Asignar nombres temporales si no existen
        padre_nombre = padre_data.get("name") or f"Padre_{i}"
        madre_nombre = madre_data.get("name") or f"Madre_{i}"

        try:
            padre = Persona(nombre=padre_nombre, grupo=padre_data.get("gs"))
            madre = Persona(nombre=madre_nombre, grupo=madre_data.get("gs"))
        except Exception as e:
            registrar_log(f"[Caso {i}] Error creando personas: {e}")
            continue

        porcentajes = calcular_probabilidades(padre, madre)
        resultados_archivo.append({
            "father": {"name": padre.nombre, "gs": padre.grupo_sanguineo},
            "mother": {"name": madre.nombre, "gs": madre.grupo_sanguineo},
            "probabilities": porcentajes
        })

        # Generar gráfico
        try:
            titulo = f"Probabilidades hijo: {padre.nombre} x {madre.nombre}"
            graficar_porcentajes(porcentajes, titulo=titulo)
        except Exception as e:
            registrar_log(f"[Caso {i}] Error generando gráfico: {e}")

    # Guardar resultados en JSON
    resultado_filename = os.path.join(
        RESULTS_DIR,
        f"result_{os.path.basename(filepath)}"
    )
    with open(resultado_filename, "w", encoding="utf-8") as f_out:
        json.dump({
            "date": str(datetime.now()),
            "file_processed": os.path.basename(filepath),
            "results": resultados_archivo
        }, f_out, indent=4)

    # Mover archivo procesado a done
    done_filepath = os.path.join(DONE_DIR, os.path.basename(filepath))
    os.replace(filepath, done_filepath)

    registrar_log(f"Archivo procesado correctamente: {filepath}")

def main():
    archivos = [f for f in os.listdir(PENDING_DIR) if f.endswith(".json")]
    if not archivos:
        registrar_log("No hay archivos pendientes en 'data/pending/'")
        return

    for archivo in archivos:
        filepath = os.path.join(PENDING_DIR, archivo)
        procesar_archivo(filepath)

if __name__ == "__main__":
    main()
