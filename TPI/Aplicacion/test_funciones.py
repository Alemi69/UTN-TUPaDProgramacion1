from funciones import * 

# --- Ruta al archivo CSV ---
# Opción 1 (recomendada): ruta relativa
#ruta = "paises_mundo_2023.csv"

# Opción 2 (si el archivo está en otra carpeta)
ruta = "TPI/Aplicacion/paises_mundo_2023.csv"

# --- Leemos los datos ---
paises = leer_csv(ruta)
"""
# --- Mostramos los datos en crudo ---
print("\n=== CONTENIDO DEL ARCHIVO EN CRUDO ===\n")
if paises:
    for pais in paises:
        print(pais)
else:
    print(paises)
"""
nombre = "Argentina"
resu = buscar_pais(paises, nombre)

print(resu)
