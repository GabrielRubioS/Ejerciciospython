"""
Cree un programa que lea un número y muestre si éste
es divisible entre cinco o no.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""

n1 = int(input("Ingrese el numero: "))
if n1 % 5 == 0:
    print(str(n1)+" Es divisible por 5")
else:
    print(str(n1)+" No es divisile por 5")