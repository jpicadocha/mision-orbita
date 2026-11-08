# Misión Órbita

Simulador básico de exploración espacial en Python, desarrollado de forma progresiva en tres avances para el curso
**SOFT-01 Principios de programación 1** (Universidad CENFOTEC, Escuela de Ingeniería del Software, periodo C3-2026,
sección SCV6). Docente facilitadora: Verónica Mora Lezcano.

## Integrantes

- Juan Pablo Picado Chaves (entrega individual)

## Descripción

Cada ejercicio es un programa independiente que usa solo la consola. Los valores son unidades ficticias de misión.

- **Avance 1 (preparación de la misión):** ejercicios 1 a 4 (cálculo de recursos, verificación de combustible,
  soporte de la tripulación y autorización inicial de lanzamiento).
- **Avance 2 (ejecución de la misión):** ejercicios 7 y 8, que corresponden al alcance individual.
  - `ejercicio7_exploracion.py`: menú de actividades de exploración científica que se repite con un ciclo `while`,
    con contadores, un acumulador de puntos científicos y una variable de control.
  - `ejercicio8_regreso.py`: evalúa si la nave puede regresar. Con combustible simula el regreso día a día (caso A);
    sin combustible estima la supervivencia de la tripulación varada y su recurso limitante (caso B).

## Estructura del repositorio

```text
mision-orbita/
├── README.md
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
├── avance2/
│   ├── ejercicio7_exploracion.py
│   └── ejercicio8_regreso.py
└── documentacion/
    ├── avance1.pdf
    ├── ejercicio7_exploracion.pdf
    └── ejercicio8_regreso.pdf
```

## Cómo ejecutar los programas

Requiere Python 3 y Visual Studio Code. Se abre la carpeta del proyecto en VS Code, se abre una terminal
(Terminal > Nueva terminal) y se ejecuta cada programa por separado:

```bash
python avance2/ejercicio7_exploracion.py
python avance2/ejercicio8_regreso.py
```

En algunos equipos el comando es `python3` en lugar de `python`. Los programas piden los datos por consola en el orden
indicado en pantalla. Se asume que se ingresan números enteros positivos; solo se valida la opción del menú del
ejercicio 7.

## Convenciones y estilos de programación

- Nombres de variables descriptivos, en minúscula y con notación `snake_case`.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo; no hay números mágicos en las fórmulas.
- Indentación uniforme de 4 espacios, espacios alrededor de los operadores y líneas en blanco entre bloques lógicos.
- Cada archivo inicia con un encabezado (archivo, curso, integrantes, fecha, versión y descripción).
- Cada bloque lógico (constantes, entrada, procesamiento, decisiones y salida) tiene un comentario que explica su propósito.
- Mensajes de consola claros, con sus unidades, en el orden de los ejemplos de la consigna.
- Restricciones técnicas del curso: sin funciones propias (`def`), listas, tuplas, diccionarios, librerías, `break`,
  `continue`, `exit()`, `quit()`, `min()` ni `max()`. El ciclo `for` solo se permitiría con `range()`.
- Mensajes de commit en español, que describen la modificación realizada.

## Documentación

Cada PDF de `documentacion/` incluye la tabla de variables, el diagrama de flujo, el código, la tabla de casos de prueba
y las capturas de pantalla de la ejecución de cada caso.
