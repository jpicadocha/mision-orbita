# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: 08/11/2026     Versión: 1.0
# Descripción: Simula las actividades de exploración científica en
#              el destino mediante un menú que se repite hasta que la
#              tripulación finaliza o los recursos no alcanzan.
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes
# Los costos y puntos de cada actividad se declaran aquí para que
# no aparezcan "números mágicos" dentro de las decisiones.
# ------------------------------------------------------------
OPCION_ANALIZAR = 1
OPCION_MUESTRA = 2
OPCION_OBSERVACION = 3
OPCION_FINALIZAR = 4

NOMBRE_ANALIZAR = "Analizar terreno"
NOMBRE_MUESTRA = "Recolectar muestra"
NOMBRE_OBSERVACION = "Realizar observación"

ENERGIA_ANALIZAR = 8
PROVISIONES_ANALIZAR = 0
PUNTOS_ANALIZAR = 10

ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

# ------------------------------------------------------------
# Entrada de datos
# Cada ejercicio es independiente: el estado al llegar al destino
# se solicita por consola.
# ------------------------------------------------------------
energia = int(input("Energía disponible al llegar al destino: "))
provisiones = int(input("Provisiones disponibles al llegar al destino: "))

# ------------------------------------------------------------
# Inicialización del estado de la exploración
# La misión inicia sin puntos ni actividades; explorando es la
# variable de control que mantiene vivo el menú.
# ------------------------------------------------------------
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
explorando = True

# ------------------------------------------------------------
# Ciclo del menú de actividades
# El ciclo termina únicamente cuando explorando pasa a False
# (opción 4 o recursos insuficientes), sin usar break.
# ------------------------------------------------------------
while explorando == True:
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una actividad: "))

    # Decisión múltiple: finalizar, actividad válida u opción inválida
    if opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        explorando = False
    elif opcion >= OPCION_ANALIZAR and opcion <= OPCION_OBSERVACION:
        # Se asignan los costos y puntos de la actividad elegida
        if opcion == OPCION_ANALIZAR:
            nombre_actividad = NOMBRE_ANALIZAR
            energia_actividad = ENERGIA_ANALIZAR
            provisiones_actividad = PROVISIONES_ANALIZAR
            puntos_actividad = PUNTOS_ANALIZAR
        elif opcion == OPCION_MUESTRA:
            nombre_actividad = NOMBRE_MUESTRA
            energia_actividad = ENERGIA_MUESTRA
            provisiones_actividad = PROVISIONES_MUESTRA
            puntos_actividad = PUNTOS_MUESTRA
        else:
            nombre_actividad = NOMBRE_OBSERVACION
            energia_actividad = ENERGIA_OBSERVACION
            provisiones_actividad = PROVISIONES_OBSERVACION
            puntos_actividad = PUNTOS_OBSERVACION

        # Decisión anidada: solo tiene sentido verificar los recursos
        # una vez que se sabe que la actividad es válida
        if energia >= energia_actividad and provisiones >= provisiones_actividad:
            energia = energia - energia_actividad
            provisiones = provisiones - provisiones_actividad
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + puntos_actividad

            # Solo la recolección de muestra incrementa este contador
            if opcion == OPCION_MUESTRA:
                muestras_recolectadas = muestras_recolectadas + 1

            print(f"Actividad realizada: {nombre_actividad}. Puntos obtenidos: {puntos_actividad}")
        else:
            # La exploración termina aunque otra actividad más barata
            # sí pudiera realizarse, según lo indica la consigna
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            explorando = False
    else:
        print("Opción no válida.")

# ------------------------------------------------------------
# Salida de resultados: resumen final de la exploración
# ------------------------------------------------------------
print()
print(f"Actividades realizadas: {actividades_realizadas}")
print(f"Muestras recolectadas: {muestras_recolectadas}")
print(f"Puntos científicos: {puntos_cientificos}")
print(f"Energía restante: {energia} unidades")
print(f"Provisiones restantes: {provisiones} unidades")
