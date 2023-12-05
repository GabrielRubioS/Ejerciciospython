"""
Cree un programa que lea los tres ángulos internos de un 
triángulo y muestre si los ángulos corresponden a un
triángulo o no.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""

a = int(input("Ingrese el primer angulo: "))
b = int(input("Ingrese el segundo angulo: "))
c = int(input("Ingrese el tercer angulo: "))
triangulo= a + b + c
if triangulo == 180:
    print("El angulo corresponde al de un triangulo")
else:
    print("El angulo no corresponde al de un triangulo")
