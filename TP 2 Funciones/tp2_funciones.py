"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal."""

def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
“Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    return nombre

llamada=("Alejandro")
print(f"Hola {llamada}!")

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

print("\n---Ingresa tus datos ---")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados."""

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

print("\n--- Calculadora de Círculo ---")

valor_radio = float(input("Ingresa el radio del círculo: "))

area = calcular_area_circulo(valor_radio)
perimetro = calcular_perimetro_circulo(valor_radio)

print(f"\nEl área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función."""

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

print("--- Convertir los Segundos en Horas ---")

cantidad_segundos = int(input("Ingresa la cantidad de segundos: "))

horas_calculadas = segundos_a_horas(cantidad_segundos)

print(f"La cantidad de segundos a horas son: {horas_calculadas:.2f} horas.")


"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
print("--- Tabla de Multiplicar ---")

numero_ingresado = int(input("Ingresa el número del que quieres la tabla: "))

tabla_multiplicar(numero_ingresado)


"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara."""

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    resultados = (suma,resta,multiplicacion,division)
    return resultados

num1 = 10
num2 = 2
resultados_tupla = operaciones_basicas(num1,num2)

suma_res, resta_res, mult_res, div_res = resultados_tupla

print(f"Los números de entrada son: {num1} y {num2}")
print(f"Suma:{suma_res}")
print(f"Resta:{resta_res}")
print(f"Multiplicación:{mult_res}")
print(f"División:{div_res}")


"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso_kg = float(input("Ingresa tu peso en kilogramos: "))
altura_m = float(input("Ingresa tu altura en metros: "))

imc_calculado = calcular_imc(peso_kg, altura_m)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")


"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

temp_celsius=float(input("Ingresa una temperatura en grados celsius: "))

far_equivalente = celsius_a_fahrenheit(temp_celsius)

print(f"El equivalente en grados Fahrenhiet es de: {far_equivalente:.2f}°F")

    
"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función."""

def calcular_promedio(a, b, c):
    suma = ( a + b + c)
    promedio = suma / 3
    return promedio

numero1 =float(input("Ingresa primer numero: "))
numero2 =float(input("Ingresa segundo numero: "))
numero3 =float(input("Ingresa tercer numero: "))

cal_promedio = calcular_promedio(numero1 ,numero2,numero3)

print(f"El promedio de los tres numeros ingresado es: {cal_promedio:.2f}")
