"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i  in range(0,100+1):
    print(i) 
    
"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

num_ingresado=int(input("Ingresa un numero entero: "))

num_positivo=abs(num_ingresado) 
cadena_numero=str(num_positivo)
cantidad_digitos=len(cadena_numero)

print(f"El numero ingresado es: {num_ingresado} y la cantidad de digitos es: {cantidad_digitos}")



"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

num1=int(input("Ingrese primer numero entero: "))
num2=int(input("Ingrese segundo numero entero: "))

suma=0

if num1 < num2:
    start= num1 +1 
    end= num2
else:
    start=num2 +1
    end=num1 

for i in range(start, end):    
    suma += i
    
print(f"La suma de {num1} y {num2} es: {suma}")


"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

suma = 0

numero_ingresado = -1 

while numero_ingresado != 0:
    numero_ingresado = int(input("Ingresa un número entero. Recuerda:cero para terminar: "))
    suma += numero_ingresado

print(f"El total acumulado es: {suma}")


"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

numero_secreto= random.randint(0,9)
cont=0
numero_ingresado= -1

while numero_ingresado != numero_secreto:
    cont += 1
    try:
        numero_ingresado = int(input("Ingresa un número entero entre 0 y 9: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingresa solo un número.")
        continue
    if numero_ingresado < numero_secreto:
        print("El número secreto es más alto. Sigue intentando...")
    elif numero_ingresado > numero_secreto:
        print("El número secreto es más bajo. Sigue intentando...")
    
print(f"¡El número {numero_ingresado} es el correcto! ¡Felicitaciones!")
print(f"Necesitaste {cont} intentos para acertar el número.")


"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for i in range(100, -1, -2):
    print(i)
    
"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

suma=0
num_ingresados=int(input("Ingresar numeros: "))

for i in range(0, num_ingresados +1):
    suma += i
    
    print(f"La suma de los numeros ingresados entre el cero y {num_ingresados} es de: {suma}")
    

"""8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

num_pares=0
num_impares=0
num_negativos=0
num_positivos=0

cantidad_numeros = 20 

for i in range(cantidad_numeros):
    try:
        num_ingresado = int(input(f"Ingresa el número {i+1} de {cantidad_numeros}: "))
        
        if num_ingresado % 2 == 0:
            num_pares += 1 
        else:
            num_impares += 1

        if num_ingresado > 0:
            num_positivos += 1 
        elif num_ingresado < 0:
            num_negativos += 1 
            
    except ValueError:
        print("Entrada inválida. Por favor, ingresa solo un número entero.")
        continue 
    
print(f"Números pares: {num_pares}")
print(f"Números impares: {num_impares}")
print(f"Números positivos: {num_positivos}")
print(f"Números negativos: {num_negativos}")


"""9)Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

suma_total= 0
cantidad_numeros= 100

for i in range(cantidad_numeros):
    try:
        numero = int(input(f"Ingresa el número {i+1} de {cantidad_numeros}: "))
        suma_total += numero
        
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero: ")
        continue

media = suma_total / cantidad_numeros
print(f"La media de los números ingresados es: {media}")


"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero_ingresado = input("Ingresar un número para invertir: ")

numero_invertido = numero_ingresado[::-1]

print(f"El número invertido es: {numero_invertido}")









