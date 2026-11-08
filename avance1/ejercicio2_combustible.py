# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: [COMPLETAR FECHA]    Version: 1.0
# Descripcion: Verifica el margen adicional de combustible.
# ============================================================

# Declaracion de constantes
RESERVA_COMBUSTIBLE = 10
UMBRAL_MARGEN = 10

# Entrada de datos
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

# Procesamiento: el total incluye el regreso y la reserva.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Salida obligatoria, incluso cuando el margen es insuficiente.
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# Decision simple: se advierte solo si el margen es menor que diez.
if combustible_adicional < UMBRAL_MARGEN:
    print("Advertencia: el margen adicional de combustible es bajo.")
