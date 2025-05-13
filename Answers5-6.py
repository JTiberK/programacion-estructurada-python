# 
# ========== Pregunta 5. Funciones y Procedimientos ==========
print("\n=== Pregunta 5. Procedimiento sin parámetros===")
def saludar():
    print("Hola, bienvenido al programa.")

saludar()

print("\n=== Pregunta 5. Función con parámetros (con retorno)===")
def sumar(a, b):
    return a + b

print("Suma de 4 y 5:", sumar(4, 5))

print("\n=== Pregunta 5. Procedimiento con parámetros (sin retorno)===")
def mostrar_cuadrado(valor):
    print(f"El cuadrado de {valor} es {valor ** 2}") 

mostrar_cuadrado(7)

print("\n=== Pregunta 5. Parámetros por valor (inmutable: int)===")
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

print("\n=== Pregunta 5. Procedimiento con parámetros (sin retorno)===")
def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    # Caso recursivo
    else:
        return n * factorial(n - 1)

# ========== Pregunta 6. Recursividad ==========
print("\n=========== Pregunta 6. Ejemplo de Factorial Recursivo ===========")
numero = int(input("Ingresa un número para calcular su factorial: "))
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
