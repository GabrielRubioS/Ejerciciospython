"""
Cree un programa que pida un numero (n) y 
calcule su factorial (!)
"""

numero= int(input("Ingrese un numero Entero: "))
factorial=1
if numero!=0:
    for i in range(1,numero+1):
        factorial=factorial*i
        print(f"{i} * ", end="")
print("= ", factorial)
if numero<0:
    print("No se puede calcular el factorial de un numero negativo")

