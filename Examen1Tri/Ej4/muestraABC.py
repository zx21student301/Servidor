#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

from http import cookies
import os

todasCookies = {}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] 
    listaCoki = listaCoki.split('; ') 

    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre] = valor

print("Conten-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
<title>Ejercicio 4</title>
</head>
<body>""")

print("Palabras que empiezan por ABC: "+todasCookies['empiezaABC'])
print("Palabras que no empiezan por ABC: "+todasCookies['otras'])

print("</body>")
print("</html>")