from itertools import product
from datetime import datetime

# ========================
# PARTE 1: CONJUNTOS
# ========================

# DNIs ficticios
dni_1 = "27147777"
dni_2 = "37587117"
dni_3 = "17987867"

# Crear conjuntos de dígitos únicos
conjunto_A = set(dni_1)
conjunto_B = set(dni_2)
conjunto_C = set(dni_3)

print("Conjunto A:", conjunto_A)
print("Conjunto B:", conjunto_B)
print("Conjunto C:", conjunto_C)
print()

# Operaciones entre conjuntos
print("Unión A ∪ B:", conjunto_A.union(conjunto_B))
print("Intersección A ∩ B:", conjunto_A.intersection(conjunto_B))
print("Diferencia A - B:", conjunto_A.difference(conjunto_B))
print("Diferencia simétrica A Δ B:", conjunto_A.symmetric_difference(conjunto_B))
print()

# Expresiones lógicas (lenguaje natural y en código)
# 1. "Si hay un número que aparece en todos los conjuntos, mostrarlo"
interseccion_total = conjunto_A & conjunto_B & conjunto_C
if interseccion_total:
    print("Dígitos en común entre los tres conjuntos:", interseccion_total)
else:
    print("No hay dígitos en común entre los tres conjuntos")

# 2. "Si algún conjunto tiene más de 6 elementos, tiene diversidad alta"
for nombre, conjunto in [("A", conjunto_A), ("B", conjunto_B), ("C", conjunto_C)]:
    if len(conjunto) > 6:
        print(f"El conjunto {nombre} tiene diversidad numérica alta.")
print()

# ========================
# PARTE 2: AÑOS DE NACIMIENTO
# ========================

# Años ficticios
años = [2001, 1998, 2004]

# Contar pares e impares
pares = [a for a in años if a % 2 == 0]
impares = [a for a in años if a % 2 != 0]

print("Cantidad de personas nacidas en años pares:", len(pares))
print("Cantidad de personas nacidas en años impares:", len(impares))

# Grupo Z
if all(a > 2000 for a in años):
    print("Todos nacieron después del 2000: ¡Grupo Z!")
else:
    print("No todos son del Grupo Z")

# Año bisiesto
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if any(es_bisiesto(a) for a in años):
    print("Tenemos un año especial: hay al menos un año bisiesto")
else:
    print("No hay años bisiestos")
print()

# Producto cartesiano entre años y edades
año_actual = datetime.now().year
edades = [año_actual - a for a in años]
cartesiano = list(product(años, edades))

print("Producto cartesiano entre años y edades:")
for par in cartesiano:
    print(par)