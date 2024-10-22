def op3(lista):
    while True:
        try:
            indice = int(input("\tIngrese el índice del elemento al que desea acceder: "))
            return lista[indice]
        except ValueError:
            print("\tPor favor, ingrese un número entero válido.")
        except IndexError:
            print(f"\tEl índice {indice} está fuera de rango. La lista tiene {len(lista)} elementos.")

def op2(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")

def op1(n1,n2):
    if n2 == 0:
        print("\nERROR no se puede dividir en 0")
    else:
        print(n1/n2)
    
def main():

    while True:
        print("\n\n1.Escribe un programa que solicite al usuario dos números, los divida, y maneje la excepción de división por cero.")
        print("2. Crea una función que lea un archivo y maneje la excepción en caso de que el archivo no exista.")
        print("3. Escribe un script que maneje una lista de números, solicitando al usuario un índice, y maneje la excepción de índice fuera de rango.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            
            n1 = int(input("Ingrese el 1er numero: "))
            n2 = int(input("Ingrese el 2do numero: "))
            op1(n1,n2)
        elif op == 2:
            nombre = str(input("Ingresa el nombre del arhivo con su terminacion (.bat-.csv-.txt):\n->"))
            op2(nombre)
        elif op == 3:
            mi_lista = [10, 20, 30, 40]
            print("\t\t->",op3(mi_lista))
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
