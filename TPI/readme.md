<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Estado-Completado-success" alt="Estado Badge">
  <img src="https://img.shields.io/badge/Licencia-Académica-lightgrey" alt="Licencia Badge">
</p>

<h1 align="center"> Sistema de Gestión de Países</h1>

**Trabajo Práctico Integrador (TPI) - Programación 1**

Este proyecto es un sistema de consola desarrollado en Python que permite gestionar, filtrar, ordenar y analizar datos de países cargados desde un archivo CSV.


**Tecnologías y conceptos aplicados**

- **Estructuras:** Listas y Diccionarios
- **Persistencia de datos:** Archivos CSV
- **Paradigma:** Programación estructurada
- **Validaciones:** Control de entrada de usuario
- **Módulos:** CSV, OS
- **Fuente bibliográfica:** CURSO INTENSIVO DE PYTHON 3ªEDICIÓN Introducción práctica a la programación basada en proyectos Eric Matthes (Editorial Anaya MULTIMEDIA)

**Tabla de Contenidos**
- [Diagrama de flujo](#diagrama-de-flujo)
- [Descripcion](#descripcion)
- [Instrucciones de uso ](#instalacion-y-ejecucion)
- [Participacion de los integrantes](#integrantes-y-roles)
- [Descarga del proyecto](https://github.com/Arcademys/UTN-TUPaDProgramacion1/raw/refs/heads/main/TPI/Aplicacion/Proyecto_completo.rar)
---

## [Diagrama de flujo](#-Diagrama-de-flujo)



```mermaid
flowchart TD
    A([Inicio del programa]) --> B[Leer archivo CSV con leer_csv]
    B --> C{Archivo existe?}
    C -->|No| D[Crear lista vacia de paises]
    C -->|Si| E[Cargar lista de paises desde el CSV]
    E --> F[Mostrar menu principal]

    F --> G[1 Buscar pais por nombre]
    F --> H[2 Filtrar paises]
    F --> I[3 Ordenar paises]
    F --> J[4 Mostrar estadisticas]
    F --> K[5 Salir]

    G --> L[Usa buscar_pais]
    L --> M[Mostrar resultados en consola]
    M --> F

    H --> H1{Criterio de filtro}
    H1 -->|Continente| H2[Usa filtrar_por_continente]
    H1 -->|Poblacion| H3[Usa filtrar_por_rango_poblacion]
    H1 -->|Superficie| H4[Usa filtrar_por_rango_superficie]
    H2 --> M
    H3 --> M
    H4 --> M

    I --> I1{Criterio de ordenamiento}
    I1 -->|Nombre| I2[Usa ordenar_por_nombre]
    I1 -->|Poblacion| I3[Usa ordenar_por_poblacion]
    I1 -->|Superficie| I4[Usa ordenar_por_superficie]
    I2 --> M
    I3 --> M
    I4 --> M

    J --> J1[Usa funciones estadisticas]
    J1 --> J2[pais_mayor_poblacion y pais_menor_poblacion]
    J2 --> J3[promedio_poblacion y promedio_superficie]
    J3 --> J4[cantidad_por_continente]
    J4 --> M

    K --> N[Guardar cambios con guardar_csv]
    N --> O([Fin del programa])


```

---

## [Descripcion](#descrpcion)
El presente Trabajo Práctico Integrador (TPI) consiste en el desarrollo de una aplicación de consola en Python diseñada para la gestión y análisis de datos geográficos y demográficos. El objetivo principal del proyecto fue crear un sistema capaz de leer una base de datos externa (en formato CSV) y ofrecer al usuario una interfaz interactiva para explorar esa información.

A través de un menú de opciones, el sistema permite realizar búsquedas específicas de países, aplicar filtros por diversos criterios (continente, población, superficie), ordenar los resultados y visualizar estadísticas globales. Este proyecto nos permitió integrar y aplicar los conceptos fundamentales de la estructura de programación, tales como el manejo de estructuras de datos complejas (listas de diccionarios), la modularización mediante funciones y el uso de control de flujo para la interacción con el usuario.


---

## [Instalacion y Ejecucion](#instalacion-y-ejecucion)

Para ejecutar este proyecto, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Arcademys/UTN-TUPaDProgramacion1.git](https://github.com/Arcademys/UTN-TUPaDProgramacion1.git)
    ```
2.  **Navegar a la carpeta de la aplicación:**
    ```bash
    cd UTN-TUPaDProgramacion1/TPI/Aplicacion
    ```
3.  **Ejecutar el programa:**
    ```bash
    python sistema_gestion_países.py
    ```

O descarga de forma directa el proyecto completo, podés descargar todos los archivos necesarios ( `funciones.py`, `sistema_gestion_paises.py` y `paises_mundo_2023.csv`) en un solo paquete comprimido desde el siguiente enlace: [Descargar Proyecto Completo .rar](https://github.com/Arcademys/UTN-TUPaDProgramacion1/raw/refs/heads/main/TPI/Aplicacion/Proyecto_completo.rar)

---

## Funcionalidades

**Menú Principal**
![Menú Principal](menu_principal.jpg)

**1. Buscar País**
Permite buscar un país por su nombre exacto o parcial.
*(Ejemplo: Buscar "arg" encuentra "Argentina").*

![Ejemplo de Búsqueda](busqueda.jpg)

**2. Filtrar Países**
Sub-menú para filtrar la lista completa por:
* **Continente** (ej. "América del Sur")
* **Rango de Población** (mínimo y máximo)
* **Rango de Superficie** (mínimo y máximo)

![Ejemplo de Filtro](filtro.jpg)

**3. Ordenar Lista**
Permite reordenar los países ascendente o descendentemente por:
* Nombre
* Población
* Superficie

**4. Estadísticas**
Muestra cálculos automáticos sobre los datos actuales:
* País con mayor/menor población.
* Promedios de población y superficie.
* Cantidad de países por continente.

![Ejemplo de Estadísticas](estadisticas.jpg)

---

##  Integrantes y Roles

* **Enrique Alejandro Carrasco:** Desarrollo de la interfaz de terminal (menús, validaciones, interacción con el usuario).
* **Juan José Benitez:** Desarrollo del archivo `funciones.py`, manejo de archivos CSV, filtrado, ordenamiento y estadísticas.

---

<h6 align="center"> *Proyecto realizado para la materia Programación I (UTN 2025).*</h6>
