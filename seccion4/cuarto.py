"""
Cree un programa que lea un número entre
1 y 15 y muestre si éste es primo o no
Autor: Gabriel Rubio S
Fecha: 3 / Noviembre / 2023s

"""
primo2=2
primo3=3
primo5=5
primo7=7
primo11=11
primo13=13
print("Elija un numero del 1 al 15")
n1 = int(input("Ingrese el numero: "))
if n1>15 or n1<1:
    print("¡ERROR! - elije un numero correcto")
elif n1==primo2 or n1==primo3 or n1==primo5 or n1==primo7 or n1==primo11 or n1==primo13:
    print(str(n1)+" Es Primo")
else:
    print(str(n1)+" No es primo")
    