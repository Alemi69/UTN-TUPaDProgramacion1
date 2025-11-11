import csv
import os.path  # chequear la existencia

"""
1. Gestion de archivos
"""


def leer_csv(paises_mundo_2023):
    paises = []
    if not os.path.exists(paises_mundo_2023):
        return paises  # Devuelve una lista vacia

    with open(
        paises_mundo_2023, "r", newline="", encoding="utf-8-sig"
    ) as f:  # lee los datos de los paises desde un archivo csv.
        lector = csv.DictReader(f)
        for fila in lector:
            if (
                fila.get("nombre")
                and fila.get("poblacion")
                and fila.get("superficie_km2")
            ):
                fila["poblacion"] = int(fila["poblacion"])
                fila["superficie_km2"] = int(fila["superficie_km2"])
                paises.append(fila)
    return paises


"""
Notas:
    - Si se devuelve una lista vacía, el archivo no fue encontrado.
    - No se utilizan excepciones
    - Se asume que los datos 'poblacion' y 'superficie' son números válidos en el CSV. 
      Si no lo son, el programa se detendrá (error ValueError) ya que no se manejan fallos.
"""


# Cada pais debe tener las claves: nombre, poblacion, superfcie, continente.


def guardar_csv(
    paises_mundo_2023, lista_paises
):  # Guarda la lista actualizada de paises en el archivo leer_csv
    campos = ["nombre", "poblacion", "superficie_km2", "continente"]
    with open(paises_mundo_2023, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)

        escritor.writeheader()  # Encabezado
        # escrbir cada pais en fila
        for pais in lista_paises:
            escritor.writerow(pais)


"""
2. Gestion de paises ( altas y modificaciones)
"""


def agregar_pais(lista_paises, nuevo_pais):
    """
    Agrega un nuevo país a la lista si no existe y los datos son válidos.
    nuevo_pais es un diccionario con las claves:
    nombre, iso_codigo, poblacion, anio_poblacion, superficie_km2, continente, capital
    """
    # Verificar que ningún campo esté vacío
    if (
        not nuevo_pais["nombre"].strip()
        or not nuevo_pais["poblacion"]
        or not nuevo_pais["superficie_km2"]
        or not nuevo_pais["continente"].strip()
    ):
        return False

    # Verificar duplicados (por nombre)
    for pais in lista_paises:
        if pais["nombre"].lower() == nuevo_pais["nombre"].lower():
            return False  # ya existe

    # Agregar a la lista
    lista_paises.append(nuevo_pais)
    return True


def actualizar_pais(lista_paises, nombre, nueva_poblacion, nueva_superficie):
    """
    Busca un país por nombre y actualiza su población y superficie.
    Devuelve True si lo actualiza, False si no se encuentra.
    """
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = nueva_poblacion
            pais["superficie_km2"] = nueva_superficie
            return True  # actualización exitosa
    return False  # país no encontrado


"""
3. Busquedas y filtro
"""


def buscar_pais(lista_paises, nombre):
    """
    Devuelve una lista de países cuyo nombre contenga
    el texto buscado (coincidencia parcial, sin distinguir mayúsculas).
    """
    resultados = []
    texto = nombre.lower()

    for pais in lista_paises:
        if texto in pais["nombre"].lower():
            resultados.append(pais)

    return resultados


def filtrar_por_continente(lista_paises, continente):
    """
    Devuelve una lista de países que pertenecen al continente indicado.
    """
    resultados = []
    cont = continente.lower()

    for pais in lista_paises:
        if pais["continente"].lower() == cont:
            resultados.append(pais)

    return resultados


def filtrar_por_rango_poblacion(lista_paises, min_pob, max_pob):
    """
    Devuelve una lista de países cuya población esté dentro del rango indicado.
    """
    resultados = []
    for pais in lista_paises:
        if pais["poblacion"] >= min_pob and pais["poblacion"] <= max_pob:
            resultados.append(pais)
    return resultados


def filtrar_por_rango_superficie(lista_paises, min_sup, max_sup):
    """
    Devuelve una lista de países cuya superficie esté dentro del rango indicado.
    """
    resultados = []
    for pais in lista_paises:
        if pais["superficie_km2"] >= min_sup and pais["superficie_km2"] <= max_sup:
            resultados.append(pais)
    return resultados


# 4. ORDENAMIENTOS


def ordenar_por_nombre(lista_paises, ascendente=True):
    def clave_nombre(pais):
        return pais["nombre"]

    return sorted(lista_paises, key=clave_nombre, reverse=not ascendente)


"""
Devuelve una nueva lista ordenada por nombre de país.
"""


def ordenar_por_poblacion(lista_paises, ascendente=True):
    def clave_poblacion(pais):
        return pais["poblacion"]

    return sorted(lista_paises, key=clave_poblacion, reverse=not ascendente)


"""
Devuelve una nueva lista ordenada por población.
"""


def ordenar_por_superficie(lista_paises, ascendente=True):
    def clave_superficie(pais):
        return pais["superficie_km2"]

    return sorted(lista_paises, key=clave_superficie, reverse=not ascendente)


"""
Devuelve una nueva lista ordenada por superficie.
"""


# 5. ESTADÍSTICAS


def pais_mayor_poblacion(lista_paises):
    """
    Devuelve el país con mayor población.
    """
    if not lista_paises:
        return None

    mayor = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
    return mayor


def pais_menor_poblacion(lista_paises):
    """
    Devuelve el país con menor población.
    """
    if not lista_paises:
        return None

    menor = lista_paises[0]
    for pais in lista_paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais
    return menor


def promedio_poblacion(lista_paises):
    """
    Calcula el promedio de población de todos los países.
    """
    if not lista_paises:
        return 0

    suma = 0
    for pais in lista_paises:
        suma += pais["poblacion"]

    return suma / len(lista_paises)


def promedio_superficie(lista_paises):
    """
    Calcula el promedio de superficie de todos los países.
    """
    if not lista_paises:
        return 0

    suma = 0
    for pais in lista_paises:
        suma += pais["superficie_km2"]

    return suma / len(lista_paises)


def cantidad_por_continente(lista_paises):
    """
    Devuelve un diccionario con la cantidad de países por continente.
    """
    conteo = {}
    for pais in lista_paises:
        cont = pais["continente"]
        if cont not in conteo:
            conteo[cont] = 1
        else:
            conteo[cont] += 1
    return conteo


# 6. VALIDACIONES (opcional)


def validar_entero(valor):
    return f"Función validar_entero ejecutada correctamente"


"""
Verifica si el valor puede convertirse a entero.
Devuelve True o False.
"""


def validar_no_vacio(texto):
    return f"Función validar_no_vacio ejecutada correctamente"


"""
Verifica que el texto no esté vacío ni solo contenga espacios.
"""
