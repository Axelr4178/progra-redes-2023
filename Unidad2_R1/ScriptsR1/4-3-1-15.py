"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""

from os import strerror

filname = input("¿Cuál es el nombre del archivo?: ")

try:
    file = open(filname, 'r')
except IOError as e:
    print("No se pudo abrir :", strerror(e.errno))
    exit()

store = {}
count = 0

read = file.read()
for char in read:
    if char.isalpha() == True:
        if char not in store.keys():
            count = 1
            store.update({char.lower():count})
        else
            count += 1
            store.update({char.lower():count})

clean_name = filname.split(".")[0]
output = open(clean_name + "hist", 'w+t')