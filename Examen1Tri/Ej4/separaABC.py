#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import cgi
from http import cookies
import os

args = cgi.parse()

texto = args["texto"][0]

print("Conten-Type: text/plain\n")

todasCokis={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor)=elemCoki.split('=')
        todasCokis[nombre]=valor

coki= cookies.SimpleCookie()

if(texto == ""):
    coki["empiezaABC"] = ""
    coki["otras"] = ""
else:
    for l in texto:
        if((l[0] == 'A')|(l[0] == 'B')|(l[0] == 'C')):
            if("empiezaABC" in todasCokis):
                coki["empiezaABC"] = texto + " " + str(coki["empiezaABC"])
            else:
                coki["empiezaABC"] = texto + " "
        else:
            if("otras" in todasCokis):
                coki["otras"] = texto + " " + str(coki["otras"])
            else:
                coki["otras"] = texto + " "

print("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta http-equiv="Refresh" content="0; URL=muestraABC.py" />
</head>
<body>
</body>
</html>
""")




