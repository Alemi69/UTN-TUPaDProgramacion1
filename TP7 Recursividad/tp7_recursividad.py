# factorial
def calcular_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

# fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# decimal a binario
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        div = n // 2
        resto = n % 2
        return decimal_a_binario(div) + str(resto)

# palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    primera = palabra[0]
    ultima = palabra[-1]
    
    if primera != ultima:
        return False
    else:
        nueva_palabra = palabra[1:-1]
        return es_palindromo(nueva_palabra)

# suma de digitos 
def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto = n // 10
        return ultimo + suma_digitos(resto)

# contar bloques de la piramide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# contar cuantas veces aparece un digito
def contar_digito(numero, digito_buscado):
    if numero == 0:
        return 0
    
    ultimo = numero % 10

    if ultimo == digito_buscado:
        sumar = 1
    else:
        sumar = 0
        
    resto_del_numero = numero // 10
    return sumar + contar_digito(resto_del_numero, digito_buscado)

# --- PRUEBAS DE LOS EJERCICIOS ---

print("--- Ejercicio 1: Factorial ---")
numero = int(input("Ingresa un numero para el factorial: "))

for i in range(1, numero + 1):
    print("Factorial de", i, "es:", calcular_factorial(i))

print("\n--- Ejercicio 2: Fibonacci ---")
cantidad = int(input("Cuantos numeros de Fibonacci querés ver?: "))
for i in range(cantidad + 1):
    print(fibonacci(i), end=" ")
print() 

print("\n--- Ejercicio 3: Potencia ---")
print("2 elevado a 3 es:", potencia(2, 3))

print("\n--- Ejercicio 4: Binario ---")
print("10 en binario:", decimal_a_binario(10))
print("13 en binario:", decimal_a_binario(13))

print("\n--- Ejercicio 5: Palindromo ---")
print("neuquen es palindromo?:", es_palindromo("neuquen"))
print("auto es palindromo?:", es_palindromo("auto"))

print("\n--- Ejercicio 6: Suma de digitos ---")
print("Suma de 1234:", suma_digitos(1234))

print("\n--- Ejercicio 7: Piramide ---")
print("Bloques para altura 4:", contar_bloques(4))

print("\n--- Ejercicio 8: Contar digito ---")
print("El 2 aparece en 12233421:", contar_digito(12233421, 2), "veces")

input("\nPresiona Enter para terminar...")