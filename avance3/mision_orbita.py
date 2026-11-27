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


# ============================================================
# Componente A: Preparación y autorización
# ============================================================

def mostrar_destinos():
    # Salida: un destino por línea, numerado desde 1 para el usuario
    print("Destinos disponibles:")
    numero = PRIMERA_OPCION
    for destino in DESTINOS:
        print(f"{numero}. {destino[DES_NOMBRE]} ({destino[DES_DIAS]} días)")
        numero = numero + 1


def leer_recursos():
    # Entrada de datos: se pide cada recurso en el orden de RECURSOS,
    # así la posición de la lista coincide con las constantes de posición
    recursos = []
    for nombre_recurso in RECURSOS:
        cantidad = int(input(f"Cantidad disponible de {nombre_recurso}: "))
        recursos.append(cantidad)
    return recursos


def calcular_requeridos(dias_viaje, tripulantes):
    # Procesamiento: fórmulas del Avance 1. Se multiplica por TRAYECTOS
    # porque la nave debe conservar recursos para volver a la Tierra.
    combustible = dias_viaje * CONSUMO_COMBUSTIBLE_DIA * TRAYECTOS + RESERVA_COMBUSTIBLE
    oxigeno = (dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * TRAYECTOS * tripulantes
               + OXIGENO_EMERGENCIA)
    energia = dias_viaje * CONSUMO_ENERGIA_DIA * TRAYECTOS + ENERGIA_EXPLORACION
    provisiones = (dias_viaje * tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA * TRAYECTOS
                   + PROVISIONES_ADICIONALES)
    requeridos = [combustible, oxigeno, energia, provisiones]
    return requeridos


def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes,
                    disponibles, requeridos):
    # Salida: datos generales de la misión
    print(f"Misión: {nombre_mision}")
    print(f"Destino: {nombre_destino}")
    print(f"Duración del viaje de ida: {dias_viaje} días")
    print(f"Tripulantes: {tripulantes}")

    # Salida: comparación de cada recurso disponible contra el requerido
    for i in range(len(RECURSOS)):
        print(f"{RECURSOS[i].capitalize()}: disponible {disponibles[i]} | "
              f"requerido {requeridos[i]}")

    # Decisión: el margen es el combustible extra sobre lo requerido (Ejercicio 2)
    margen = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print(f"Margen adicional de combustible: {margen} unidades")
    if margen < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


def autorizar_lanzamiento(disponibles, requeridos):
    # Decisión: basta con que un recurso no alcance para negar la
    # autorización; por eso la variable inicia en True y solo cambia a False
    autorizado = True
    for i in range(len(RECURSOS)):
        if disponibles[i] < requeridos[i]:
            autorizado = False
    return autorizado


# ============================================================
# Componente B: Viaje de ida (descuento directo)
# ============================================================

def calcular_consumo_diario(tripulantes):
    # Procesamiento: oxígeno y provisiones dependen de la tripulación
    consumo = [CONSUMO_COMBUSTIBLE_DIA,
               CONSUMO_OXIGENO_TRIPULANTE_DIA * tripulantes,
               CONSUMO_ENERGIA_DIA,
               CONSUMO_PROVISIONES_TRIPULANTE_DIA * tripulantes]
    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    # Procesamiento: como la misión fue autorizada, los recursos alcanzan
    # para la ida, así que se descuenta todo el viaje de una sola vez
    consumo = calcular_consumo_diario(tripulantes)
    for i in range(len(recursos)):
        recursos[i] = recursos[i] - consumo[i] * dias_viaje
    return recursos


def recursos_alcanzan(recursos, consumo):
    # Decisión: un día solo se puede viajar si todos los recursos cubren su consumo
    alcanzan = True
    for i in range(len(recursos)):
        if recursos[i] < consumo[i]:
            alcanzan = False
    return alcanzan


def simular_trayecto(recursos, dias, tripulantes):
    # Procesamiento: simulación día a día. dias_completados es el contador y
    # puede_continuar es la variable de control que detiene el ciclo cuando
    # falta un recurso (no se usa break).
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True
    while dias_completados < dias and puede_continuar:
        # Se verifica antes de descontar para no registrar un día incompleto
        if recursos_alcanzan(recursos, consumo):
            for i in range(len(recursos)):
                recursos[i] = recursos[i] - consumo[i]
            dias_completados = dias_completados + 1
            print(f"Día {dias_completados} | Combustible: {recursos[COMBUSTIBLE]} | "
                  f"Oxígeno: {recursos[OXIGENO]} | Energía: {recursos[ENERGIA]} | "
                  f"Provisiones: {recursos[PROVISIONES]}")
        else:
            puede_continuar = False
    return dias_completados


def mostrar_recursos(recursos):
    # Salida: recursos actuales, con el nombre del recurso en mayúscula
    print("Recursos restantes:")
    for i in range(len(recursos)):
        print(f"- {RECURSOS[i].capitalize()}: {recursos[i]} unidades")


# ============================================================
# Componente C: Exploración con bitácora
# ============================================================

def mostrar_menu_actividades():
    # Salida: la opción para finalizar se calcula para que siga siendo
    # correcta si se agregan actividades a la tupla
    for i in range(len(ACTIVIDADES)):
        print(f"{i + 1}. {ACTIVIDADES[i][ACT_NOMBRE]}")
    print(f"{len(ACTIVIDADES) + 1}. Finalizar exploración")


def explorar(recursos):
    print("=== EXPLORACIÓN ===")
    bitacora = []
    opcion_finalizar = len(ACTIVIDADES) + 1
    # Variable de control del menú: el ciclo termina por su condición
    explorando = True
    while explorando:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))

        # Decisión: actividad válida, finalizar u opción no válida
        if opcion >= PRIMERA_OPCION and opcion < opcion_finalizar:
            actividad = ACTIVIDADES[opcion - 1]
            # Se revisan los tres recursos que consumen las actividades
            if (recursos[COMBUSTIBLE] >= actividad[ACT_COMBUSTIBLE]
                    and recursos[ENERGIA] >= actividad[ACT_ENERGIA]
                    and recursos[PROVISIONES] >= actividad[ACT_PROVISIONES]):
                recursos[COMBUSTIBLE] = recursos[COMBUSTIBLE] - actividad[ACT_COMBUSTIBLE]
                recursos[ENERGIA] = recursos[ENERGIA] - actividad[ACT_ENERGIA]
                recursos[PROVISIONES] = recursos[PROVISIONES] - actividad[ACT_PROVISIONES]
                # El número de la fila es el orden en que se hizo la actividad
                bitacora.append([len(bitacora) + 1, actividad[ACT_NOMBRE],
                                 actividad[ACT_PUNTOS]])
                print(f"Actividad realizada: {actividad[ACT_NOMBRE]}. "
                      f"Puntos obtenidos: {actividad[ACT_PUNTOS]}")
            else:
                # La consigna pide terminar aunque otra actividad sí alcance
                print("Recursos insuficientes para realizar la actividad. "
                      "La exploración finaliza.")
                explorando = False
        elif opcion == opcion_finalizar:
            print("Exploración finalizada por la tripulación.")
            explorando = False
        else:
            print("Opción no válida.")
    return bitacora


def contar_actividad(bitacora, nombre_actividad):
    # Recorrido con contador: cuántas filas corresponden a la actividad
    cantidad = 0
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            cantidad = cantidad + 1
    return cantidad


def calcular_puntos(bitacora):
    # Recorrido con acumulador (no se permite sum())
    total_puntos = 0
    for fila in bitacora:
        total_puntos = total_puntos + fila[BIT_PUNTOS]
    return total_puntos


def mostrar_resumen_exploracion(bitacora, recursos):
    # Salida: resumen de la exploración y recursos para el regreso
    print(f"Actividades realizadas: {len(bitacora)}")
    print(f"Muestras recolectadas: {contar_actividad(bitacora, NOMBRE_MUESTRA)}")
    print(f"Puntos científicos: {calcular_puntos(bitacora)}")
    mostrar_recursos(recursos)


# ============================================================
# Componente D: Regreso y supervivencia
# ============================================================

def puede_regresar(recursos, dias_viaje):
    # Decisión: solo se exige el combustible del regreso, sin la reserva
    combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
    puede = recursos[COMBUSTIBLE] >= combustible_regreso
    return puede


def calcular_supervivencia(recursos, tripulantes):
    # Procesamiento: división entera porque solo cuentan los días completos.
    # El orden de la lista es el de RECURSOS_VITALES.
    dias_oxigeno = recursos[OXIGENO] // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA)
    dias_energia = recursos[ENERGIA] // CONSUMO_ENERGIA_DIA
    dias_provisiones = recursos[PROVISIONES] // (tripulantes
                                                 * CONSUMO_PROVISIONES_TRIPULANTE_DIA)
    dias_por_recurso = [dias_oxigeno, dias_energia, dias_provisiones]
    return dias_por_recurso


def obtener_limitantes(dias_por_recurso, minimo):
    # Recorrido: se guardan todos los recursos que empatan con el mínimo
    limitantes = []
    for i in range(len(dias_por_recurso)):
        if dias_por_recurso[i] == minimo:
            limitantes.append(RECURSOS_VITALES[i])
    return limitantes


def regresar(recursos, dias_viaje, tripulantes):
    print("=== REGRESO ===")
    # Decisión principal: caso A (puede regresar) o caso B (varada)
    if puede_regresar(recursos, dias_viaje):
        # Caso A: el regreso dura lo mismo que la ida
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = RESULTADOS[RES_EXITOSO]
        else:
            # El día que falló es el siguiente al último completado
            print(f"El regreso se interrumpió en el día {dias_completados + 1}.")
            consumo = calcular_consumo_diario(tripulantes)
            for i in range(len(RECURSOS)):
                if recursos[i] < consumo[i]:
                    print(f"Recurso insuficiente: {RECURSOS[i]}")
            print("La tripulación no completó el regreso.")
            resultado = RESULTADOS[RES_INTERRUMPIDO]
    else:
        # Caso B: sin combustible para volver se estima la supervivencia
        print("La tripulación quedó varada en el destino.")
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)
        for i in range(len(dias_por_recurso)):
            print(f"Días por {RECURSOS_VITALES[i]}: {dias_por_recurso[i]}")
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        print(f"Supervivencia estimada: {minimo} días")
        print(f"Recurso(s) limitante(s): {', '.join(limitantes)}")
        resultado = RESULTADOS[RES_VARADA]
    return resultado


# ============================================================
# Componente E: Reporte final ordenado
# ============================================================

def obtener_puntos_actividad(fila):
    # Criterio de ordenamiento para sorted(): puntos de la fila
    puntos = fila[BIT_PUNTOS]
    return puntos


def ordenar_bitacora(bitacora):
    # sorted() devuelve una matriz nueva y conserva el orden original de las
    # filas con el mismo puntaje, así que el número menor queda primero
    bitacora_ordenada = sorted(bitacora, key=obtener_puntos_actividad, reverse=True)
    return bitacora_ordenada


def mostrar_reporte(mision, bitacora):
    # Salida: datos de la misión
    print("=== REPORTE FINAL ===")
    print(f"Misión: {mision[MIS_NOMBRE]}")
    print(f"Destino: {mision[MIS_DESTINO]}")
    print(f"Resultado: {mision[MIS_RESULTADO]}")
    print(f"Puntos científicos: {mision[MIS_PUNTOS]}")
    print("Bitácora de exploración (de mayor a menor puntaje):")

    # Decisión: bitácora vacía o recorrido de la bitácora ordenada
    if len(bitacora) == 0:
        print("Sin actividades registradas.")
    else:
        for fila in ordenar_bitacora(bitacora):
            print(f"#{fila[BIT_NUMERO]} {fila[BIT_ACTIVIDAD]} - {fila[BIT_PUNTOS]} puntos")


def ejecutar_mision(numero):
    # Entrada de datos de la planificación
    print("=== PLANIFICACIÓN ===")
    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))
    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))

    # Si la misión no llega a explorar, la bitácora queda vacía (0 puntos)
    bitacora = []

    # Decisión: validación de la opción de destino
    if opcion_destino < PRIMERA_OPCION or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
        nombre_destino = DESTINO_NINGUNO
        resultado = RESULTADOS[RES_NO_PLANIFICADA]
    else:
        # Preparación: la opción empieza en 1 y la fila de la tupla en 0
        destino = DESTINOS[opcion_destino - 1]
        nombre_destino = destino[DES_NOMBRE]
        dias_viaje = destino[DES_DIAS]
        recursos = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes,
                        recursos, requeridos)

        # Decisión: autorización del lanzamiento
        if autorizar_lanzamiento(recursos, requeridos):
            print("Lanzamiento autorizado.")
            # Viaje → llegada → exploración → evaluación del regreso
            print("=== VIAJE DE IDA ===")
            recursos = viajar_al_destino(recursos, dias_viaje, tripulantes)
            print(f"La nave llegó a {nombre_destino} en {dias_viaje} días.")
            mostrar_recursos(recursos)
            bitacora = explorar(recursos)
            mostrar_resumen_exploracion(bitacora, recursos)
            resultado = regresar(recursos, dias_viaje, tripulantes)
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
            resultado = RESULTADOS[RES_NO_AUTORIZADA]

    # Salida: la fila de la misión se arma para el reporte y el historial
    puntos = calcular_puntos(bitacora)
    mision = [numero, nombre_mision, nombre_destino, resultado, puntos]
    mostrar_reporte(mision, bitacora)
    return mision


# ============================================================
# Componente F: Menú principal e historial de misiones
# ============================================================

def mostrar_menu_principal():
    print("===== MISIÓN ÓRBITA =====")
    print("1. Planificar y ejecutar una misión")
    print("2. Ver historial de misiones")
    print("3. Salir")


def obtener_puntos_mision(mision):
    # Criterio de ordenamiento para sorted(): puntos de la misión
    puntos = mision[MIS_PUNTOS]
    return puntos


def ordenar_historial(historial):
    # Matriz nueva de mayor a menor puntaje; el historial original no cambia
    historial_ordenado = sorted(historial, key=obtener_puntos_mision, reverse=True)
    return historial_ordenado


def linea_mision(mision):
    linea = (f"#{mision[MIS_NUMERO]} {mision[MIS_NOMBRE]} | {mision[MIS_DESTINO]} | "
             f"{mision[MIS_RESULTADO]} | {mision[MIS_PUNTOS]} puntos")
    return linea


def mostrar_historial(historial):
    print("=== HISTORIAL DE MISIONES ===")
    # Decisión: historial vacío o recorrido del historial ordenado
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        for mision in ordenar_historial(historial):
            print(linea_mision(mision))


def main():
    # El historial vive en main y se comparte solo por parámetros
    historial = []
    # Variable de control del menú principal
    en_ejecucion = True
    while en_ejecucion:
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))

        # Decisión: opción del menú principal
        if opcion == OPCION_PLANIFICAR:
            # El número de la misión es la cantidad de misiones registradas + 1
            mision = ejecutar_mision(len(historial) + 1)
            historial.append(mision)
        elif opcion == OPCION_HISTORIAL:
            mostrar_historial(historial)
        elif opcion == OPCION_SALIR:
            en_ejecucion = False
        else:
            print("Opción no válida.")
    print("Fin del sistema Misión Órbita.")


main()
