"""
Cree un programa que calcule el promedio de 10 números
"""
suma=0
for i in range (1,10+1):
    num = float(input("Ingrese el numero "+str(i)+": "))
    suma += num
    promedio = suma/10
print ("El promedio de los numeros ingresados es: ",promedio)