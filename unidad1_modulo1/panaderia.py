
pan = (3.49)
pandesc = (3.49*60)/100

print("Escribe la canitdad de barras vendidas que no son de día")
cantpan = int(input())

print ("Precio habitual por cada barra: $",pan)
print ("Descuento por cada barra que no se fresca: $",pandesc)
print ("Coste final total: ", (cantpan * pan)*60/100)