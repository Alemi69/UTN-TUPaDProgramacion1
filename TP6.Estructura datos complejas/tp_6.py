"""1) Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""
precios_frutas = {"Banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

"""2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""
precios_frutas = {"Banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melon"] = 2800
print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
    crear una lista que contenga únicamente las frutas sin los precios.
"""

precios_frutas = {"Banana":1200, "Anana":2500, "Melon":3000, "Uva":1450}

lista_productos = list(precios_frutas.keys())
print(lista_productos)

"""4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""
contactos = {"Pedro":1147896537, "Paco":1145689865, "Emi":1125891254, "Lujan":1145679632, "Mati":1156587433}

nombre_solicitado = input("Ingresa el nombre a buscar: ")

if nombre_solicitado in contactos:
    numero_asociado = contactos[nombre_solicitado]
    print(f"El numero de: {nombre_solicitado} es: {numero_asociado}")
else:
    print(f"El nombre buscado no existe en la lista de contactos.")
    

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingresa una frase: ")

lista_palabras = frase.lower().split()

palabras_unicas = set(lista_palabras)

print("\n--- Resultado ---")
print(f"Palabras únicas: {palabras_unicas}")

conteo_palabras = {}

for palabra in lista_palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(f"Recuento: {conteo_palabras}")


"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno.
"""
alumnos = {
    "Juan": (10, 8, 6),
    "Emilia": (8, 7, 9),
    "Marcos": (7, 6, 9)
}

for nombre, notas in alumnos.items():
    suma_notas = sum(notas)
    
    cantidad_notas = len(notas)
    
    promedio = suma_notas / cantidad_notas
    
    print(f"El promedio de {nombre} es: {promedio}")
    
"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

aprobados_parcial1 = {101, 105, 110, 115, 125}
aprobados_parcial2 = {105, 115, 120, 135, 140}

ambos_aprobados = aprobados_parcial1 & aprobados_parcial2

print("1. Aprobaron AMBOS parciales (Intersección):")
print(ambos_aprobados)

alguno_aprobado = aprobados_parcial1 | aprobados_parcial2

print("\n2. Lista total que aprobaron al menos un parcial (Unión):")
print(alguno_aprobado)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2

print("\n3. Aprobaron SOLO uno de los dos (Diferencia Simétrica):")
print(solo_uno)


"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""
articulos = {"Fideos": 500 , "Aceite": 850, "Harina": 480, "Manteca": 540, "Galletitas": 274, "Arroz":210}

producto_solicitado = input("Ingresa el nombre del producto: ")

if producto_solicitado in articulos:
    stock_actual = articulos[producto_solicitado]
    print(f"Stock actual de {producto_solicitado}: {stock_actual}")
    
    unidades_a_agregar = int(input("¿Cuántas unidades desea agregar? "))
    articulos[producto_solicitado] += unidades_a_agregar 
    
    print(f"Nuevo stock: {articulos[producto_solicitado]}")
else:    
    print(f"El producto '{producto_solicitado}' no está en inventario.")
    respuesta = input("¿Desea agregarlo como nuevo? (s/n): ")
    
    if respuesta == 's':
        stock_inicial = int(input("Ingrese stock inicial: "))
        articulos[producto_solicitado] = stock_inicial 
        print(f"Producto '{producto_solicitado}' agregado con éxito.")

print("\nInventario Final:", articulos)


"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
"""

agenda = {
    ("Lunes", 6): "Reunión",
    ("Lunes", 13): "Clase de Matematica",
    ("Martes",21): "Clase de Python",
    ("Jueves", 23): "Turno control medico",
    ("Viernes", 31): "Tarde de futbol"
}

clave_a_consultar = ("Lunes", 6)
print(f"Evento del {clave_a_consultar}: {agenda[clave_a_consultar]}")

agenda[("Martes", 14)] = "Cena familiar"
print("\nEvento añadido con éxito.")

print("\n--- Agenda Completa ---")
print(agenda)


"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

paises_y_capitales = {"Buenos Aires": "Argentina", "Brasilia":"Brasil", "Roma": "Italia", "Berlin":"Alemania"}

capitales_y_paises = {}

for capital, pais in paises_y_capitales.items():
    
    capitales_y_paises[pais] = capital

print("--- Diccionario Invertido ---")
print(capitales_y_paises)






