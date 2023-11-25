"""
    Autor:Axel Alejandro Almaguer Rodriguez
    Descripcion: Problemas Python Institute
"""

from datetime import datetime

dt = datetime(2020,11,4,14,53,0)

print(dt)
print(dt.strftime('%y/%B/%d %H:%M:%S %p'))
print(dt.strftime('%a, %Y %b %d'))
print(dt.strftime('%A, %Y %B %d'))
print('Weekday: ' + str(dt.weekday() + 1))
print('Day of the year: ' + dt.strftime('%j'))
print('Week number of the year: ' + dt.strftime('%W'))