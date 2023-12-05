"""
Cree un programa que calcula la suma de los primeros n números naturales.
"""

numero=int(input("Ingrese un numero natural: "))
suma=0
for i in range (1,numero+1):
    suma+=i
    print(i, " + ",end="")
print(" = " + str(suma))
