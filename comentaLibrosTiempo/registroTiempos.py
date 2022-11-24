#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
from configuracion import configBD

def regT(id,op,pa):
    #conectar a la base de datos
    mydb = mysql.connector.connect(
    host = configBD["host"],
    user = configBD["user"],
    password = configBD["password"],
    database = configBD["database"]
    )

    #variables que cada operacion mandará a la función
    id_usuario = id
    oper = op
    param = pa

    #crear un cursor a la base de datos
    mycursor = mydb.cursor()

    sql = "INSERT INTO regOperaciones (id_usuario, operacion, parametros, tmpOperacion) VALUES (%s, %s, %s, now());"
    value = (id_usuario,oper,param)

    mycursor.execute(sql,value)
    mydb.commit()