"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""
import os


def find(path, dir):
    # Comprueba si el directorio dado existe
    if not os.path.exists(path):
        print("El directorio dado no existe.")
        return

    # Itera sobre todos los directorios en la ruta dada
    for root, dirs, files in os.walk(path):
        # Comprueba si el nombre del directorio coincide con el nombre dado
        if dir in dirs:
            # Imprime la ruta absoluta del directorio
            print(os.path.join(root, dir))


# Prueba la función
path = "./tree"
dir = "python"

# Llama a la función find()
find(path, dir)


