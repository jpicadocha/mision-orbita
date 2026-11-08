# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrantes: [COMPLETAR NOMBRES]
# Fecha: [COMPLETAR FECHA]    Version: 1.0
# Descripcion: Calcula los recursos para ida y regreso.
# ============================================================

# Declaracion de constantes
CONSUMO_COMBUSTIBLE = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES = 1
RESERVA_PROVISIONES = 3
TRAYECTOS = 2

# Entrada de datos
nombre_mision = input("Nombre de la mision: ")
tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Dias estimados para llegar: "))

# Procesamiento: el viaje de regreso dura lo mismo que el de ida.
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
oxigeno_requerido = dias_viaje * CONSUMO_OXIGENO * TRAYECTOS * tripulantes + RESERVA_OXIGENO
energia_requerida = dias_viaje * CONSUMO_ENERGIA * TRAYECTOS + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * tripulantes * TRAYECTOS * CONSUMO_PROVISIONES + RESERVA_PROVISIONES

# Salida: resumen completo con unidades.
print("\n--- RESUMEN DE LA MISION ---")
print("Mision:", nombre_mision)
print("Tripulantes:", tripulantes)
print("Duracion estimada hasta el destino:", dias_viaje, "dias")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxigeno requerido:", oxigeno_requerido, "unidades")
print("Energia requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")
