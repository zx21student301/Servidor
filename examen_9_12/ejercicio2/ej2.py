#!C:\Users\zx21student301\AppData\Local\Microsoft\WindowsApps\python


def cuentaNumeros(frase):
    salida=0
    if len(frase) > 100:
        return 'error'
    
    for i in frase:
       if(i== '0') or (i== '1') or (i== '2') or (i== '3') or (i== '4') or (i== '5') or (i== '6') or (i== '7') or (i== '8') or (i== '9'): 
            salida += 1
    
    return salida

print("Content-Type: text/plain\n")

print(cuentaNumeros("hola 123"))
print(cuentaNumeros("En un lugar de la mancha"))
print(cuentaNumeros("699 766 987"))