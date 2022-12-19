#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe

import cgi 
from http import cookies
import datetime

args = cgi.parse()

puntos= 0

puntos = args["puntos"][0]
puntuacion = 0

puntuacion = puntuacion + int(puntos)

coki = cookies.SimpleCookie()
coki["Puntos"] = puntuacion
expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
coki['Puntos']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
print(coki)

#se pone siempre despues de las cookies 
print("Content-Type: text/plain\n")