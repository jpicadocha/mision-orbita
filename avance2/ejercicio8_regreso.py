# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: 08/11/2026     Versión: 1.0
# Descripción: Evalúa si la nave puede iniciar el regreso. Si hay
#              combustible, simula día a día el viaje de vuelta; si no,
#              la tripulación queda varada y se estima su supervivencia.
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes
# Consumos diarios definidos por la consigna.
# ------------------------------------------------------------
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1

# ------------------------------------------------------------
# Entrada de datos
# Estado de la nave al terminar la exploración en el destino.
# ------------------------------------------------------------
tripulantes = int(input("Cantidad de tripulantes: "))
dias_ida = int(input("Cantidad de días del viaje de ida: "))
combustible = int(input("Combustible disponible: "))
oxigeno = int(input("Oxígeno disponible: "))
energia = int(input("Energía disponible: "))
provisiones = int(input("Provisiones disponibles: "))

# ------------------------------------------------------------
# Procesamiento previo
# El regreso dura lo mismo que la ida; en esta evaluación no se suma
# la reserva de emergencia. El consumo de oxígeno y provisiones
# depende de la cantidad de tripulantes.
# ------------------------------------------------------------
combustible_regreso = dias_ida * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA

# ------------------------------------------------------------
# Decisión principal: caso A (inicia el regreso) o caso B (varada)
# ------------------------------------------------------------
if combustible >= combustible_regreso:
    # --------------------------------------------------------
    # Caso A: simulación del regreso, un día por iteración
    # dias_completados es el contador; regreso_continua es la
    # variable de control que detiene el ciclo si falta un recurso.
    # --------------------------------------------------------
    dias_completados = 0
    regreso_continua = True

    while dias_completados < dias_ida and regreso_continua == True:
        # Se verifica antes de descontar para no consumir un día incompleto
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno >= consumo_oxigeno_dia
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= consumo_provisiones_dia):
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - consumo_oxigeno_dia
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - consumo_provisiones_dia
            dias_completados = dias_completados + 1
            print(f"Día {dias_completados} | Combustible: {combustible} | Oxígeno: {oxigeno} | Energía: {energia} | Provisiones: {provisiones}")
        else:
            regreso_continua = False

    # Resultado del regreso
    if dias_completados == dias_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print(f"Combustible restante: {combustible} unidades")
        print(f"Oxígeno restante: {oxigeno} unidades")
        print(f"Energía restante: {energia} unidades")
        print(f"Provisiones restantes: {provisiones} unidades")
    else:
        # Como no se descontó el día fallido, los recursos conservan el
        # valor con el que se detectó la falta
        dia_interrumpido = dias_completados + 1
        print(f"El regreso se interrumpió en el día {dia_interrumpido}.")

        # Cada recurso se evalúa por separado porque pueden faltar varios.
        # El combustible no se evalúa: la regla de decisión ya lo garantizó.
        if oxigeno < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")

        print("La tripulación no completó el regreso.")
else:
    # --------------------------------------------------------
    # Caso B: tripulación varada, estimación de supervivencia
    # La división entera da únicamente días completos.
    # --------------------------------------------------------
    print("La tripulación quedó varada en el destino.")

    dias_oxigeno = oxigeno // consumo_oxigeno_dia
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // consumo_provisiones_dia

    # El valor mínimo se obtiene comparando con condicionales
    supervivencia_dias = dias_oxigeno
    if dias_energia < supervivencia_dias:
        supervivencia_dias = dias_energia
    if dias_provisiones < supervivencia_dias:
        supervivencia_dias = dias_provisiones

    # Se identifican todos los recursos que empatan en el mínimo,
    # respetando el orden oxígeno, energía y provisiones
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia_dias:
        recursos_limitantes = "oxígeno"
    if dias_energia == supervivencia_dias:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
    if dias_provisiones == supervivencia_dias:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    print(f"Días por oxígeno: {dias_oxigeno}")
    print(f"Días por energía: {dias_energia}")
    print(f"Días por provisiones: {dias_provisiones}")
    print(f"Supervivencia estimada: {supervivencia_dias} días")
    print(f"Recurso(s) limitante(s): {recursos_limitantes}")
