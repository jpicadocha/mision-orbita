# ============================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: 27/11/2026          Versión: 1.0
# Descripción: Sistema integrado Misión Órbita. Administra el ciclo
#              completo de una misión espacial: preparación,
#              autorización, viaje de ida, exploración con bitácora,
#              evaluación del regreso (o supervivencia si la
#              tripulación queda varada) y reporte final ordenado.
#              Incluye un menú principal con historial de misiones.
#              Alcance: grupo de 1 persona (componentes A a F).
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes: datos fijos de la misión
# Se usan tuplas porque estos datos no cambian durante la ejecución.
# ------------------------------------------------------------
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))
# Cada actividad: (nombre, combustible, energía, provisiones, puntos)
ACTIVIDADES = (("Analizar terreno", 0, 8, 0, 10),
               ("Recolectar muestra", 0, 12, 2, 20),
               ("Realizar observación", 0, 5, 0, 8),
               ("Sobrevolar la zona", 15, 3, 0, 25))
RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = ("Regreso exitoso", "Regreso interrumpido", "Tripulación varada",
              "No autorizada", "No planificada")

# Columnas de DESTINOS: (nombre, dias)
DES_NOMBRE = 0
DES_DIAS = 1
# Columnas de ACTIVIDADES: (nombre, combustible, energía, provisiones, puntos)
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4
# Posición de cada recurso en las listas recursos, requeridos y consumo
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3
# Columnas de la matriz bitacora: [numero, actividad, puntos]
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2
# Columnas de la matriz historial: [numero, nombre, destino, resultado, puntos]
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# ------------------------------------------------------------
# Declaración de constantes: valores fijos de las fórmulas
# Consumos diarios del viaje (Avance 1 y Avance 2).
# ------------------------------------------------------------
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
# Se planifica ida y regreso, por eso los recursos se calculan para 2 trayectos
TRAYECTOS = 2
RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3
# Por debajo de este margen se advierte que el combustible extra es bajo
MARGEN_MINIMO_COMBUSTIBLE = 10

# ------------------------------------------------------------
# Declaración de constantes: posiciones de RESULTADOS y opciones
# Evitan números mágicos al elegir un resultado o una opción de menú.
# ------------------------------------------------------------
RES_EXITOSO = 0
RES_INTERRUMPIDO = 1
RES_VARADA = 2
RES_NO_AUTORIZADA = 3
RES_NO_PLANIFICADA = 4
DESTINO_NINGUNO = "Ninguno"
NOMBRE_MUESTRA = "Recolectar muestra"
PRIMERA_OPCION = 1
OPCION_PLANIFICAR = 1
OPCION_HISTORIAL = 2
OPCION_SALIR = 3
