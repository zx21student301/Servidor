#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import os, datetime, codigoHTML
from http import cookies
from registroTiempos import regT
from configuracion import configBD
import mysql.connector

#conectar a la base de datos
mydb = mysql.connector.connect(
  host = configBD["host"],
  user=configBD["user"],
  password=configBD["password"],
  database=configBD["database"]
)

todasCokis={} 
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split('; ') 

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor


if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    coki["SID"]=todasCokis["SID"]
    cookie = coki["SID"].value
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) # enviar cookie caducada
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)
    logOut = True
            
if logOut:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT id FROM usuarios where coki like \"'+cookie+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    regT(myresult[0],"logout.py","")
    print("Content-Type: text/html\n")

    print(codigoHTML.cabeceraHTML.format("Log out con éxito",
          '<meta http-equiv="Refresh" content="2; URL=index.html"/>', "Log out con &eacute;xito. Redirigiendo","",""))
    print(codigoHTML.finalHTML)