"""
Cree un programa que lea dos números y 
muestre su producto, su cociente, su módulo, su suma y su resta.
Autor: Gabriel Rubio 
Fecha: 6 / octubre / 2023

"""
#pedimos los numeros a sumar 
numero1 = float (input("Imgrese el primer numero: "))
numero2 = float (input("Ingrese el segundo numero: "))
suma = numero1 + numero2

producto = numero1 * numero2

cociente = numero1 / numero2

modulo = numero1 % numero2

suma = numero1 + numero2

resta = numero1 - numero2

# Imprimimos los resultados
print("El producto (*) de los números es:", producto)
print("El cociente (/) de los números es:", cociente)
print("El módulo (%) de los números es:", modulo)
print("La suma (+) de los números es:", suma)
print("La resta (-) de los números es:", resta)
print ("La suma (+) es: " + str(suma))