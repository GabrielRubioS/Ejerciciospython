"""
programa que lee el monto de un prestamo y el plazo en meses
y muestre al usuario el valor de las cuotas mensuales
pagando un interes fijo del 2.7% mensual
Autor: Gabriel Rubio
Fecha: 20 / octubre / 2023
"""


montoprestamo = int(input("Ingrese el monto del prestamo: "))
plazomeses = int(input("ingrese el plazo en meses: "))
interes = 0.27
valor_mensual = montoprestamo / plazomeses
cuota_mensual = (valor_mensual * interes) + valor_mensual
print ("La cuota mensual es de " + str(cuota_mensual))

