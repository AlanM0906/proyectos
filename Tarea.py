import sys
print ("CALCULADORA")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Salir")
print ("")
def suma():
    print ("*****SUMA*****")
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))
    resul = num1 + num2
    print("El resultado de la suma es: ", resul)
    print ("")
def resta():
    print ("*****RESTA*****")
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))
    resul = num1 - num2
    print("El resultado de la resta es: ", resul)
    print ("")
def multi():
    print ("*****MULTIPLICACION*****")
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))
    resul = num1 * num2
    print("El resultado de la multiplicacion es: ", resul)
    print ("")
def div():
    print ("*****DIVISION*****")
    num1 = int(input("Digite el primer numero: "))
    num2 = int(input("Digite el segundo numero: "))
    if (num2 != 0):
        resul = num1 // num2
        print("El resultado de la division es: ", resul)
        print ("")        
    else:
        print("La division entre 0 no esta definida, escoja otro numero.")        
def salir():
    print("Gracias por utilizar nuestra aplicacion, hasta pronto.")
    sys.exit()
try:
    a = int(input("Escoja una opcion del menu: "))  
    while (a<=5):
        operaciones = [suma,resta,multi,div,salir]
        operaciones[a-1]()
        print ("CALCULADORA")
        print ("1. Suma")
        print ("2. Resta")
        print ("3. Multiplicacion")
        print ("4. Division")
        print ("5. Salir")
        print ("")
        a = int(input("Escoja una opcion del menu: "))  
except (ValueError):
    print("A ocurrido un error, vuelva a intentarlo.")




    