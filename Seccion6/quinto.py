"""
 Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el
programa se detendrá, de lo contrario continuará ejecutándose.

"""

bandera = input("Ingrese s/n")
while(bandera != "s"):
    bandera = input("Ingrese s/n")
    print ("gracias por tu tiempo")