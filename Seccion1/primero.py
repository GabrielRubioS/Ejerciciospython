"""
programa que lee la edad y muestra cuantos 
años tendra el usuario dentro de tantos años 
como el usuario indique 
números
Autor: Gabriel Rubio
Fecha: 20 / octubre / 2023

"""

edad=int(input("Ingrese la edad: "))
añospasados = int(input("Ingrese años a Transcurrir: "))
total = edad + añospasados

print ("Dentro de " + str(añospasados)+ " años tendras " + str(total) + " años")