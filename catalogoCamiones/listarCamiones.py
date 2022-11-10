#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
import json

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='ventaCamiones',
    password='ventaCamiones',
    database='ventaCamiones'
)

mycursor = mibd.cursor()

#consultar en la base de datos la lista de todos los camiones
sql="SELECT marca, modelo, precio, imagen, fechaCreacion FROM camiones ORDER BY fechaCreacion"
mycursor.execute(sql)
lc = mycursor.fetchall()

print("Conten-Type: text/html\n")

print(json.dumps(lc))