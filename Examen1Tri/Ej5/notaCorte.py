#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import cgi

args = cgi.parse()


print("Conten-Type: text/plain\n")

f = open("dat/nombres.dat" ,"rt")

nombres = []

for n in f:
    nombres.append(n)

f.close()

f = open("dat/notas.dat" ,"rt")

notas = []

for n in f:
    notas.append(n)

f.close()

nCorte = args["corte"][0]
f = open("dat/salida.dat","a")
for i in range(len(notas)):
    if(int(notas[i]) >= int(nCorte)):
        f.write(nombres[i]+" "+notas[i]+"\n")
f.close()