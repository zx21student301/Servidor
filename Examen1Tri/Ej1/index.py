#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

print("Conten-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
<title>Ejercicio 1</title>
</head>
<body>""")

for i in range(1,21):
    print("<div id='contenedor"+str(i)+"'>")
    print("<img src='img/coche"+str(i)+".png' alt='imagen de coche "+str(i)+"'>")
    print("</div>")

print("""</body>
</html>""")