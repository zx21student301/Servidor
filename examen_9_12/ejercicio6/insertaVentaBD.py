#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe

import cgi
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="museo",
    password="museo",
    database="museo"
)

args = cgi.parse()

dni=""
adultos=""
menores=""

dni = args["dni"][0]
adultos = args["adultos"][0]
menores = args["menores"][0]

noVacio=False
usuario=False

print("Content-Type: text/plain\n")

if dni!=" " and adultos!=" " and menores!=" ":
    noVacio=True
    
else:
    print("Faltan datos por rellenar")

if noVacio:
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM comprador")

    lista = mycursor.fetchall()
    for comprador in lista:
        if comprador[1]== dni: #str(socios[1]).lower()==socio.lower() para que no importe mayusc o minusc
            usuario=True
            idComprador=comprador[0]
total = (int(adultos)*20) + (int(menores)*5)

if usuario:
    sql = "INSERT INTO `entradas`(numAdultos, numMenores, total, id_comprador) VALUES (%s,%s,%s,%s)"
    valores=(adultos,menores,total,idComprador)
    mycursor.execute(sql, valores)
    mydb.commit()
    print("Comprado con exito")
else:
    print("El usuario no existe")
