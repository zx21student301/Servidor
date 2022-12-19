#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe


aprobado = 5
texto=""

f = open("datos.dat", "rt")
nombres = f.read()
listaNombres= nombres.split(" ")
f.close()

contNota=0

print("Content-Type: text/html\n")


for nota in listaNombres:
    
    if int(nota)>=int(aprobado):
        texto += listaNombres[contNota]
        texto += " "+nota+"\n"
    contNota +=1  

    f = open("aprobados.dat", "a")
    f.write(texto)
    f.close()

else:
    f = open("suspensos.dat", "a")
    f.write(texto)
    f.close()


print("""<!DOCTYPE html>
<html>
<head>
</head>
<body>""")
print("<p>Filtro realizado</p><p>",texto,"</p>")
print("""
</body>

</html>""")
