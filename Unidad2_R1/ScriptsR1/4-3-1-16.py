"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""
from collections import defaultdict

def generar_histograma(archivo):
    recuento_letras = defaultdict(int)

    try:
        with open(archivo, 'r') as file:
            contenido = file.read()

        for caracter in contenido:
            if caracter.isalpha():
                letra = caracter.lower()
                recuento_letras[letra] += 1

        ordenado = sorted(recuento_letras.items(), key=lambda x: x[1], reverse=True)

        for letra, recuento in ordenado:
            print(f"{letra} -> {recuento}")

        nombre_archivo_salida = archivo.split('.')[0] + '.hist'
        with open(nombre_archivo_salida, 'w') as output_file:
            for letra, recuento in ordenado:
                output_file.write(f"{letra} -> {recuento}\n")

        print(f"Histograma guardado en {nombre_archivo_salida}")

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print("Error: {e}")
