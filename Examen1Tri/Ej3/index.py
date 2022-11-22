#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

precioProductosID = {
    "CA132" : 99.2,
    "CB231" : 55.7,
    "CA332" : 101.0,
    "CD563" : 65.2,
    "CB838" : 48.1
}

print("Conten-Type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
<title>Ejercicio 3</title>
</head>
<body>
<table>
<tr>
<td>Identificador</td>
<td>Precio</td>
</tr>""")

lista = precioProductosID.items()

suma = 0

for item in lista:
    print("<tr>")
    print("<td>"+item[0]+"</td>")
    print("<td>"+str(item[1])+"</td>")
    print("</tr>")

    suma = item[1] + suma

print("<tr>")
print("<td>Total</td>")
print("<td>"+str(suma)+"</td>")
print("</tr>")
print("""</table>
</body>
</html>""")