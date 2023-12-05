"""
Aplicacion que toma el precio de un producto 
e imprima su precio final al consumidor 
con un iva del 19%
números
Autor: Gabriel Rubio
Fecha: 17 / octubre / 2023

"""
#Aqui le pediremos el precio de un producto al usuario 
Nombre_producto = input("Ingrese el nombre del producto: ")
valor_produc = float(input("Ingrese el precio del producto: "))

#Aqui definimos una variable que lleve el iva y otra variable que tenga el resultado de la operación
iva = 0.19 
precio_final = valor_produc * (1 + iva)

#Imprimimos el precio final que es el que se mostrara al usuario 
print(f"Nombre del producto: {Nombre_producto}" ) 
print(f"Valor del producto: {valor_produc}" ) 
print(f"El iva es de: {iva}" ) 
print(f"el precio final es: {precio_final}" ) 