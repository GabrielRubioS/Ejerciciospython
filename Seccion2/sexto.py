"""
Aplicacion que toma el valor 
de un producto e imprima su precio final si este tiene 
siempre un descunto del 10% 
números
Autor: Gabriel Rubio
Fecha: 17 / octubre / 2023

"""


cantidad = float(input("Ingrese la cantidad: "))
porcentaje = float(input("Ingrese el porcentaje a calcular: "))
porcentaje_d = porcentaje / 100
porcentaje_finnal = cantidad * porcentaje_d
print("El porcentaje calculado es:", porcentaje_finnal)
