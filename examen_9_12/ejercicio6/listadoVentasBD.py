#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="museo",
    password="museo",
    database="museo"
)

print("Content-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1>Listado de entradas compradas</h1>""")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM comprador ORDER BY id")

listaCompradores = mycursor.fetchall()

for comprador in listaCompradores:
    print("<hr><h4>",comprador[1],"ha comprado:</h4>")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM entradas WHERE id_comprador="+str(comprador[0]))
    listaEntradas = mycursor.fetchall()
    for entradas in listaEntradas:
        print("<p>",entradas[1]," entradas de adultos y "+str(entradas[2])+" entradas de menores, con un precio total de "+str(entradas[3])+"€"+ "</p>")

print("""
</body>
</html>""")
