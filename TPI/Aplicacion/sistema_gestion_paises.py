from funciones import *

def mostrar_menu():
    """
    Imprime el menú principal de opciones en la consola.
    """
    print("\n*********************************")
    print(" Sistema de Gestión de Países")
    print("***********************************")
    print("1. Buscar un país por nombre")
    print("2. Filtrar países (por continente, población, etc.)")
    print("3. Ordenar países (por nombre, población, etc.)")
    print("4. Mostrar estadísticas")
    print("5. Salir del programa")
    print("----------------------------------------")

def mostrar_paises(lista_de_paises):
    """
    Recibe una lista de países y la imprime de forma clara.
    También maneja el caso de que la lista esté vacía (búsqueda sin resultados).
    """
    if not lista_de_paises:
        print("No se encontraron países que cumplan con el criterio.")
        return

    print(f"\nPaíses encontrados ({len(lista_de_paises)}):")
    for pais in lista_de_paises:
        print(f"  - Nombre: {pais['nombre']}")
        print(f"    Continente: {pais['continente']}")
        print(f"    Población: {pais['poblacion']}")
        
        print(f"    Superficie: {pais['superficie_km2']} km²") 
        
        print("  ---")

def opcion_1_buscar_pais(paises):
    """
    Opción 1: Pide al usuario un nombre y busca países que coincidan.
    Luego, muestra los resultados llamando a mostrar_paises().
    """
    print("\n--- Opción 1: Buscar País ---")
    nombre_buscado = input("Ingrese el nombre (o parte del nombre) del país: ").strip()
    resultados_encontrados = buscar_pais(paises, nombre_buscado) 
    
    mostrar_paises(resultados_encontrados)

def opcion_2_filtrar_paises(paises):
    """
    Opción 2: Muestra un sub-menú para filtrar países.
    Llama a las funciones de filtrado correspondientes.
    """
    print("\n--- Opción 2: Filtrar Países ---")
    
    while True:
        print("\n¿Por qué criterio desea filtrar?")
        print("A. Por Continente")
        print("B. Por Rango de Población")
        print("C. Por Rango de Superficie_km²")
        print("D. Volver al menú principal")
        
        sub_opcion = input("Seleccione una opción (A-D): ").strip().upper() 

        if sub_opcion == "A":
            continente = input("Ingrese el nombre del continente: ").strip()
            
            resultados = filtrar_por_continente(paises, continente)
            
            mostrar_paises(resultados)
        
        elif sub_opcion == "B":
            print("Ingrese el rango de población:")
            
            min_pob_str = input("Población mínima: ").strip()
            max_pob_str = input("Población máxima: ").strip()

            if not min_pob_str.isdigit() or not max_pob_str.isdigit():
                print("Error: Ingrese solo números para la población.")
                continue 

            min_pob = int(min_pob_str)
            max_pob = int(max_pob_str)
            
            resultados = filtrar_por_rango_poblacion(paises, min_pob, max_pob)
            
            mostrar_paises(resultados)

        elif sub_opcion == "C":
            print("Ingrese el rango de superficie (en km²):")
            
            min_sup_str = input("Superficie mínima: ").strip()
            max_sup_str = input("Superficie máxima: ").strip()

            if not min_sup_str.isdigit() or not max_sup_str.isdigit():
                print("Error: Ingrese solo números para la superficie.")
                continue

            min_sup = int(min_sup_str)
            max_sup = int(max_sup_str)

            resultados = filtrar_por_rango_superficie(paises, min_sup, max_sup)
            
            mostrar_paises(resultados)
            
        elif sub_opcion == "D":
            print("Volviendo al menú principal...")
            break 
        else:
            print("Error: Opción no válida. Intente de nuevo (A-D).")

def opcion_3_ordenar_países(paises):
    """
    Opción 3: Muestra un sub-menú para ordenar la lista de países.
    Llama a la función de ordenamiento correspondiente.
    """
    print("\n--- Opción 3: Ordenar Países ---")
    
    while True:
        print("\n¿Por qué criterio desea ordenar?")
        print("A. Por Nombre")
        print("B. Por Población")
        print("C. Por Superficie")
        print("D. Volver al menú principal")
        
        sub_opcion = input("Seleccione una opción (A-D): ").strip().upper()
        
        if sub_opcion == "D":
            print("Volviendo al menú principal...")
            break 
        
        print("\n¿En qué orden?")
        print("1. Ascendente (A-Z, menor a mayor)")
        print("2. Descendente (Z-A, mayor a menor)")
        
        orden = input("Seleccione el orden (1-2): ").strip()
        
        es_ascendente = True 
        
        if orden == "1":
            es_ascendente = True
        elif orden == "2":
            es_ascendente = False
        else:
            print("Error: Orden no válido. Debe ser '1' o '2'.")
            continue 

        # Creamos la variable de resultados
        resultados = []

        if sub_opcion == "A":
            resultados = ordenar_por_nombre(paises, es_ascendente)
        elif sub_opcion == "B":
            resultados = ordenar_por_poblacion(paises, es_ascendente)
        elif sub_opcion == "C":
            # Esta función usa 'superficie_km2' internamente
            resultados = ordenar_por_superficie(paises, es_ascendente) 
        else:
            print("Error: Opción no válida. Intente de nuevo (A-D).")
            continue 
        
        orden_texto = "Ascendente" if es_ascendente else "Descendente"
        print(f"\nResultados ordenados ({orden_texto}):")
        mostrar_paises(resultados)

def opcion_4_mostrar_estadisticas(paises):
    """
    Opción 4: Llama a todas las funciones de estadísticas
    y muestra los resultados en la terminal.
    """
    print("\n--- Opción 4: Estadísticas Globales ---")

    if not paises:
        print("No hay datos de países cargados para mostrar estadísticas.")
        return

    pais_max = pais_mayor_poblacion(paises)
    pais_min = pais_menor_poblacion(paises)
    prom_pob = promedio_poblacion(paises)
    prom_sup = promedio_superficie(paises)
    conteo_continentes = cantidad_por_continente(paises)

    # --- 2. IMPRIMIMOS LOS RESULTADOS ---
    print("\n--- Estadísticas de Población ---")
    print(f"País con MAYOR población: {pais_max}")
    print(f"País con MENOR población: {pais_min}")
    print(f"Promedio de población: {prom_pob}")

    print("\n--- Estadísticas de Superficie ---")
    print(f"Promedio de superficie: {prom_sup}")
    print("\n--- Conteo por Continente ---")

    if isinstance(conteo_continentes, dict):
        for continente, cantidad in conteo_continentes.items():
            print(f"  - {continente}: {cantidad} país(es)")
    else:
        print(conteo_continentes)

def main():
    """
    Función principal del programa.
    Carga los datos e inicia el bucle principal del menú.
    """
    
    ruta_del_archivo = 'TPI/Aplicacion/paises_mundo_2023.csv'
    
    lista_paises = leer_csv(ruta_del_archivo) 
    
    if not lista_paises:
        print(f"Error: No se pudo cargar el archivo '{ruta_del_archivo}' o está vacío.")
        print("Saliendo del programa.")
        return 
    
    print(f"¡Bienvenido! Se cargaron {len(lista_paises)} países desde el archivo.")

    while True:
        mostrar_menu()
        
        opcion_usuario = input("Por favor, seleccione una opción (1-5): ").strip()
        
        if opcion_usuario == "1":
            # Llamamos a la función de la Opción 1
            opcion_1_buscar_pais(lista_paises)
        
        elif opcion_usuario == "2":
            # Llamamos a la función de la Opción 2
            opcion_2_filtrar_paises(lista_paises)
            
        elif opcion_usuario == "3":
            # Llamamos a la función de la Opción 3
            opcion_3_ordenar_países(lista_paises)
            
        elif opcion_usuario == "4":
            # Llamamos a la función de la Opción 4
            opcion_4_mostrar_estadisticas(lista_paises)
            
        elif opcion_usuario == "5":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break   
        else:
            # Validación de menú principal (consigna 3)
            print("\nError: Opción no válida.")
            print("Por favor, ingrese solo un número del 1 al 5.")

# Esta construcción de Python se asegura de que la función
# main() solo se llame cuando el archivo se ejecuta directamente.
if __name__ == "__main__":
    main()