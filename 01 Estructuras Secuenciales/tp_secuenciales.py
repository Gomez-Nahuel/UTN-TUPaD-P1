# 🧠 **Tecnicatura en Programación a Distancia**

## 📚 **Trabajo Práctico: Estructuras Secuenciales**

### 👨‍🎓 **Alumno:** Gómez Saucedo Augusto Nahuel  
### 🖥️ **Materia:** Programación 1  
### 🏷️ **Comisión:** 14

#1) ----------------------------------------------------------------------------
print("Hola mundo!")

#2) ----------------------------------------------------------------------------
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3)-----------------------------------------------------------------------------
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
lugar = input("Ingrese su lugar de residencia:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

#4)-----------------------------------------------------------------------------
pi = 3.14
radio = float(input("Ingrese el radio del círculo: "))
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El área del círculo es {area}")
print(f"El perímetro del círculo es {perimetro}")

#5)-----------------------------------------------------------------------------
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#6)-----------------------------------------------------------------------------
numero = int(input("Ingrese un número: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#7)-----------------------------------------------------------------------------
numero1 = int(input("Ingrese el primer número (distinto de 0): "))
numero2 = int(input("Ingrese el segundo número (distinto de 0): "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8)-----------------------------------------------------------------------------
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su índice de masa corporal (IMC) es: {imc}")

#9)-----------------------------------------------------------------------------
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print("La temperatura en Fahrenheit es:", fahrenheit)

#10)----------------------------------------------------------------------------
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio es:", promedio)
