print("---promedio de notas para n estudiantes---")
n = int(input("Ingrese el numero de estudiantes: "))
for i in range (n):
    nota1=float(input("Ingrese la primer nota: "))
    nota2=float(input("Ingrese la segunda nota: "))
    nota3=float(input("Ingrese la tercer nota: "))
    promedio= (nota1+nota2+nota3) / 3
    print("Estudiante registrado: ", str(i+1))
    print ("Las notas son: " + str(nota1) + " | " + str(nota2) + " | "+ str(nota3))
    print("El promedio es: " + str(promedio))
    print("Presione enter para pasar al siguiente estudiante")
    input()
    
