#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector
from configuracion import configBD

def regT():
    #conectar a la base de datos
    mydb = mysql.connector.connect(
    host = configBD["host"],
    user=configBD["user"],
    password=configBD["password"],
    database=configBD["database"]
    )