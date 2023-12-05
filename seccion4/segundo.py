"""
Cree un programa que lea un número y muestre si éste es par o impar.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""

n1 = int(input("Ingrese el numero: "))

if n1 % 2 == 0:
    print(str(n1)+" Es par")
else:
    print(str(n1)+" Es impar")