# Autor:Axel Alejandro Almaguer Rodriguez
# Programacion de Redes
# Listas y Tuplas

from turtle import end_fill


mylist = int(input(1,2,3,4,5))
datos = mylist

tuplaDatos = (1,2,3,4,5)
print (tuplaDatos)

def mostrar_contenido(tuplaDatos):
    for datos in tuplaDatos:
        print(datos)

mostrar_contenido(tuplaDatos)

longitud_tupla = len(tuplaDatos)
print("La longitud de la tupla es: ", longitud_tupla)

def sumar_tupla(tuplaDatos):
    suma = sum(tuplaDatos)
    return suma

resultado_suma = sumar_tupla(tuplaDatos)
print("La suma de los elementos de la tupla es: ",resultado_suma)

mostrar_contenido(tuplaDatos)
suma= sum(tuplaDatos(end_fill +end_fill))
print(longitud_tupla)
