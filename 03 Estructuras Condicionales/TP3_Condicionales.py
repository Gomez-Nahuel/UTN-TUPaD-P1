#Tecnicatura en Programación a distancia
#Trabajo Practico Estructuras Condicionales
#Alumno: Gomez Saucedo Augusto Nahuel

#1) Escribir un programa que solicite la edad del usuario. 

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad.")

#2) Escribir un programa que solicite su nota al usuario. 

nota = float(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes pertenece: Niño, Adolecentes, Adulto/a joven y Adulto/a mayor.

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Ñino/a")
elif edad < 18:
    print("Adolecente")
elif edad < 30:
    print("Adulto/a joven")
else: 
    print("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 

contraseña = input("Ingrese una contraseña: ")

longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene un sesgo positivo (a la derecha).")
elif media < mediana < moda:
    print("La distribución tiene un sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar el sesgo exacto.")

#7) Escribir un programa que solicite una frase o palabra al usuario.

texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto = texto + "!"
    
print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee.

nombre = input("Ingrese su nombre: ")

print("¿Cómo desea ver su nombre?")
print("1 - Todo en MAYÚSCULAS")
print("2 - Todo en minúsculas")
print("3 - Con la primera letra en mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida.")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías.

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S).

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el número del mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion = "Invierno" if hemisferio == "N" else "Verano"
elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio == "N" else "Otoño"
elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio == "N" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "N" else "Primavera"

print("Estás en", estacion)



