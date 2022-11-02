#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/plain\n")

import cgi
import json
import codigoHTML as HTML
import os
import hashlib
import mysql.connector

#conectar a la base de datos
mibd = mysql.connector.connect(
    host='localhost',
    user='log/reg',
    password='log/reg',
    database='log/reg'
)

args =  cgi.parse()

nom = args["nombre"][0]
pwd = args["pwd"][0]
email = args["email"][0]

pwdCod = hashlib.sha512(str.encode(pwd))

usuario = []

usuario.append(nom)
usuario.append(pwdCod.hexdigest())
usuario.append(email)

listaUsuarios = []

if (os.path.exists("usuarios/usuarios.json")):
    f = open("usuarios/usuarios.json" ,"rt")
    usuariosEnJson = json.loads(f.read())
    f.close()

    for valor in usuariosEnJson:
        elemento = []
        elemento.append(valor[0])
        elemento.append(valor[1])
        elemento.append(valor[2])

        listaUsuarios.append(elemento)

        

listaUsuarios.append(usuario)


usuariosJson = json.dumps(listaUsuarios)

f = open("usuarios/usuarios.json" ,"wt")

f.write(usuariosJson)

f.close()

HTML.redireccionPrincipal()
