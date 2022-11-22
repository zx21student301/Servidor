#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python

import cgi

args = cgi.parse()

figura=int(args["figura"][0])

print("Conten-Type: text/plain\n")

letras=['A','6','I','O','U']

def concatenaVocales(letras):
    cadena = ""
    error = False
    if (len(letras) <= 5):
        for x in letras:
            if ((x != 'A') & (x != 'E') & (x != 'O') & (x != 'I') & (x != 'U')):
                print("error")
                error = True
                break
            else:
                cadena = cadena + x
        if(error == False):
            print(cadena)
    else:
        print("error")

if(figura == 1):
    concatenaVocales(letras)