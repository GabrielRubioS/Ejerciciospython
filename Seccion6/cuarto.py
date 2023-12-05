"""
Cree un programa que muestre los números impares entre 1 y n
"""

numero=int(input("Ingrese un numero: "))
print("Los numeros impares son: ")
for i in range (1,numero+1): 
    if i % 2==1:   
        print(i)
     