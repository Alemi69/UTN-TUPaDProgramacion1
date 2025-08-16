"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos,
dividirlos, multiplicarlos y restarlos."""

numero1=int(input("Ingresa primer numero entero, distinto de cero: "))
numero2=int(input("Ingresa segundo numero entero, distinto de cero: "))

suma= numero1 + numero2
resta=numero1 - numero2
multiplicacion=numero1 * numero2
division=numero1 / numero2

print(f"El resultado de {numero1} + {numero2}= {suma}")
print(f"El resultado de {numero1} - {numero2}= {resta}")
print(f"El resultado de {numero1} * {numero2}= {multiplicacion}")
print(f"El resultado de {numero1} / {numero2}= {division}")






