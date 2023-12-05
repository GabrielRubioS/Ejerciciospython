"""
Cree un programa que reciba tres números y muestre el mayor.
En caso de que los números sean iguales
también se debe mostrar al usuario.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1>n2 and n1>n3:
    print(str(n1)+" Es mayor")
elif n2>n1 and n2>n3:
    print(str(n2)+" Es mayor")
elif n3>n2 and n3>n1:
    print(str(n3)+" Es mayor")
else:
    print("Los tres son iguales")