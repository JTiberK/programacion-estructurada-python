print("\nTIPOS DE DATOS EN PYTHON")

# ========== Pregunta 1. Tipos Primitivos y Estructurados ==========
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
print("\n=========== Pregunta 1. Primitivos ===========")
print(type(numero_entero))
print(type(numero_flotante))
print(type(texto))
print(type(es_verdadero))
print(type(nada))
print("\n=========== Pregunta 1. Estructurados ===========")
print(type(mi_lista))
print(type(mi_tupla))
print(type(mi_diccionario))
print(type(mi_conjunto))

# ========== Pregunta 2. Variables y Ámbito de Utilización ==========
print("\n===== Pregunta 2. Ejercicio Ambito de las Variables =========")
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

# ========== Pregunta 3. Operadores Aritméticos y Lógicos ==========
# Operadores Aritméticos
a = 10
b = 3

print("\n====== Pregunta 3. Operadores Aritméticos ========")
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

print("\n===== Pregunta 3. Operadores Lógicos =====")
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



# === Pregunta 4. Estructuras de Control ===
print("\n=== Pregunta 4. Programa que clasifica un número y muestra una cuenta regresiva ===")

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
print("¡Final!\n")