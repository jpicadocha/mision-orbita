# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrantes: Juan Pablo Picado Chaves
# Fecha: [COMPLETAR FECHA]    Version: 1.0
# Descripcion: Verifica soporte vital de la tripulacion.
# ============================================================

# Entrada de datos
oxigeno_disponible = int(input("Oxigeno disponible: "))
oxigeno_requerido = int(input("Oxigeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Decision doble: ambos recursos deben cubrir el minimo requerido.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulacion.")
else:
    print("La nave no posee recursos suficientes para la tripulacion.")
