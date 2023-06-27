import csv
import numpy as np

peliculas = []
asientos = np.zeros((10, 15), dtype=int)
valor_entrada = 2000

# Película predeterminada
pelicula_predeterminada = {
    "nombre": "Spiderman - Lejos de Casa",
    "categoria": "Superheroes",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "El Rey León",
    "categoria": "Live accion",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "Toy Story 4",
    "categoria": "Animacion",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "Scream IV",
    "categoria": "Terror",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "Super Mario Bros 2D",
    "categoria": "Animacion",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "Super Mario Bros 3D",
    "categoria": "Animacion",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

pelicula_predeterminada = {
    "nombre": "Avatar 2 3D",
    "categoria": "Acción",
    "ventas": 0,
    "asistentes": 0,
    "asistentes_lista": []
}
peliculas.append(pelicula_predeterminada)

def nueva_pelicula():
    nombre = input("Ingrese el nombre de la película: ")
    descripcion = input("Ingrese la descripción de la película: ")
    categoria = input("Ingrese la categoría de la película (acción/terror/suspenso): ")
    pelicula = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "ventas": 0,
        "asistentes": 0,
        "asistentes_lista": []
    }
    peliculas.append(pelicula)

def mostrar_asientos(pelicula_index):
    if pelicula_index < 0 or pelicula_index >= len(peliculas):
        print("La película seleccionada no es válida.")
        return

    pelicula = peliculas[pelicula_index]
    print(f"Estado de los asientos para la película: {pelicula['nombre']}")
    if pelicula['asistentes'] == 0:
        print("No hay asientos ocupados.")
        return

    print("  1  2  3  4  5  6  7  8  9  10   11  12  13  14  15 ")
    for i, fila in enumerate(asientos):
        print(f"{i+1:2d} ", end="")
        for j, asiento in enumerate(fila):
            if asiento == 0:
                print("[⭕]", end=" ")
            else:
                print("[❌]", end=" ")
        print()

def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No hay películas registradas.")
    else:
        for i, pelicula in enumerate(peliculas):
            print(f"{i+1}. {pelicula['nombre']} - {pelicula['categoria']}")

def comprar_entrada(pelicula_index):
    if pelicula_index < 0 or pelicula_index >= len(peliculas):
        print("La película seleccionada no es válida.")
        return

    pelicula = peliculas[pelicula_index]
    mostrar_asientos(pelicula_index)

    fila_str = input("Ingrese el número de fila del asiento: ")
    if not fila_str.isdigit():
        print("El número de fila debe ser un número entero.")
        return
    fila = int(fila_str)

    columna_str = input("Ingrese el número de columna del asiento: ")
    if not columna_str.isdigit():
        print("El número de columna debe ser un número entero.")
        return
    columna = int(columna_str)

    if fila < 1 or fila > 20 or columna < 1 or columna > 10:
        print("El asiento seleccionado no es válido.")
        return

    if asientos[fila-1, columna-1] == 0:
        asientos[fila-1, columna-1] = 1
        pelicula["ventas"] += 1
        pelicula["asistentes"] += 1
        pelicula["asistentes_lista"].append(input("Ingrese el nombre del asistente: "))
        num_boleta = len(pelicula["asistentes_lista"])
        generar_boucher(pelicula["nombre"], fila, columna, num_boleta)
        print("¡Compra exitosa! Se ha generado el boletín.")
    else:
        print("El asiento seleccionado ya está ocupado.")

def generar_boucher(nombre_pelicula, fila, columna, num_boleta):
    with open(f"boucher_{num_boleta}.txt", "w") as archivo:
        archivo.write(f"************************\n")
        archivo.write(f"***    CINEDUOC    *****\n")
        archivo.write(f"************************\n")
        archivo.write(f"Pelicula: {nombre_pelicula}\n")
        archivo.write(f"Asiento: Fila {fila}, Columna {columna}\n")
        archivo.write(f"Valor de entrada: {valor_entrada}\n")
        archivo.write(f"Numero de boleta: {num_boleta}\n")
        archivo.write(f"************************\n")
        archivo.write(f"******* CINEDUOC *******\n")
        archivo.write(f"************************\n")

def actualizar_datos_pelicula(pelicula_index):
    if pelicula_index < 0 or pelicula_index >= len(peliculas):
        print("La película seleccionada no es válida.")
        return

    pelicula = peliculas[pelicula_index]
    pelicula["nombre"] = input("Ingrese el nuevo nombre de la película: ")
    pelicula["descripcion"] = input("Ingrese la nueva descripción de la película: ")
    pelicula["categoria"] = input("Ingrese la nueva categoría de la película: ")

def calcular_total_ventas():
    for pelicula in peliculas:
        print(f"{pelicula['nombre']} - Ventas: {pelicula['ventas']}")

def calcular_total_asistentes():
    for pelicula in peliculas:
        print(f"{pelicula['nombre']} - Asistentes: {pelicula['asistentes']}")

def mostrar_listado_asistentes():
    for pelicula in peliculas:
        print(f"Película: {pelicula['nombre']}")
        print("Asistentes:")
        for asistente in pelicula["asistentes_lista"]:
            print(asistente)

def guardar_reporte():
    with open("reporte_asistentes.txt", "w") as archivo:
        for pelicula in peliculas:
            archivo.write(f"Película: {pelicula['nombre']}\n")
            archivo.write("Asistentes:\n")
            for asistente in pelicula["asistentes_lista"]:
                archivo.write(f"- {asistente}\n")

def importar_peliculas():
    nombre_archivo = input("Ingrese el nombre del archivo a importar: ")
    try:
        with open(nombre_archivo, "r") as archivo:
            reader = csv.reader(archivo)
            for linea in reader:
                nombre, descripcion, categoria = linea
                pelicula = {
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "categoria": categoria,
                    "ventas": 0,
                    "asistentes": 0,
                    "asistentes_lista": []
                }
                peliculas.append(pelicula)
        print("¡Películas importadas correctamente!")
    except FileNotFoundError:
        print("El archivo de importación no existe.")

def exportar_peliculas():
    nombre_archivo = input("Ingrese el nombre del archivo a exportar: ")
    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        for pelicula in peliculas:
            writer.writerow([pelicula["nombre"], pelicula["descripcion"], pelicula["categoria"]])
    print("¡Películas exportadas correctamente!")

# Película predeterminada
asientos[5, 3] = 1
pelicula_predeterminada["ventas"] += 1
pelicula_predeterminada["asistentes"] += 1
pelicula_predeterminada["asistentes_lista"].append("Amaro Torres")

# Menú principal
while True:
    print("---- CINEDUOC ----")
    print("1. Nueva película")
    print("2. Mostrar asientos")
    print("3. Mostrar películas")
    print("4. Comprar entrada")
    print("5. Actualizar datos de película")
    print("6. Calcular total de ventas")
    print("7. Calcular total de asistentes")
    print("8. Mostrar listado de asistentes")
    print("9. Guardar reporte de asistentes")
    print("10. Importar películas desde archivo ")
    print("11. Exportar películas a archivo ")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        nueva_pelicula()
    elif opcion == "2":
        mostrar_asientos(int(input("Ingrese el número de película: ")) - 1)
    elif opcion == "3":
        mostrar_peliculas()
    elif opcion == "4":
        comprar_entrada(int(input("Ingrese el número de película: ")) - 1)
    elif opcion == "5":
        actualizar_datos_pelicula(int(input("Ingrese el número de película: ")) - 1)
    elif opcion == "6":
        calcular_total_ventas()
    elif opcion == "7":
        calcular_total_asistentes()
    elif opcion == "8":
        mostrar_listado_asistentes()
    elif opcion == "9":
        guardar_reporte()
    elif opcion == "10":
        importar_peliculas()
    elif opcion == "11":
        exportar_peliculas()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")