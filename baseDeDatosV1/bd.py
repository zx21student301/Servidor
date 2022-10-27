#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='generico',
    password='generico',
    database='generico'
)

mycursor = mibd.cursor()

#Creamos la sentencia para añadir los valores a la columnas y especificamos el tipo de dato que vamos a insertar
#%s -> string
#%d -> int
#%f -> float
sql = 'INSERT INTO tabla (columna1, columna2, columna3) VALUES (%s,%s,%d)'
val = ('valor 1','valor 2',0) #valores que se van a añadir en las posiciones por orden
mycursor.execute(sql,val) #ejecuta la sentencia de sql

mibd.commit() #hacemos un commit en la base de datos

print("Conten-Type: text/html\n")

print(mycursor.rowcount, 'Registro insertado.')