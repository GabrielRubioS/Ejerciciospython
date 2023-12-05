"""
Aplicacion que toma el valor 
de un producto e imprima su precio final si este tiene 
siempre un descunto del 10% 
números
Autor: Gabriel Rubio
Fecha: 17 / octubre / 2023

"""
#Solicitamos el valor 
val_produc = float(input("Ingrese el valor del producto: "))

#calculamos el precio final y agregamos la variable del descuento 
descuento = 0.10  
precio_final = val_produc * (1 - descuento)

# Imprimir el precio final al consumidor
print(f"El precio final con un descuento del 10% es: {precio_final}")