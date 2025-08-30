"""1) Escribir un programa que solicite la edad del usuario. 
Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad."""

edad=int(input("Ingresa tu edad: "))

if edad >= 18 :
    print(f"Eres mayor de edad.")
    
    
"""2) Escribir un programa que solicite su nota al usuario. 
Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
en caso contrario deberá mostrar el mensaje “Desaprobado”."""

nota=float(input("Ingresa tu nota: "))

if nota >= 6:
    print(f"Aprobado!!!")
else:
    print(f"Desaprobado.")
    
    
"""3) Escribir un programa que permita ingresar solo números pares. 
Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, 
imprimir por pantalla "Por favor, ingrese un número par". 
Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""
    
numero_ingresado=int(input("Ingresa un numero: "))

if numero_ingresado %2 == 0:
    print(f"Ha ingresado un numero par.")
else:
    print(f"Por favor, ingresa un numero par.")
    
    
"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""
    
edad=int(input("Ingresa tu edad: "))

if edad < 12:
    print(f"Eres un niño/a.")
elif edad >= 12 and edad < 18:
    print(f"Eres un adolescente.")
elif edad >= 18 and edad < 30:
    print(f"Eres un adulto/a joven.")
else:
    print(f"Eres un adulto/a.")
    
"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string."""

contraseña_ingresada=input("Ingresa una contraseña: ")
longitud=len(contraseña_ingresada)

if longitud >=8 and longitud <=14:
     print(f"Ha ingresado una contraseña correcta.")
else:
     print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
     

"""Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria."""

import random
import statistics

numeros_aleatorios=[random.randint(1,100) for i in range(50)]

moda= statistics.mode(numeros_aleatorios)
print(moda)

mediana= statistics.median(numeros_aleatorios)
print(mediana)

media= statistics.mean(numeros_aleatorios)
print(media)

if media > mediana and mediana > moda:
    print("El sesgo es positivo.")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo.")
else:
    print("No hay sesgo.")
    
    
    
"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo 
de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, 
dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

palabra_frase=input("Ingresar una palabra o frase: ")

ultima_letra=palabra_frase[-1].lower()
vocales="aeiou"

if ultima_letra in "aeiou":
    print(palabra_frase + "!")
else:
    print(palabra_frase)
    
    
"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

nombre=input("Ingresa tu nombre: ")
numero=int(input("Elige una opcion [1] [2] [3]"))

if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
else:
    print(nombre.title())
    
    
"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías 
según la escala de Richter e imprima el resultado por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

intensidad_sismica=float(input("Ingresar la intensidad sismica registrada: "))

if intensidad_sismica < 3:
    print(f"Muy leve,(imperceptible.)")
elif intensidad_sismica >= 3 and intensidad_sismica < 4 :
    print(f"Leve,(ligeramente perceptible.)")
elif intensidad_sismica >= 4 and intensidad_sismica < 5:
    print(f"Moderado,(sentido por personas,pero generalmente no genera daños. )")
elif intensidad_sismica >= 5 and intensidad_sismica < 6:
    print(f"Fuerte, (puede causar daños en estructuras débiles.)")
elif intensidad_sismica >= 6 and intensidad_sismica < 7:
    print(f"Muy fuerte, (puede causar daños significativos.)")
elif intensidad_sismica >= 7:
    print(f"Extremo,(puede causar daños a gran escala.) ") 
    
    
#10)
hemisferio= input("Ingresa en que parte del hemisferio te encuentras (N/S): ").upper()
mes=input("Ingresa mes del año (actual): ").lower()
dia=int(input("Ingresa el dia (actual): "))

if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes=="febrero") or (mes=="marzo" and dia <=20):
        print(f"Te encuentras en invierno.")
    elif (mes=="marzo" and dia>=21) or (mes=="abril") or (mes=="mayo") or (mes=="junio" and dia<=21):
        print(f"Te encuentras en primavera")
    elif (mes=="junio" and dia >=21) or (mes=="julio") or (mes=="agosto") or (mes=="septiembre" and dia <=20):
        print(f"Te encuentras en verano.")
    elif (mes=="septiembre" and dia>= 21) or (mes=="octubre") or (mes=="noviembre") or (mes=="diciembre" and dia<=20):
        print(f"Te encuentras en otoño.")
        
elif hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes=="febrero") or (mes=="marzo" and dia <=20):
        print(f"Te encuentras en verano.")
    elif (mes== "marzo" and dia >=21) or (mes== "abril") or (mes=="mayo") or (mes=="junio" and dia<=20):
        print(f"Te encuentras en otoño.")
    elif (mes=="junio" and dia >=21) or (mes=="julio") or (mes=="agosto") or (mes=="septiembre" and dia <=20):
        print(f"Te encuentras en invierno.")
    elif (mes=="septiembre" and dia>= 21) or (mes=="octubre") or (mes=="noviembre") or (mes=="diciembre" and dia<=20):
        print(f"Te encuentras en primavera. .")
    else:
        print(f"Has ingresado un hemisferio incorrecto!")
    
    
    
    
    



