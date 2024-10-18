import csv
def op3():
    f = open("ejercicio3_sin_lineas.txt", "x")
    with open('ejercicio3.txt', 'r', encoding='utf-8') as fichero:
        lineas = fichero.readlines()
    for i in lineas:
        print(i.strip())
        if i != "\n" and i != " ":
            f.write(i)
    
def op2():
    with open('ejercicio2.csv', 'r', encoding='utf-8') as fichero:
        lector = csv.DictReader(fichero)  
        datos = [fila for fila in lector]
    for fila in datos:
        print(fila)  
    return datos 

def op1():
    with open('ejercicio1.txt', 'r', encoding='utf-8') as fichero:
        contenido = fichero.readlines()  # Lee todas las líneas del archivo

    # Contar líneas, palabras y caracteres
    num_lineas = len(contenido)
    num_palabras = sum(len(linea.split()) for linea in contenido)
    num_caracteres = sum(len(linea) for linea in contenido)

    # Mostrar los resultados
    print(f"Número de líneas: {num_lineas}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de caracteres: {num_caracteres}")

def main():
    while True:
        print("\n\n1. Implementa el algoritmo **bubble sort** y **quick sort** para ordenar una lista de números.")
        print("2. Escribe una función que implemente **búsqueda binaria** para encontrar un número en una lista ordenada.")
        print("3. Crea una función que utilice el algoritmo de **ordenación por inserción** para ordenar una lista de palabras alfabéticamente.")
        print("7. Salir")
        
        # Solicitar una nueva opción en cada iteración del bucle
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue  # Volver al inicio del bucle si la entrada no es válida

        if op == 1:
            op1()
        elif op == 2:
            op2()
        elif op == 3:
            # Asegúrate de tener la función op3 implementada
            op3()
        elif op == 7:
            print("Adios ;)")
            break  # Salir del bucle y del programa
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
