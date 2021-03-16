import math
import sys
archivo = open("salida.txt","a")
def progra1():
    print ("Digite 3 numeros enteros por favor")
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    num3 = float(input("Numero 3: "))

    if (num1 > num2 and num1 > num3 and num2 != num3):
        suma = num1 + num2 + num3
        print("La suma de los tres valores es: ",suma)
        print("")
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        sumas = str(suma)
        archivo.write("La suma de los tres valores es: " + sumas)
        archivo.write("\n")

    elif(num2 > num1 and num2 > num3 and num1 != num3):
        multi = num1 * num2 * num3
        print("La multiplicacion de los tres valores es: ", multi)
        print("")
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        multipli = str(multi)
        archivo.write("La multiplicacion de los tres valores es: " + multipli)
        archivo.write("\n")

    elif(num3 > num1 and num3 > num2 and num1 != num2):
        print ("", num1, ",",num2,",",num3)
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")

    elif(num1 == num2 and num1 != num3):
        print("El valor diferente es: ", num3)
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        archivo.write("El valor diferente es:"+numero3)
        archivo.write("\n")

    elif(num2 == num3 and num2 != num1):
        print("El valor diferente es: ", num1)
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        archivo.write("El valor diferente es:"+numero1)
        archivo.write("\n")

    elif(num1 == num3 and num1 != num2):
        print("El valor diferente es: ", num2)
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        archivo.write("El valor diferente es:"+numero2)
        archivo.write("\n")

    else:
        print ("", num1, ",",num2,",",num3)
        numero1 = str(num1)
        numero2 = str(num2)
        numero3 = str(num3)
        archivo.write(numero1 + ", " +numero2+ ", " +numero3)
        archivo.write("\n")
        print ("Todos son iguales")
        archivo.write("Todos son iguales")
        archivo.write("\n")
        
def progra2():
    valor = int(input("Digite un valor: "))
    for i in range(1,valor+1):
        if (valor%i == 0):
            print("Se tiene una division exacta entre: ",i)
    
def progra3():
    numsuma = int(input("Ingrese un numero entero por favor: "))
    impsuma = 0
    for i in range(1,numsuma+1):
        impsuma = impsuma + i
    print("La suma es: ", impsuma)
    numero = str(impsuma)
    archivo.write("La suma desde 1 es: " + numero)
    archivo.write("\n")
    
def progra4():
    contador=0
    numimpar=1
    for i in range (1,51):
        impar = str(numimpar)
        archivo.write(impar + ", ")
        print(numimpar,",")
        numimpar = numimpar +2
        contador = contador+1
    print("La cantidad total de numeros impares en el intervalo es: ",contador)
    cont = str(contador)
    archivo.write("La cantidad total de numeros impares en el intervalo es: " + cont)
    archivo.write("\n")
    
def progra5():
    print("Digite la distancia de cada lado de un traingulo:")
    lado1 = int(input("Lado 1:"))
    lado2 = int(input("Lado 2:"))
    lado3 = int(input("Lado 3:"))
    if(lado1<0 or lado2 < 0 or lado3 <0):
        print("INGRESE UN VALOR POSITIVO")
    else:
        if(lado1 == lado2 and lado1==lado3):
            print("Es un triangulo equilatero")
            ladouno = str(lado1)
            ladodos = str(lado2)
            ladotre = str(lado3)
            archivo.write("Lado 1: "+ ladouno)
            archivo.write("\n")
            archivo.write("Lado 2: "+ ladodos)
            archivo.write("\n")
            archivo.write("Lado 3: "+ ladotre)
            archivo.write("\n")
            archivo.write("Es un triangulo equilatero")
            archivo.write("\n")
        elif(lado1 == lado2 or lado1==lado3 or lado2==lado3):
            print("Es un traingulo isosceles")
            ladouno = str(lado1)
            ladodos = str(lado2)
            ladotre = str(lado3)
            archivo.write("Lado 1: "+ ladouno)
            archivo.write("\n")
            archivo.write("Lado 2: "+ ladodos)
            archivo.write("\n")
            archivo.write("Lado 3: "+ ladotre)
            archivo.write("\n")
            archivo.write("Es un triangulo isosceles")
            archivo.write("\n")
        else:
            print("Es un triangulo escaleno")
            ladouno = str(lado1)
            ladodos = str(lado2)
            ladotre = str(lado3)
            archivo.write("Lado 1: "+ ladouno)
            archivo.write("\n")
            archivo.write("Lado 2: "+ ladodos)
            archivo.write("\n")
            archivo.write("Lado 3: "+ ladotre)
            archivo.write("\n")
            archivo.write("Es un triangulo escaleno")
            archivo.write("\n")
    
def progra6():
    valorsiete = int(input("Ingrese un valor que sea divisible entre 7: "))
    if(valorsiete%7 == 0):
        calc=math.factorial(valorsiete)
        print("El factorial de este numero es: ",calc)
        numero = str(valorsiete)
        fac = str(calc)
        archivo.write(numero + " es divisible entre 7 y su factorial es: " + fac)
        archivo.write("\n")
    else:
        print("ERROR, ESE NUMERO NO ES DIVISBLE ENTRE 7")
    
def progra7():
    print("Ingrese un numero de inicio y un numero de final.")
    inicio= int(input("Inicio: "))
    final= int(input("Final:"))
    while(inicio<=final):
        print(inicio,",")
        inicio = inicio + 2
    
def progra8():
    print("Ingrese dos numeros diferentes por favor.")
    numero1 = int(input("Numero 1: "))
    numero2 = int(input("Numero 2: "))
    if(numero1 > numero2):
        while(numero1>=numero2):
            print(numero1,",")
            numero1 = numero1 - 1
    elif(numero2 > numero1):
        while(numero2 >= numero1):
            print(numero2,",")
            numero2 = numero2 - 1
    else:
        print("Ingrese valores diferentes.")
    
def progra9():
    print ("CALCULADORA DE AREAS")
    print ("1. Circulo")
    print ("2. Triangulo")
    print ("3. Cuadrado")
    print ("4. Rectangulo")
    print ("5. Salir")
    def circ():
        print("*****AREA DE UN CIRCULO*****")
        radio = float(input("De el radio del circulo: "))
        area = 3.141592 * radio * radio
        print ("El area del circulo es: ", area)
        rad = str(radio)
        resul= str(area)
        archivo.write("El area de un circulo de radio "+rad+" es: "+resul)
        archivo.write("\n")
    def tri():
        print("*****AREA DE UN TRIANGULO*****")
        base = float(input("De la base del triangulo: "))
        altura = float(input("De la altura del triangulo: "))
        area = (base * altura)/2
        print("El area del triangulo es: ", area)
        b = str(base)
        h = str(altura)
        resul= str(area)
        archivo.write("Un triangulo con base "+b+" y altura "+h+" tiene un area de: "+resul)
        archivo.write("\n")
    def cuad():
        print("*****AREA DE UN CUADRADO*****")
        lado = float(input("De la longitud de uno de los lados: "))
        area = lado * lado
        print("El area del cuadrado es: ", area)
        side = str(lado)
        resul = str(area)
        archivo.write("Un cuadrado con lados de "+side+" tiene un area de: "+resul)
        archivo.write("\n")
    def rec():
        print("*****AREA DE UN RECTANGULO*****")
        base = float(input("De la base del rectangulo: "))
        altura = float(input("De la altura del rectangulo: "))
        area = base * altura
        print("El area de rectuangulo es: ",area)
        b = str(base)
        h = str(altura)
        resul= str(area)
        archivo.write("Un rectangulo con base "+b+" y altura "+h+" tiene un area de: "+resul)
        archivo.write("\n")
    op= int(input("Seleccione una opcion: "))
    while(op<=4):
        figuras = [circ,tri,cuad,rec]
        figuras[op-1]()
        op= int(input("Seleccione una opcion: "))
    
def progra10():
    print("Notas Finales")
    nota1 = int(input("Nota 1:"))
    nota2 = int(input("Nota 2:"))
    nota3 = int(input("Nota 3:"))
    if(nota1 < 0 or nota2 < 0 or nota3 < 0):
        print("Las notas no pueden ser negativas.")
    else:
        nota = (nota1 + nota2 + nota3)/3
        if (nota >= 60):
            print("Su nota final del curso es: ", nota)
            print("APROBADO")
            note = str(nota)
            archivo.write("Aprobo el curso. Su nota final fue de: "+note+" puntos")
            archivo.write("\n")
        else:
            print("Su nota final del curso es: ", nota)
            print("REPROBADO")
            note = str(nota)
            archivo.write("Reprobo el curso. Su nota final fue de: "+note+" puntos")
            archivo.write("\n")
    
def progra11():
    print("Años bisiestos")
    anio = int(input("Ingrese su año de nacimiento: "))
    if(anio%4 == 0):
        print("Este año fue bisiesto.")
        print("")
        an = str(anio)
        archivo.write("El año "+an+" fue un año bisiesto")
        archivo.write("\n")
    else:
        print("Este año no fue bisiesto.")
        print("")
        an = str(anio)
        archivo.write("El año "+an+" no fue un año bisiesto")
        archivo.write("\n")
    
def progra12():
    print("*****TAXIS SAN CARLOS*****")
    nombre = input("¿Cual es su nombre? ")
    modelo = int(input("¿Qué modelo es su taxi? "))
    km = float(input("¿Cuantos kilometros tiene recorrido su taxi? "))
    if(modelo<2007 and km > 20000):
        print("Su taxi necesita una renovacion.")
        mod= str(modelo)
        kilo=str(km)
        archivo.write("Nombre: "+nombre)
        archivo.write("\n")
        archivo.write("Modelo del taxi: "+mod)
        archivo.write("\n")
        archivo.write("Kilometraje: "+kilo)
        archivo.write("\n")
        archivo.write("Su taxi necesita una renovacion.")
        archivo.write("\n")
    elif(2007 <= modelo <= 2013 and km > 20000):
        print("Su taxi necesita mantenimiento.")
        mod= str(modelo)
        kilo=str(km)
        archivo.write("Nombre: "+nombre)
        archivo.write("\n")
        archivo.write("Modelo del taxi: "+mod)
        archivo.write("\n")
        archivo.write("Kilometraje: "+kilo)
        archivo.write("\n")
        archivo.write("Su taxi necesita mantenimiento.")
        archivo.write("\n")
    elif(modelo>2013 and km <10000):
        print("Su taxi esta en optimas condiciones")
        mod= str(modelo)
        kilo=str(km)
        archivo.write("Nombre: "+nombre)
        archivo.write("\n")
        archivo.write("Modelo del taxi: "+mod)
        archivo.write("\n")
        archivo.write("Kilometraje: "+kilo)
        archivo.write("\n")
        archivo.write("Su taxi esta en optimas condiciones.")
        archivo.write("\n")
    else:
        print("Consultar al mecanico")
        mod= str(modelo)
        kilo=str(km)
        archivo.write("Nombre: "+nombre)
        archivo.write("\n")
        archivo.write("Modelo del taxi: "+mod)
        archivo.write("\n")
        archivo.write("Kilometraje: "+kilo)
        archivo.write("\n")
        archivo.write("Consultar al mecanico.")
        archivo.write("\n")
def progra13():
    def contador(frase):
        vocales = "aeiouAEIOU"
        return [c for c in frase if c in vocales]
    texto = input("Esciba una palabra: ")
    cuenta = len(contador(texto))
    print("La cantidad de vocales en esta palabra es: ",cuenta)
def progra14():
    frase = input("Escriba una palabra: ")
    frase = frase.lower()
    vocales = ["a","e","i","o","u"]
    for x in vocales:
        veces=0
        for y in frase:
            if x==y:
                veces+=1
        print(x, "aparece", veces,"veces")
def salir():
    print("Gracias por utilizar nuestra aplicacion, hasta pronto.")
    archivo.close()
    sys.exit()

try:
    archivo.write("*****CODIGO DE PYTHON*****")
    archivo.write("\n")
    print("MENU SORPRESA")
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    print("Opcion 4")
    print("Opcion 5")
    print("Opcion 6")
    print("Opcion 7")
    print("Opcion 8")
    print("Opcion 9")
    print("Opcion 10")
    print("Opcion 11")
    print("Opcion 12")
    print("Opcion 13")
    print("Opcion 14")
    print("15. Salir")
    print("")
    opciones = int(input("Escoja una opcion del menu: "))
    while(opciones<=15):
        programas = [progra1,progra2,progra3,progra4,progra5,progra6,progra7,progra8,progra9,progra10,progra11,progra12,progra13,progra14,salir]
        programas[opciones-1]()
        print("")
        print("MENU SORPRESA")
        print("Opcion 1")
        print("Opcion 2")
        print("Opcion 3")
        print("Opcion 4")
        print("Opcion 5")
        print("Opcion 6")
        print("Opcion 7")
        print("Opcion 8")
        print("Opcion 9")
        print("Opcion 10")
        print("Opcion 11")
        print("Opcion 12")
        print("Opcion 13")
        print("Opcion 14")
        print("15. Salir")
        print("")
        opciones = int(input("Escoja una opcion del menu: "))

except(ValueError):
    print("A ocurrido un error, vuelva a intentarlo.")
    
    
        
        