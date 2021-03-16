import psycopg2
import sys
archivo = open("201807151.txt","a")

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "Abuelokiko50"
PSQL_DB = "primerparcial"

connection_address = """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
connection = psycopg2.connect(connection_address)

cursor = connection.cursor()

def progra1():
    print("Ingrese 5 valores enteros por favor: ")
    numeros = []
    for i in range(5):
      numero = int(input("Introduce un numero: ".format(i + 1)))
      numeros.append(numero)
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    print("El numero mas grande es:", mayor)
    print("El numero mas pequeño es:", menor)
    num1 = str(numeros[0])
    num2 = str(numeros[1])
    num3 = str(numeros[2])
    num4 = str(numeros[3])
    num5 = str(numeros[4])
    grande = str(mayor)
    pequenio = str(menor)
    archivo.write(num1 + ", " +num2 + ", " + num3 + ", "  + num4 + ", " + num5)
    archivo.write("\n")
    archivo.write("El numero mas grande es: " + grande)
    archivo.write("\n")
    archivo.write("El numero mas pequeño es:" + pequenio)
    archivo.write("\n")
    SQL = "insert into primerprograma (lenguaje,valoruno,valordos,valortres,valorcuatro,valorcinco,mayor,menor) values ('Python' , %s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(SQL, (num1,num2,num3,num4,num5,grande,pequenio))
    connection.commit()
    print("")
def progra2():
    horas = int(input("Cantidad de horas trabajadas en el mes: "))
    tiempo = str(horas)
    if (horas <8):
        print("No trabajo ni un dia.")
        print("Sueldo : Q0.00")
    elif(horas <= 40):
        sueldo = 50 * horas
        salario = str(sueldo)
        print("Sueldo: Q",sueldo)
        archivo.write("Durante el mes trabajo " + tiempo + " horas, por lo que su sueldo es de Q"+salario)
        archivo.write("\n")
        SQL = "insert into segundoprograma (lenguaje,horas,sueldo) values ('Python' , %s,%s);"
        cursor.execute(SQL, (tiempo,salario))
        connection.commit()
    elif(horas > 40):
        diferencia = horas - 40
        sueldo = (50 * 40) + (75 * diferencia)
        print("Sueldo: Q",sueldo)
        salario = str(sueldo)
        archivo.write("Durante el mes trabajo " + tiempo + " horas, por lo que su sueldo es de Q"+salario)
        archivo.write("\n")
        SQL = "insert into segundoprograma (lenguaje,horas,sueldo) values ('Python' , %s,%s);"
        cursor.execute(SQL, (tiempo,salario))
        connection.commit()
    print("")
def progra3():
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
            SQL = "insert into tercerprograma (lenguaje,valoruno,valordos,valortres,tipo) values ('Python' , %s,%s,%s,'Equilatero');"
            cursor.execute(SQL, (ladouno,ladodos,ladotre))
            connection.commit()
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
            SQL = "insert into tercerprograma (lenguaje,valoruno,valordos,valortres,tipo) values ('Python' , %s,%s,%s,'Isoceles');"
            cursor.execute(SQL, (ladouno,ladodos,ladotre))
            connection.commit()
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
            SQL = "insert into tercerprograma (lenguaje,valoruno,valordos,valortres,tipo) values ('Python' , %s,%s,%s,'Escaleno');"
            cursor.execute(SQL, (ladouno,ladodos,ladotre))
            connection.commit()
    print("")
def progra4():
    dia = int(input("Ingrese su dia de nacimiento: "))
    mes = int(input("Ingrese su mes de nacimiento: "))
    anio = int(input("Ingrese su año de nacimiento: "))
    diferenciauno = 2021 - anio
    diferenciados = 3 - mes
    diferenciatres = 4 - dia
    if (diferenciados < 1):
        diferenciauno = diferenciauno - 1
        diferenciados = 12 + diferenciados
    if (diferenciatres < 1):
        diferenciados = diferenciados - 1
        diferenciatres = -1 * diferenciatres
    print("Su edad al dia 3 de marzo del 2021 es de ",diferenciauno," años, ",diferenciados," meses y ",diferenciatres," dias")
    uno = str(diferenciauno)
    dos = str(diferenciados)
    tres = str(diferenciatres)
    dias = str(dia)
    meses = str(mes)
    an = str (anio)
    archivo.write("Fecha de nacimiento: "+dias+" del "+meses+ " del "+an)
    archivo.write("\n")
    archivo.write("Su edad al dia 4 de marzo del 2021 es: "+uno+" años, "+dos+" meses y "+tres+" dias")
    archivo.write("\n")
    SQL = "insert into cuartoprograma (lenguaje,diainicio,mesinicio,anioinicio,anios,meses,dias) values ('Python' , %s,%s,%s,%s,%s,%s);"
    cursor.execute(SQL, (dias,meses,an,uno,dos,tres))
    connection.commit()
    print("")
def salir():
    print("Gracias por utilizar nuestra aplicacion, hasta pronto.")
    archivo.close()
    cursor.close()
    connection.close()
    sys.exit()
try:
    archivo.write("*****CODIGO DE PYTHON*****")
    archivo.write("\n")
    print("1. Mayor y menor de 5 numeros")
    print("2. Calculo de salario")
    print("3. Tipos de Triangulos")
    print("4. Calculo de Edad")
    print("5. Salir")
    opciones = int(input("Seleccione una opcion del menu: "))
    while(opciones <= 5):
        try:
            programas = [progra1,progra2,progra3,progra4,salir]
            programas[opciones-1]()
            print("")
            print("1. Mayor y menor de 5 numeros")
            print("2. Calculo de salario")
            print("3. Tipos de Triangulos")
            print("4. Calculo de Edad")
            print("5. Salir")
            opciones = int(input("Seleccione una opcion del menu: "))
        except(ValueError):
            print("Ocurrio un problema durante la ejecucion del programa.")
            opciones = int(input("Seleccione una opcion del menu: "))
except(ValueError):
    print("Valor no contemplado.")
