#Trabajo Práctico Recursividad
#Alumno: Gomez Saucedo Augusto Nahuel

#1. Función recursiva que calcule el factorial de un número.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
limite = int(input("Ingrese un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#2. Función recursiva para calcular el valor de la serie de Fibonacci.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
pos = int(input("Ingrese la cantidad de términos de Fibonacci a mostrar: "))
for i in range(pos):
    print(fibonacci(i), end=" ")

#3. Función recursiva que calcule la potencia.

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

#4. Convertir número decimal a binario (retornando string).

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número en base decimal: "))
binario = decimal_a_binario(numero)
print("Binario:", binario if binario else "0")

#5. Función recursiva para verificar si una palabra es palíndromo.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print(es_palindromo("radar"))

#6. Sumar los dígitos de un número entero positivo.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print("Suma de sus dígitos:", suma_digitos(numero))

#7. Contar bloques para una pirámide.

def contar_bloques(n):
  if n <= 1:
    return n
  else:
    return n + contar_bloques(n - 1)

print(contar_bloques(7))

#8. Contar cuántas veces aparece un dígito dentro de un número.

def contar_digito(numero, digito):
  if numero // 10 == 0:
    return 1 if numero == digito else 0
  else:
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
