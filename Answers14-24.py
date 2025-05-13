# === Pregunta 14. Manipulación de Arrays (listas) ===
print("\n=== Pregunta 14. Manipulación de Arrays ===")

def manipular_array():
    # Crear array
    numeros = [1, 2, 3, 4, 5]
    print("Array original:", numeros)

    # Acceder a elementos
    print("Primer elemento:", numeros[0])

    # Modificar elementos
    numeros[2] = 10
    print("Array modificado:", numeros)

    # Recorrer array
    print("Recorrido del array:")
    for numero in numeros:
        print(numero)

manipular_array()


# === Pregunta 15. Uso de Operadores Bit a Bit ===
print("\n=== Pregunta 15. Operadores Bit a Bit ===")

def operadores_bit():
    a = 5   # 0b0101
    b = 3   # 0b0011

    print(f"a = {a} ({bin(a)})")
    print(f"b = {b} ({bin(b)})")
    
    print("AND bit a bit (a & b):", a & b)
    print("OR bit a bit (a | b):", a | b)
    print("XOR bit a bit (a ^ b):", a ^ b)
    print("NOT bit a bit (~a):", ~a)
    print("Desplazamiento izquierdo (a << 1):", a << 1)
    print("Desplazamiento derecho (a >> 1):", a >> 1)

operadores_bit()


# === Pregunta 16. Manejo de Listas y Tuplas ===
print("\n=== Pregunta 16. Listas vs. Tuplas ===")

def listas_y_tuplas():
    lista = [1, 2, 3]
    tupla = (1, 2, 3)

    print("Lista:", lista)
    print("Tupla:", tupla)

    # Las listas son mutables
    lista.append(4)
    print("Lista modificada:", lista)

    # Las tuplas son inmutables
    try:
        tupla[3] = 4
    except TypeError as e:
        print("Error al intentar modificar una tupla:", e)

listas_y_tuplas()


# === Pregunta 17. Diccionarios y Conjuntos ===
print("\n=== Pregunta 17. Diccionarios y Conjuntos ===")

def usar_diccionarios_conjuntos():
    # Diccionario
    persona = {
        "nombre": "Ana",
        "edad": 28,
        "ciudad": "Madrid"
    }
    print("Diccionario:", persona)

    # Agregar clave-valor
    persona["profesion"] = "Ingeniera"
    print("Diccionario actualizado:", persona)

    # Iterar sobre diccionario
    print("Recorrido del diccionario:")
    for clave, valor in persona.items():
        print(f"{clave}: {valor}")

    # Conjunto
    conjunto = {1, 2, 3, 3, 4}
    print("Conjunto (sin duplicados):", conjunto)

usar_diccionarios_conjuntos()


# === Pregunta 18. Generación de Números Aleatorios ===
print("\n=== Pregunta 18. Números Aleatorios ===")

import random

def generar_aleatorios():
    print("Número aleatorio entre 1 y 10:", random.randint(1, 10))
    print("Número flotante aleatorio entre 0 y 1:", random.random())
    print("Elección aleatoria de una lista:", random.choice(["rojo", "verde", "azul"]))
    print("Barajar una lista:", random.sample([1, 2, 3, 4, 5], k=5))

generar_aleatorios()


# === Pregunta 19. Interacción con el Sistema Operativo ===
print("\n=== Pregunta 19. Interacción con el SO ===")

import os

def interactuar_so():
    print("Directorio actual:", os.getcwd())
    print("Archivos en directorio:", os.listdir())

    # Crear carpeta si no existe
    if not os.path.exists("temp"):
        os.makedirs("temp")
        print("Carpeta 'temp' creada.")
    else:
        print("La carpeta 'temp' ya existe.")

interactuar_so()


# === Pregunta 20. Pruebas Unitarias ===
print("\n=== Pregunta 20. Pruebas Unitarias ===")

import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)

if __name__ == "__main__":
    print("Ejecutando pruebas unitarias...")
    unittest.main(argv=[''], exit=False)


# === Pregunta 21. Programación Orientada a Objetos (POO) ===
print("\n=== Pregunta 21. POO - Clases y Objetos ===")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Carlos", 30)
persona1.saludar()


# === Pregunta 22. Herencia y Polimorfismo ===
print("\n=== Pregunta 22. Herencia y Polimorfismo ===")

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

def sonidos(animal):
    animal.hacer_sonido()

perro = Perro()
gato = Gato()

sonidos(perro)
sonidos(gato)


# === Pregunta 23. Programación Concurrente ===
print("\n=== Pregunta 23. Programación Concurrente ===")

import threading

def contar_hasta(n):
    for i in range(1, n+1):
        print(f"{threading.current_thread().name}: {i}")

hilo1 = threading.Thread(target=contar_hasta, args=(3,), name="Hilo 1")
hilo2 = threading.Thread(target=contar_hasta, args=(3,), name="Hilo 2")

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()


# === Pregunta 24. Seguridad Informática ===
print("\n=== Pregunta 24. Seguridad Informática ===")

import hashlib
from getpass import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = getpass("Ingresa tu contraseña para guardar su hash: ")
print("Hash de la contraseña:", hash_password(password))


# === Pregunta 25. Optimización de Código ===
print("\n=== Pregunta 25. Optimización de Código ===")

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci optimizado con memoización:")
for i in range(10):
    print(fib(i))