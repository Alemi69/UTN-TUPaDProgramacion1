"""1)Crear una lista con las notas de 10 estudiantes.
Mostrar la lista completa.
Calcular y mostrar el promedio.
Indicar la nota más alta y la más baja."""

notas=[8,7,9,6.50,10,5,4,9,8,8.50]
print("La lista de notas de los 10 estudiantes: ")

for nota in notas:#toma el primer elemento 8 lo asigna a nota, luego imprime...
    print(nota, end= ",")
    
promedio = sum(notas) / len(notas)
print()
print(f"El promedio de las notas es: {promedio}")

nota_mas_alta =max(notas)
nota_mas_baja =min(notas)
print(f"La nota mas alta es: {nota_mas_alta}")
print(f"La nota mas baja es: {nota_mas_baja}")

"""2)
Pedir al usuario que cargue 5 productos en una lista.
Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
Preguntar al usuario qué producto desea eliminar y actualizar la lista."""

productos=["pan","leche","queso","manteca"]
productos_ordenados = sorted(productos) # sorted()=ordenado
print(productos_ordenados)

producto_a_eliminar=input("Ingresa que producto deseas eliminar: ")

if producto_a_eliminar in productos:
    productos.remove(producto_a_eliminar)
    print(f"El producto a eliminar es: {producto_a_eliminar}")
else:
    print(f"Ese producto no existe en la lista, por favor elige otro!")
    
print(f"Lista de productos actualizada.{productos}")


"""3)
Generar una lista con 15 números enteros al azar entre 1 y 100.
Crear una lista con los pares y otra con los impares.
Mostrar cuántos números tiene cada lista."""

import random # para generar numeros al azar

numeros=[]

for contador in range(15): #bucle for para generar 15 numeros
    numeros.append(random.randint(1,100)) #append para añadir elementos a una lista
print(f"Lista de numeros generados al azar: {numeros}")

num_pares=[] #lista para los numeros pares
num_impares=[]

for numero in numeros:
    if numero %2 == 0:
        num_pares.append(numero)
    else:
        num_impares.append(numero)

print(f"Lista de los numeros pares: {num_pares}")
print(f"Lista de los numeros impares: {num_impares}")

print(f"La cantidad de numeros pares es: {len(num_pares)}")
print(f"La cantidad de numeros impares es: {len(num_impares)}")


"""4)
Dada una lista con valores repetidos: datos=[1,3,5,3,7,1,9,5,3]
Crear una nueva lista sin elementos repetidos.
Mostrar el resultado."""

lista_original=[1,3,5,3,7,1,9,5,3]

lista_sin_duplicados=[]

for numero in lista_original:
    if numero not in lista_sin_duplicados:
        lista_sin_duplicados.append(numero)

print(f"Lista original: {lista_original}")
print(f"Lista sin los numeros duplicados: {lista_sin_duplicados}")

"""5)
Crear una lista con los nombres de 8 estudiantes presentes en clase.
Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
Mostrar la lista final actualizada."""

lista_estudiantes=["Emilia", "Juan", "Alejandro", "Julio", "Maria", "Lucas", "Andres", "Andrea"]

eleccion=input("¿Desea agregar un nuevo estudiante o eliminar uno existente? Escriba 'agregar' o 'eliminar': ").lower()

if eleccion == "agregar":  # Lógica para decidir qué acción tomar.
    nuevo_estudiante = input("Escriba el nombre del nuevo estudiante: ")
    lista_estudiantes.append(nuevo_estudiante)
    print(f"'{nuevo_estudiante}' ha sido agregado a la lista.")
elif eleccion == "eliminar":
    estudiante_a_eliminar = input("Escriba el nombre del estudiante a eliminar: ")
    if estudiante_a_eliminar in lista_estudiantes:
        lista_estudiantes.remove(estudiante_a_eliminar)
        print(f"'{estudiante_a_eliminar}' ha sido eliminado de la lista.")
    else:
        print(f"'{estudiante_a_eliminar}' no se encuentra en la lista.")
else:
    print("Nombre no valido.")

print("Lista final actualizada de estudiantes:")  # Mostrar la lista final actualizada usando una estructura repetitiva (for).
for i in range(len(lista_estudiantes)):
    print(f"El elemento en la posición {i} es {lista_estudiantes[i]}")
    
    
"""6)
Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero)."""

lista_numeros = [1, 2, 3, 4, 5, 6, 7]

for numero in lista_numeros:
    print(numero, end=",")
    
print()

ultimo_elemento = lista_numeros[-1]

lista_numeros.pop()

lista_numeros.insert(0, ultimo_elemento) 
print(f"La lista con el nuevo orden es: {lista_numeros}")


"""7)
Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
Calcular el promedio de las mínimas y el de las máximas.
Mostrar en qué día se registró la mayor amplitud térmica."""

temperaturas = [
    [10, 22],  # Lunes
    [12, 25],  # Martes
    [8, 18],   # Miércoles
    [11, 23],  # Jueves
    [15, 28],  # Viernes
    [13, 26],  # Sábado
    [9, 20]    # Domingo
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

sum_minimas = 0
sum_maximas = 0
num_dias = len(temperaturas) 

for dia in temperaturas:
    sum_minimas += dia[0]  
    sum_maximas += dia[1] 

promedio_minimas = sum_minimas / num_dias
promedio_maximas = sum_maximas / num_dias

print(f"El promedio de las temperaturas mínimas es: {promedio_minimas:.2f}°C")
print(f"El promedio de las temperaturas máximas es: {promedio_maximas:.2f}°C")


"""8)
Crear una matriz con las notas de 5 estudiantes en 3 materias.
Mostrar el promedio de cada estudiante.
Mostrar el promedio de cada materia."""


notas = [
    [10, 8, 9],   # Notas del Estudiante 1
    [7, 8, 6],    # Notas del Estudiante 2
    [8, 5, 9],    # Notas del Estudiante 3
    [10, 6, 9],   # Notas del Estudiante 4
    [4, 8, 6],    # Notas del Estudiante 5
]

print("--- Promedio de cada estudiante ---")
num_estudiantes = len(notas) 
num_materias = len(notas[0]) 

for i in range(num_estudiantes):
    promedio_estudiante = sum(notas[i]) / num_materias
    print(f"Estudiante {i+1}: {promedio_estudiante:.2f}")

print("\n--- Promedio de cada materia ---")

for j in range(num_materias):
    suma_materia = 0
    
    for i in range(num_estudiantes):
        suma_materia += notas[i][j]   
    promedio_materia = suma_materia / num_estudiantes
    print(f"Materia {j+1}: {promedio_materia:.2f}")


"""9)Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
Inicializarlo con guiones "-" representando casillas vacías.
Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
Mostrar el tablero después de cada jugada."""

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero():
    print("\n--- TABLERO ---")
    for fila in tablero:
        print(" ".join(fila)) 
    print("---------------")

for jugada in range(9):
    jugador = "X" if jugada % 2 == 0 else "O"

    mostrar_tablero()
    print(f"Turno del jugador '{jugador}'.")

    while True:
        try:
            fila = int(input("Ingresa la fila (0, 1, 2): "))
            columna = int(input("Ingresa la columna (0, 1, 2): "))

            if 0 <= fila < 3 and 0 <= columna < 3:
                if tablero[fila][columna] == "-":
                    break
                else:
                    print("Esa casilla ya está ocupada. Intenta de nuevo.")
            else:
                print("Posición fuera del rango. Ingresa valores entre 0 y 2.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números enteros.")
            
    tablero[fila][columna] = jugador

"""10)
Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
Mostrar el total vendido por cada producto.
Mostrar el día con mayores ventas totales.
Indicar cuál fue el producto más vendido en la semana."""


ventas = [
    [10, 15, 20, 12, 18, 25, 22],  # Ventas del Producto 1
    [8, 11, 14, 16, 10, 19, 21],   # Ventas del Producto 2
    [5, 9, 13, 11, 15, 17, 10],    # Ventas del Producto 3
    [12, 8, 18, 20, 14, 23, 15]    # Ventas del Producto 4
]


print("--- Total vendido por cada producto ---")
num_productos = len(ventas)
for i in range(num_productos):
    total_producto = sum(ventas[i])
    print(f"Producto {i+1}: {total_producto} unidades vendidas")

print("\n--- Día con mayores ventas totales ---")
num_dias = len(ventas[0])
ventas_diarias = []

for j in range(num_dias):
    suma_dia = 0
    for i in range(num_productos):
        suma_dia += ventas[i][j]
    ventas_diarias.append(suma_dia)

dia_mas_vendido_index = ventas_diarias.index(max(ventas_diarias))
print(f"El día con mayores ventas totales fue el día {dia_mas_vendido_index + 1} con {max(ventas_diarias)} unidades")

print("\n--- Producto más vendido en la semana ---")
ventas_totales_productos = []

for i in range(num_productos):
    total_producto = sum(ventas[i])
    ventas_totales_productos.append(total_producto)

producto_mas_vendido_index = ventas_totales_productos.index(max(ventas_totales_productos))
print(f"El producto más vendido en la semana fue el Producto {producto_mas_vendido_index + 1} con {max(ventas_totales_productos)} unidades vendidas")