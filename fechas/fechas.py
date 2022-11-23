#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python
import datetime
from datetime import date,timedelta
import cgi

##Fecha y hora actual
x = datetime.datetime.now()

##Fecha que quieras
y = datetime.datetime(2003, 8, 23)

print("Content-type: text/plain\n")

print(type(x))
print(x)
print(y)

##ver el año
print(x.year)

##ver el dia de la semana (tipo string)
print(x.strftime("%A"))
print(y.strftime("%A"))

##EJERCICIO 1
print("************************************")
print("EJERCICIO 1")
print("************************************")
#fecha
print(x)
#año
print(x.year)
#mes (numero)
print(x.month)
#mes (string)
    #nombre mes entero
print("%B :"+x.strftime("%B"))
    #nombre mes acortado
print("%b :"+x.strftime("%b"))
#numero de la semana del año
print("%W :"+x.strftime("%W"))
#dia de la semana (numero)
print("%w :"+x.strftime("%w"))
#dia de la semana (string)
    #nombre dia entero
print("%A :"+x.strftime("%A"))
    #nombre dia acortado
print("%a :"+x.strftime("%a"))
#dias que tiene el año desde la fecha
print("%j :"+x.strftime("%j"))
#dias que tiene el mes
print("%d :"+x.strftime("%d"))

print("************************************")
print("EJERCICIO 2")
print("************************************")

datosForm = cgi.FieldStorage()

fecha = datosForm["fecha"].value if "fecha" in datosForm else datetime.datetime.now()

if fecha:
    fecha = fecha.split("-")
    fechaDT = datetime.datetime(int(fecha[0]),12,31)
    if int(fechaDT.strftime("%j")) == 366:
        print("bisiesto")
    else:
        print("No es bisiesto")
else:
    print("Error")

print("************************************")
print("EJERCICIO 3")
print("************************************")

##resta dias a la fecha que se le pase
dt = date.today() - datetime.timedelta(5)
##suma dias a la fecha que se le pase
dd = date.today() + datetime.timedelta(15)

print("Fecha actual: ", date.today())
print("5 días antes de la fecha actual: ",dt)
print("15 días después de la fecha actual: ",dd)

print("************************************")
print("EJERCICIO 4")
print("************************************")

print("Hoy es ",date.today())
ayer = date.today() - datetime.timedelta(1)
print("Ayer fue ",ayer)
mañana = date.today() + datetime.timedelta(1)
print("Mañana es ",mañana)

print("************************************")
print("EJERCICIO 5")
print("************************************")

for i in range (0,6):
    dia = date.today() + datetime.timedelta(i)
    print("dia",i,dia)

print("************************************")
print("EJERCICIO 6")
print("************************************")
##Suma minutos y segundos al datetime que le pases
dm = datetime.datetime.now() + datetime.timedelta(minutes=2,seconds=5)
print(datetime.datetime.now())
print(dm)