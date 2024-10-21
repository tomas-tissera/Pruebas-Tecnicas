import csv
def op3(arreglo):
    print("Arreglo:",arreglo)
    for i in range(len(arreglo) - 1):        # <-- bucle padre
        menor = i # primer elemento por default será el mínimo

        for j in range(i + 1, len(arreglo)): # <-- bucle hijo
            if arreglo[j] < arreglo[menor]:
                menor = j

        if menor != i:
            arreglo[menor], arreglo[i] = arreglo[i], arreglo[menor]
    print("Arreglo Odenado:",arreglo)
    
def op2(lista, _buscado):
    tamano_lista = len(lista)
    for actual in range(0, tamano_lista):
        print("actual,",actual,"/lista[actual],",lista[actual],"/_buscado,",_buscado)

        if (lista[actual] == _buscado):
            print("\n\t¡Encontrado!\n")
            return actual

    return -1

def op1():
    lista_numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista:",lista_numeros) 
    bubble_sort(lista_numeros)
    print("quick_sort",quick_sort(lista_numeros))
def bubble_sort(lista_numeros):
    arr = lista_numeros
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print("bubble_sort",arr)
def quick_sort(lista_numeros):
    arr = lista_numeros
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def main():
    while True:
        print("\n\n1. Implementa el algoritmo **bubble sort** y **quick sort** para ordenar una lista de números.")
        print("2. Escribe una función que implemente **búsqueda binaria** para encontrar un número en una lista ordenada.")
        print("3. Crea una función que utilice el algoritmo de **ordenación por inserción** para ordenar una lista de palabras alfabéticamente.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            op1()
        elif op == 2:
            lista  = [0,1,2,3,4,5,6,7,8,9]
            numB =  int(input("ingrese el numero a buscar:"))
            print("Esta en la posicion Nº",op2(lista,numB)," de la lista")
        elif op == 3:
            a = [22, 25, 12, 64, 11]
            op3(a)
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
