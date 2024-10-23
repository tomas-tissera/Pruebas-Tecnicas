import math


def op3(lista):
    lista1= []

def op2():
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ]

    
def op1(radio):
    if not isinstance(radio, (int, float)):
        raise ValueError("El radio debe ser un número.")
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)
    
def main():
    while True:
        print("\n\n1.Escribe una serie de **tests unitarios** para una función que calcule el área de un círculo, manejando casos como radios negativos o no numéricos.")
        print("2. Implementa tests unitarios para la clase `Empleado` del ejercicio de OOP, verificando que los métodos de incremento salarial funcionen correctamente.")
        print("3. Crea un conjunto de pruebas para un programa que simule una calculadora básica (suma, resta, multiplicación y división).")
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
            lista =[1,5,8,2,6,4,7,1,2,8,3,9,7,2,9,12,13,31]
            op3(lista)
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
