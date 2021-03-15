import sys

archivo = open("facpython.txt","a")
print ("¿Que desea hacer?")
print ("1. Calcular el factorial de un numero")
print ("2. Salir")
def fact():
    inicio = 1
    valor = int(input("Digite un numero: "))
    
    for i in range(1,valor + 1):
        inicio *= i
    print ("El factorial de este numero es: ",inicio)
    dato = str(valor)
    resul = str(inicio)
    archivo.write("El factorial de " + dato + " es: " + resul)
    archivo.write("\n")
    

def salir():
    print("Hasta pronto.")
    archivo.close()
    sys.exit()
    

try:
    a = int(input("Escoja una opcion del menu: "))  
    while (a<=2):
        op = [fact,salir]
        op[a-1]()
        a = int(input("Escoja una opcion del menu: "))  
except(ValueError):
    print("Hubo un error")