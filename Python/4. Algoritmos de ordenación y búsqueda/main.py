def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ordenacion_por_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def main():
    while True:
        print("\nMenú:")
        print("1. Ordenar lista con Bubble Sort")
        print("2. Ordenar lista con Quick Sort")
        print("3. Realizar búsqueda binaria")
        print("4. Ordenar palabras alfabéticamente con Ordenación por Inserción")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            numeros = list(map(int, input("Ingresa números separados por espacios: ").split()))
            print("Lista original:", numeros)
            print("Lista ordenada (Bubble Sort):", bubble_sort(numeros))

        elif opcion == '2':
            numeros = list(map(int, input("Ingresa números separados por espacios: ").split()))
            print("Lista original:", numeros)
            print("Lista ordenada (Quick Sort):", quick_sort(numeros))

        elif opcion == '3':
            numeros_ordenados = list(map(int, input("Ingresa números ordenados separados por espacios: ").split()))
            objetivo = int(input("Ingresa el número a buscar: "))
            indice = busqueda_binaria(numeros_ordenados, objetivo)
            print(f"Búsqueda Binaria: Elemento {objetivo} {'encontrado en índice ' + str(indice) if indice != -1 else 'no encontrado'}")

        elif opcion == '4':
            palabras = input("Ingresa palabras separadas por espacios: ").split()
            print("Lista original:", palabras)
            print("Lista ordenada (Ordenación por Inserción):", ordenacion_por_insercion(palabras))

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
