#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import cgi,codigoHTML,os
from http import cookies
import mysql.connector
from configuracion import configBD

#conectar a la base de datos
mydb = mysql.connector.connect(
  host = configBD["host"],
  user=configBD["user"],
  password=configBD["password"],
  database=configBD["database"]
)

estasDentro=False

todasCokis={} 
if'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split(';')
                                
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCokis[nombre]=valor

coki = cookies.SimpleCookie()

if 'SID' in todasCokis:
    #crear un cursor a la base de datos
    mycursor = mydb.cursor() 

    sql = 'SELECT count(*) FROM usuarios where rolId = 1 and coki like \"'+todasCokis['SID']+'\"'
    mycursor.execute(sql)
    myresult = mycursor.fetchone()

    if(myresult[0]==1):
        estasDentro=True
            
if estasDentro:

    form = cgi.FieldStorage()
    id = form['id'].value
    usu = form['usuario'].value

    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Historial del usuario","","Historial del usuario",
                                         '<form action="administrador.py" method="get"><button type="submit" class="btn btn-primary">volver a la lista de usuarios</button></form>',
                                         '<form action="logout.py" method="get"><button type="submit" class="btn btn-primary">Log out</button></form>',"",""))