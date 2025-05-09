# Trabajo Práctico 5: Listas
# Alumno: Gomez Saucedo Augusto Nahuel

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4.
multiplos_de_4 = list(range(4, 101, 4))
print("Ejercicio 1 - Múltiplos de 4:", multiplos_de_4)

# 2) Crear una lista con cinco elementos (elegidos libremente) y mostrar el penúltimo.
mis_favoritos = ["auriculares", "notebook", "auto", "café", "teclado"]
print("Ejercicio 2 - Penúltimo elemento:", mis_favoritos[-2])

# 3) Crear una lista vacía, agregar tres palabras con append y mostrarla.
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("Ejercicio 3 - Lista con palabras:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”.
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"     # segundo elemento (índice 1)
animales[-1] = "oso"     # último elemento (índice -1)
print("Ejercicio 4 - Lista modificada:", animales)

# 5) Analizar el siguiente programa y explicar qué realiza:
# Elimina el número más grande de la lista usando max() y remove()
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))  # Elimina el número 22
print("5) Lista sin el número mayor:", numeros)

# 6) Crear una lista con números del 10 al 30 (incluido), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista_saltos = list(range(10, 31, 5))
print("6) Primer número:", lista_saltos[0])
print("6) Segundo número:", lista_saltos[1])

# 7) Reemplazar los valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "convertible"]
print("7) Lista de autos modificada:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append. Imprimir la lista resultante.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista de dobles:", dobles)

# 9) Modificar la lista 'compras' según las instrucciones

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print("9) Lista de compras modificada:", compras)


# 10) Crear una lista anidada con los valores indicados y mostrarla

lista_anidada = [15, True, [25.5,57.9,30.6], False]

# Imprimimos la lista resultante por pantalla
print(lista_anidada)