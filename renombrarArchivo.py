# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:42:18 2024

@author: GCopes
"""
import os
import re
from datetime import datetime

def cambiar_nombres_con_formato(ruta_carpeta):
    try:
        # Listar todos los archivos en la carpeta
        archivos_en_carpeta = os.listdir(ruta_carpeta)
        
        # Iterar sobre cada archivo
        for archivo_actual in archivos_en_carpeta:
            # Verificar si el archivo sigue el formato esperado
            if re.match(r".*-\d{4}-\d{2}-\d{2}\.csv", archivo_actual):
                print(f"Se encontró un archivo con el nombre: {archivo_actual}")
                
                # Extraer la fecha del archivo utilizando una expresión regular
                fecha_match = re.search(r"\d{4}-\d{2}-\d{2}", archivo_actual)
                if fecha_match:
                    fecha_str = fecha_match.group()
                    print(f"Fecha extraída del nombre del archivo: {fecha_str}")
                    
                    fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
                    # Construir el nuevo nombre con el formato especificado
                    nuevo_nombre = f"TEI_MBI_{fecha.strftime('%Y%m%d')}.csv"
                    # Construir la ruta completa al archivo actual y al nuevo archivo
                    ruta_actual = os.path.join(ruta_carpeta, archivo_actual)
                    nuevo_ruta_completa = os.path.join(ruta_carpeta, nuevo_nombre)
                    # Renombrar el archivo
                    os.rename(ruta_actual, nuevo_ruta_completa)
                    print(f"¡El archivo '{archivo_actual}' se ha renombrado a '{nuevo_nombre}'!")
    except PermissionError:
        print("No tienes permiso para renombrar algunos archivos.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

# Ejemplo de uso
ruta_carpeta = r"C:\Users\GCopes\Desktop\Marambio\Ozono Superficial\QLI-2012"

cambiar_nombres_con_formato(ruta_carpeta)
