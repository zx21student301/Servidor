#!C:\Users\zx21student234\AppData\Local\Programs\Python\Python311\python.exe

print("Content-Type: text/html\n")

print('''
<!DOCTYPE html>
<html lang="en">
    <head>
    
    </head>
    <body>
''')

for x in range(1,11):
    print('''
            <a href="producto''',x,'''.html" title="Producto numero ''',x,'''">Ir al producto ''',x,'''</a> <br>
         ''')

print('''
    </body>
</html>
''')