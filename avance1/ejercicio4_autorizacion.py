# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: [COMPLETAR FECHA]    Version: 1.0
# Descripcion: Autoriza lanzamiento si todos los recursos alcanzan.
# ============================================================

# Declaracion de constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))
oxigeno_disponible = int(input("Oxigeno disponible: "))
oxigeno_requerido = int(input("Oxigeno requerido: "))
energia_disponible = int(input("Energia disponible: "))
energia_requerida = int(input("Energia requerida: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Procesamiento: se reserva combustible tambien para el regreso.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Decision doble: todas las condiciones deben cumplirse a la vez.
if (combustible_disponible >= combustible_total
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La mision debe ser revisada.")
