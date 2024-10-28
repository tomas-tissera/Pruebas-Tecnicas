import csv

def op3():
    # Crear un nuevo archivo solo si no existe, de lo contrario, se manejan las excepciones
    try:
        with open("ejercicio3_sin_lineas.txt", "x") as f:
            with open('ejercicio3.txt', 'r', encoding='utf-8') as fichero:
                lineas = fichero.readlines()
                for i in lineas:
                    if i.strip():  # Eliminar líneas en blanco
                        f.write(i)
                        print(i.strip())  # Mostrar líneas no vacías
    except FileExistsError:
        print("El archivo 'ejercicio3_sin_lineas.txt' ya existe.")

def op2():
    with open('ejercicio2.csv', 'r', encoding='utf-8') as fichero:
        lector = csv.DictReader(fichero)  
        datos = [fila for fila in lector]
    
    for fila in datos:
        print(fila)
    
    return datos

def op1():
    with open('ejercicio1.txt', 'r', encoding='utf-8') as fichero:
        contenido = fichero.readlines()  
    
    num_lineas = len(contenido)
    num_palabras = sum(len(linea.split()) for linea in contenido)
    num_caracteres = sum(len(linea) for linea in contenido)
    
    print(f"Número de líneas: {num_lineas}")
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de caracteres: {num_caracteres}")

def main():
    while True:
        print("\n\n1. Leer archivo de texto y mostrar el contenido.")
        print("2. Leer un archivo CSV y convertirlo en un diccionario.")
        print("3. Copiar archivo de texto eliminando líneas en blanco.")
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
            op3()
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
