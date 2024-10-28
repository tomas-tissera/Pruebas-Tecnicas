import math
import unittest

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    if not isinstance(radio, (int, float)):
        raise ValueError("El radio debe ser un número.")
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

def op1():
    """Función para calcular el área del círculo a partir de un radio ingresado por el usuario."""
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

def op2():
    """Simulación de pruebas unitarias para la clase Empleado."""
    class Empleado:
        def __init__(self, nombre, salario):
            self.nombre = nombre
            self.salario = salario

        def incrementar_salario(self, incremento):
            self.salario += incremento

    class TestEmpleado(unittest.TestCase):
        def setUp(self):
            self.empleado = Empleado("John", 1000)

        def test_incrementar_salario(self):
            self.empleado.incrementar_salario(500)
            self.assertEqual(self.empleado.salario, 1500)

        def test_incrementar_salario_negativo(self):
            self.empleado.incrementar_salario(-300)
            self.assertEqual(self.empleado.salario, 700)

    # Ejecutar pruebas unitarias
    unittest.main(argv=[''], exit=False)

def op3(lista):
    """Realiza operaciones básicas sobre una lista de números."""
    # Ejemplo de suma, resta, multiplicación y división
    suma = sum(lista)
    resta = lista[0]  # Suponiendo que hay al menos un elemento
    for num in lista[1:]:
        resta -= num
    multiplicacion = math.prod(lista)
    division = lista[0]
    for num in lista[1:]:
        division /= num
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division:.2f}")

def main():
    while True:
        print("\n\n1. Calcula el área de un círculo manejando excepciones.")
        print("2. Tests unitarios para la clase Empleado.")
        print("3. Calculadora básica con una lista de números.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            op1()
        elif op == 2:
            op2()
        elif op == 3:
            lista = [1, 5, 8, 2, 6, 4, 7, 1, 2, 8, 3, 9, 7, 2, 9, 12, 13, 31]
            op3(lista)
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
