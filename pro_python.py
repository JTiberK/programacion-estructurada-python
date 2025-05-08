print("TIPOS DE DATOS EN PYTHON")

# Tipos Primitivos
numero_entero = 10
numero_flotante = 3.14
texto = "Hola"
es_verdadero = True
nada = None

# Tipos Estructurados
mi_lista = [1, 2, 3]
mi_tupla = (4, 5, 6)
mi_diccionario = {"nombre": "Juan", "edad": 30}
mi_conjunto = {7, 8, 9}

# Imprimir los tipos
print("--------Primitivos----------")
print(type(numero_entero))
print(type(numero_flotante))
print(type(texto))
print(type(es_verdadero))
print(type(nada))
print("--------Estructurados----------")
print(type(mi_lista))
print(type(mi_tupla))
print(type(mi_diccionario))
print(type(mi_conjunto))

print("\n--------Ejercicio Ambito de las Variables----------")
# Variable global
mensaje = "Hola yo soy una variable global"

def mostrar_mensaje():
    # Variable local
    mensaje_local = "Hola yo soy una variable local"
    print("Dentro de la función:")
    print("Variable local:", mensaje_local)
    print("Variable global (accedida desde dentro):", mensaje)

def modificar_variable_global():
    global mensaje # Declaramos que vamos a modificar la variable global
    mensaje = "Yo soy una variable global modificada"
    print("----La variable global ha sido modificada dentro de la función----")

# Programa principal
print("Antes de llamar a la función:")
print("Variable global:", mensaje)

mostrar_mensaje()

modificar_variable_global()

print("Después de modificar la variable global:")
print("Variable global:", mensaje)


# Operadores Aritméticos
a = 10
b = 3

print("\n=== Operadores Aritméticos ===")
print("Suma:", a + b)            # 13
print("Resta:", a - b)           # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)        # 3.333...
print("División entera:", a // b)  # 3
print("Módulo:", a % b)          # 1
print("Potencia:", a ** b)       # 1000

# Operadores Lógicos
x = True
y = False

print("\n=== Operadores Lógicos ===")
print("x AND y:", x and y)       # False
print("x OR y:", x or y)         # True
print("NOT x:", not x)           # False

# Combinación de expresiones
edad = 20
tiene_licencia = True

print("\n=== Combinación Lógica ===")
puede_conducir = edad >= 18 and tiene_licencia
print("¿Puede conducir?", puede_conducir)  # True

# Uso de aritméticos en condiciones lógicas
nota = 85
print("¿Nota aprobada entre 60 y 100?", nota >= 60 and nota <= 100)  # True




print("\n=== Programa que clasifica un número y muestra una cuenta regresiva ===")

# ESTRUCTURAS CONDICIONALES
global numero_es
numero_es = int(input("Ingresa un número de 1 a 15: "))

if numero_es > 0:
    print("El número es positivo.")
elif numero_es < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# BUCLE FOR
print("\nImprimiendo los primeros 5 números pares:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, end=" ")

# BUCLE WHILE
print("\n\nCuenta regresiva del número introducido:")
#contador = 5
while numero_es > 0:
    print(numero_es)
    numero_es-= 1
print("¡Final!")


print("\n\n===Procedimiento sin parámetros===")
def saludar():
    print("Hola, bienvenido al programa.")

saludar()

print("\n===Función con parámetros (con retorno)===")
def sumar(a, b):
    return a + b

print("Suma de 4 y 5:", sumar(4, 5))

print("\n===Procedimiento con parámetros (sin retorno)===")
def mostrar_cuadrado(valor):
    print(f"El cuadrado de {valor} es {valor ** 2}") 

mostrar_cuadrado(7)

print("\n===Parámetros por valor (inmutable: int)===")
def intentar_cambiar_valor(x):
    print("Antes de cambiar:", x)
    x = 100
    print("Después de cambiar:", x)

# Parámetros por referencia (mutable: lista)
def agregar_elemento(lista):
    print("Antes de agregar:", lista)
    lista.append("nuevo")
    print("Después de agregar:", lista)


# Parte a: Funciones y procedimientos
# Parte b: Valor vs. Referencia
print("--- Por valor (int) ---")
numero = 50
intentar_cambiar_valor(numero)
print("Fuera de la función:", numero)  # Sigue siendo 50

print("\n--- Por referencia (lista) ---")
mi_lista = ["a", "b"]
agregar_elemento(mi_lista)
print("Fuera de la función:", mi_lista)  # Ahora incluye "nuevo"

print("\n===Procedimiento con parámetros (sin retorno)===")
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
print("\n=========== Ejemplo de Factorial Recursivo ===========")
numero = int(input("Ingresa un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
