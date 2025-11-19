import os

nombre_archivo = "productos.txt"
lista_productos = [] 

print("--- INICIO DEL PROGRAMA ---\n")

if os.path.exists(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        print("Leyendo productos existentes...")
        for linea in archivo:
            datos = linea.strip().split(",")
            
            producto = {
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2])  
            }
            
            lista_productos.append(producto)
        print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
else:
    print(f"El archivo {nombre_archivo} no existe. Se creará uno nuevo al guardar.")

print("\n" + "-"*30 + "\n")

print("--- AGREGAR NUEVO PRODUCTO ---")
nombre_nuevo = input("Ingrese nombre del producto: ")
precio_nuevo = float(input("Ingrese precio: "))
cant_nuevo = int(input("Ingrese cantidad: "))

nuevo_producto = {
    "nombre": nombre_nuevo,
    "precio": precio_nuevo,
    "cantidad": cant_nuevo
}

lista_productos.append(nuevo_producto)
print("¡Producto agregado a la lista!")

print("\n" + "-"*30 + "\n")

print("--- BUSCAR PRODUCTO ---")
busqueda = input("Ingrese el nombre del producto a buscar: ")
encontrado = False

for prod in lista_productos:
    if prod["nombre"].lower() == busqueda.lower():
        print(f"¡ENCONTRADO! -> Nombre: {prod['nombre']}, Precio: ${prod['precio']}, Stock: {prod['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: El producto no existe en la lista.")

print("\n" + "-"*30 + "\n")

with open(nombre_archivo, "w") as archivo:
    for prod in lista_productos:
        linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n"
        archivo.write(linea)

print(f"--- Archivo {nombre_archivo} actualizado correctamente ---")