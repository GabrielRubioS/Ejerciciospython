"""
Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se
introduzca el cero.
"""
num = 0
suma = 0
contador = 0
while num != 0:
  num = float(input("Ingrese el numero "))
  suma += num
  contador += 1
  promedio = suma / contador
  print("El promedio de los numeros ingresados es: ", promedio)


