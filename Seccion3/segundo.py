"""
Cree un programa que lea la edad de un usuario e imprima un mensaje 
que diga si el usuario es mayor de edad o no.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""

print("productos: lentejas - arroz - crema - vino")
producto = input("Ingrese el producto: ")
if producto == "lentejas" or producto == "arroz" or producto == "crema" or producto == "vino":
    if producto == "lentejas" or producto == "arroz":
         print("No paga IVA")
    else: 
        print("Paga IVA")