def op3(lista):
    while True:
        try:
            # Solicitar al usuario un índice para acceder a la lista
            indice = int(input("\tIngrese el índice del elemento al que desea acceder: "))
            return lista[indice]
        except ValueError:
            print("\tPor favor, ingrese un número entero válido.")
        except IndexError:
            print(f"\tEl índice {indice} está fuera de rango. La lista tiene {len(lista)} elementos.")

def op2(nombre_archivo):
    try:
        # Abrir y leer el archivo
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")

def op1(n1, n2):
    # Manejar la división y verificar la división por cero
    try:
        resultado = n1 / n2
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError:
        print("\nERROR: No se puede dividir entre cero.")

def main():
    while True:
        print("\n\n1. Solicitar al usuario dos números, dividirlos y manejar la excepción de división por cero.")
        print("2. Leer un archivo y manejar la excepción en caso de que el archivo no exista.")
        print("3. Manejar una lista de números, solicitando al usuario un índice, y manejar la excepción de índice fuera de rango.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            try:
                n1 = int(input("Ingrese el 1er número: "))
                n2 = int(input("Ingrese el 2do número: "))
                op1(n1, n2)
            except ValueError:
                print("Por favor, ingrese solo números enteros.")
        elif op == 2:
            nombre = input("Ingresa el nombre del archivo con su extensión (.bat, .csv, .txt):\n-> ")
            op2(nombre)
        elif op == 3:
            mi_lista = [10, 20, 30, 40]
            print("\t\t->", op3(mi_lista))
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
