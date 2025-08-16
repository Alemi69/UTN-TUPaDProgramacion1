"""1.Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("¡Hola mundo!")"""



"""2.Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre=input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")"""



"""3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo
en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
edad=int(input("Ingresa tu edad: "))
residencia=input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}.") """



"""4.Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
radio=float(input("Ingrese el radio de un circulo: "))
area=math.pi *(radio **2)
perimetro= 2* math.pi * radio

print(f"El area del circulo es:{area}")
print(f"El perimetro del circulo es: {perimetro}")"""



"""5.Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

cantidad_segundos=int(input("Ingresa una cantidad de segundos: "))

horas= cantidad_segundos / 3600
print(f"Segundos ingresados:{cantidad_segundos},equivale a {horas} horas.") """



"""6.Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero_ingresado=int(input("Ingresa un numero entero: "))

print("***TABLA DE MULTIPLICAR***")

for i in range(1,11):
    resultado=numero_ingresado * i
    
    print(f"{numero_ingresado} x {i} = {resultado}") """
    
    
""" 7.Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos,
dividirlos, multiplicarlos y restarlos.

numero1=int(input("Ingresa primer numero entero, distinto de cero: "))
numero2=int(input("Ingresa segundo numero entero, distinto de cero: "))

suma= numero1 + numero2
resta=numero1 - numero2
multiplicacion=numero1 * numero2
division=numero1 / numero2

print(f"El resultado de {numero1} + {numero2}= {suma}")
print(f"El resultado de {numero1} - {numero2}= {resta}")
print(f"El resultado de {numero1} * {numero2}= {multiplicacion}")
print(f"El resultado de {numero1} / {numero2}= {division}") """



"""8.Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
IMC = peso en kg / altura m 2 


peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es de IMC: {imc}")"""



"""9.Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
Tener en cuenta la siguiente equivalencia: Temperatura en Fahrenheit = 9/5.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 en Celsius+ 32

celsius=float(input("Ingresa un valor de temperatura en grados Celsius: "))

fahrenheit= (9/5) * celsius + 32

print(f"La equivalencia en grados Fahrenheit es:{fahrenheit}")"""



"""10.Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1=float(input("Ingresa tu primer numero: "))
num2=float(input("Ingresa tu segundo numero: "))
num3=float(input("Ingresa tu tercer numero: "))

suma= num1 + num2 + num3
promedio=suma / 3

print(f"El promedio de los tres numeros ingresados es: {promedio}")"""


