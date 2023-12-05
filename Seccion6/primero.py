"""
Cree un programa que muestre los números naturales de 1 a n.

"""

numero=int(input("Ingrese un numero natural (Positivo): "))
for i in range (numero+1):
    print(i," - ", end="")
if numero<0:
    print ("⚠ El numero elegido NO es un numero natural ⚠")