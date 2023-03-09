#Inicializacion de variables
'''
x = float(4)
name = ""

''Seccion de comentarios --vowel(3)''

conff = input("Menu?\n")

if conff == "y":
    #Menu - Selector
    Nav = int(input("1.Nombres\n2.Match\n3"))
    def menu(no):
        switch={
        1:logNames(),
        2:Match(),
        3:'i',
        4:'o',
        5:'u'
        }
        return switch.get(no,"input")
       
    def logNames():        
        #.1) Mostrar nombres
        name = input("# Mostrar nombres\nComo te llamas?\n")
        return print("Tu nombre es "+name+"?")

    def Match():        
        #.2) Sumar 2 numeros y mostar un resultado --Match
        number = input("Dame un numero:\n")
        one = int(number)
        number = input("Dame otro numero:\n")
        two = int(number)
        number = one + two
        return print(f'Number: {number}')
else:
    num = int(input("Favor digite un numero\n"))
    if num > 0:
        print(f"El valor del numero es: {num} Positivo")
    else:
        print(f"El valor del numero es: {num}")'''


# 2.00 = Lunes, Martes, miercoles; 2.50 = jueves y viernes; 3.00 = sabados y domingos
'''Time limit: 5mnt || diaSemana != dias : error'''


'''
diaSemanas = input("Seleccione dias de la semana: 'lunes','martes','miercoles','jueves','viernes','sabados','domingos':\n")
time = int(input("Seleccione el tiempo en minutos:\n"))
#costo = float(0)
def cobroHour(costo):
    costo = float(time * costo)
    print(f"Costo estipúlado es:\n${costo}")
     

if diaSemanas == 'lunes' or diaSemanas == 'martes' or diaSemanas == 'miercoles':
    # var = 2.00 || var = time * var
    if time > 5:
        costo = 2.00        
        cobroHour(costo)
    else:
        print("Costo estipúlado:\n$0.00")
    

if diaSemanas == 'jueves' or diaSemanas == 'viernes':
    #2.50
    if time > 5:
        costo = 2.50        
        cobroHour(costo)
    else:
            print("Costo estipúlado:\n$0.00")  
if diaSemanas == 'sabados' or diaSemanas == 'domingos':
    #3.00
    if time > 5:
        costo = 3.00        
        cobroHour(costo)
    else:
        print("Costo estipúlado:\n$0.00")
'''
#XD = """Esto se supone que es un comentario, pero vamos a probar si sirve XD, bueno. Espero que funcione,...\nDespues de todo si fallo no pasa nada y puedo preguntarle al profe hasta que se estrece(Excelente plan).\nEnd Fin"""

#Ciclos Repetitivos
'''def ciclosRepetitivos():
        
    for x in range(2,12,2):
        print(x)
    print(XD)'''

'''for x in "banana":
    print(x)'''

'''for x in range(6):
    if x == 6:break
    print(x)
else:
        print("Finished")'''

'''i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("var 'i' no es menor a 6")'''

#Strings are Arrays
'''txt = "The best things in life are free!"
print(len(txt))
print("free" in txt)'''

'''txt = "The best things in life are free!"
if "free" in txt:
    print("Encontrado!\n")
else:
    print("Sorry!, no se encontro la palabra\n")# "abcdefghijklmnopqrstuvwxyz"
abc = -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,0,1,2,3,4,5,6,7,8,9,10,11
print(abc[-12:])

a = "Hello world!"
print(a.upper())
print(a.strip())#Return "Hello world!"
print(a.lower())
print(a.replace("H","J"))
print(a.split(","))#Return ["Hello0 world"]
'''
#String Format
'''age = 36
txt = "My name is William, I am "+ str(age) # Conversion a Str
print(txt)

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to play {} dollars for {} pieces of item {}." # Inyectar variables | Posiciones: {2} - {0} - {1}
print(myorder.format(quantity, itemno, price))'''

pyDoc = '''#Cap 2 || MANEJO DE DATOS <>\n
Admnistracion de Lista.

Estas pueden usarse para el manejo de datos. Empecemos por su uso:

|> Simple

|-> thislist = ["apple","banana","cherry"]\nprint(thislist) //otros usos : len.(longitud) >> 5 | type.(tipo-dato) >> class 'list'

|> Posiciones

|-> thislist = ['apple','banana','cherry','blackberry','mango']

|-> print(thislist[1]) /#/ Hubicacion de una posicion de la lista = {0:inicio, 1:Consecutivo, etc...}

|-> print(thislist[-1]) /#/ Hubicacion en la ultima posicion de la lista

|-> print(thislist[1:4]) /#/ Hubicacion - dentro de un rango de la lista
/>Ej: {1, 2, 3, 4, 5} | Rango(1:4) >> print( 2 - 3 - 4 );

|-> print(thislist[-4:-1]) /#/ Hubicacion - dentro de un rango de la lista (Iniciando desde atras)
/>Ej: {1, 2, 3, 4, 5} | Rango(-4:-1) >> print( 2 - 3 - 4 - 5);

|-> print(thislist[:4]) /#/ Hubicacion - dentro de un rango de la lista (el "vacio" significa la primera posicion independientemente si esta en el inicio o al final)
/>Ej: [:4] => 1-4 || [1:] => 2-4

|> Filtro

|-> thislist = ['apple','banana','cherry','blackberry','mango'] /#/ Para poder hacer un filtro de una lista de una determinada palabra se puede usar el siguiente code.
/> if "apple" in thislist:
        print("yes, 'apple' is in this list")

|> Insert

|-> thislist = ['apple','banana','cherry','blackberry','mango'] /#/ Se puede insertar uno o varios datos dentro de una Lista -> En este caso por posiciones 
/> thislist[1:3] = ["blackcurrant","watermelon"] \n print(thislist)

>> Tambien se puede de esta forma: 'thislist.insert(2, "watermelon")'
'''
thislist = ['apple','banana','cherry','blackberry','mango']
#Insertar la lista ----------------------------------------------------------------
'''print(thislist)
rm = input("Ingrese una fruta + a la lista:\n")
ps = int(input("Ingrese la posicion para la dicha fruta:\n"))
thislist.insert(ps, rm)
print(thislist)'''
#Fitrar la lista-------------------------------------------------------------------
if "apple" in thislist:
    print("Yes, apple esta en esta lista")
else:
    print("'apple' no esta en la lista")