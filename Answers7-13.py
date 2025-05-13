# === Pregunta 7. Manipulación de Cadenas de Caracteres ===
print("\n=== Pregunta 7. Manipulación de Cadenas de Caracteres ===")

def manipular_cadena():
    cadena = "Bienvenidos al curso de Programación Estructurada"
    print("Cadena original:", cadena)
    
    # Convertir a minúsculas
    print("En minúsculas:", cadena.lower())
    
    # Convertir a mayúsculas
    print("En mayúsculas:", cadena.upper())
    
    # Dividir la cadena en palabras
    palabras = cadena.split()
    print("Palabras separadas:", palabras)
    
    # Reemplazar parte de la cadena
    nueva_cadena = cadena.replace("Programación Estructurada", "Python")
    print("Cadena modificada:", nueva_cadena)

    # Concatenar cadenas
    saludo = "Hola"
    nombre = input("Ingresa tu nombre: ")
    mensaje = saludo + ", " + nombre + ". ¡Esperamos que disfrutes el curso!"
    print(mensaje)

manipular_cadena()


# === Pregunta 8. Manejo de Fechas con datetime ===
print("\n=== Pregunta 8. Manejo de Fechas ===")

from datetime import datetime

def manejar_fecha():
    ahora = datetime.now()
    print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Mostrar partes de la fecha
    print("Año:", ahora.year)
    print("Mes:", ahora.month)
    print("Día:", ahora.day)
    print("Hora:", ahora.hour)
    print("Minuto:", ahora.minute)

manejar_fecha()


# === Pregunta 9. Lectura y Escritura de Ficheros ===
print("\n=== Pregunta 9. Ficheros - Escritura y Lectura ===")

def gestionar_fichero():
    # Escribir en un fichero
    with open("datos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Este es un ejemplo de escritura en fichero.\n")
        archivo.write("Línea 2: Hola Mundo\n")
        archivo.write("Línea 3: Bienvenido a Python\n")
    
    print("Fichero creado y escrito correctamente.")
    
    # Leer el fichero línea por línea (simula feof)
    print("\nContenido del fichero:")
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        while True:
            linea = archivo.readline()
            if not linea:
                break  # Fin del fichero
            print(linea.strip())

gestionar_fichero()


# === Pregunta 10. Algoritmia - Máximo de Tres Números ===
print("\n=== Pregunta 10. Máximo de Tres Números ===")

def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

resultado = maximo_de_tres(num1, num2, num3)
print(f"El máximo de {num1}, {num2} y {num3} es: {resultado}")


# === Pregunta 11. Conversiones de Tipos ===
print("\n=== Pregunta 11. Ejemplos de Conversión de Tipos ===")

def conversiones_tipo():
    valor_str = "123"
    valor_int = int(valor_str)
    print(f"String '{valor_str}' convertido a entero:", valor_int)
    
    valor_float = 3.1416
    valor_int_truncado = int(valor_float)
    print(f"Float {valor_float} convertido a entero (truncado):", valor_int_truncado)
    
    valor_bool = bool(0)
    print("Entero 0 convertido a booleano:", valor_bool)
    
    valor_lista = list("hola")
    print("String 'hola' convertido a lista:", valor_lista)

conversiones_tipo()


# === Pregunta 12. Manejo de Errores (Excepciones) ===
print("\n=== Pregunta 12. Manejo de Excepciones ===")

def manejar_excepciones():
    try:
        dividendo = int(input("Ingresa un dividendo: "))
        divisor = int(input("Ingresa un divisor: "))
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except ValueError:
        print("Error: Solo se permiten números enteros.")
    else:
        print(f"El resultado es: {resultado}")
    finally:
        print("Operación finalizada.")

manejar_excepciones()


# === Pregunta 13. Uso de Enumerados ===
print("\n=== Pregunta 13. Uso de Enumerados ===")

from enum import Enum

class DiasSemana(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

def mostrar_dias():
    print("Enumerados de días de la semana:\n")
    for dia in DiasSemana:
        print(f"{dia.name}: {dia.value}")

mostrar_dias()