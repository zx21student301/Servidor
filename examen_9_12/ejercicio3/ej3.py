#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe


marcasCorredor = {
    '1001':["KIPRUTO, RHONEX",3469],
    '1002':["KIPLIMO, JACOB",3457],
    '1003':["KANDIE, KIBIWOTT",3452],
    '1007':["MUTISO, ALEXANDER",3479],
    '1008':["WANDERS, JULIEN",3595],
    '1009':["KIPLIMO, PHILEMON",3491]
}

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
        
    </head>
    <body>
        <table>
            <tr>
                <th>Dorsal</th>
                <th>Corredor</th>
            </tr>
''')

ganador = ""
for corredor in marcasCorredor:
    print('''
            <tr>
                <td>''',corredor,'''</td>
                <td>'''+str(marcasCorredor[corredor][0])+'''</td>
            </tr>
         ''')

ganador += min(marcasCorredor[corredor][1])

print('''
            <tr>
                <td>Ganador</td>
                <td>''',ganador,'''</td>
            </tr>
        </table>
    </body>
</html>
''')