"""
Cree un programa que tome el radio de un 
círculo e imprima su área y perímetro.
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023

"""
pi=3.1416
radio = float(input("Ingrese el radio del circulo: "))
area = pi * radio * radio
perimetro = 2 * pi * radio

print("El area del circulo es: " + str(area))
print("El Perimetro del circulo es : " + str(perimetro))
