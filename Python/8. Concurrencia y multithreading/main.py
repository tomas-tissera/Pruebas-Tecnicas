import threading
import requests
import time

def procesar_suma(lista):
    print("Lista:", lista)
    suma = sum(lista)  # Uso de sum() para una mejor legibilidad
    print("Total:", suma)

def op3(lista):
    lista1 = []
    lista2 = []
    
    # Dividir la lista en pares e impares
    for i in lista:
        if i % 2 == 0:
            lista1.append(i)
        else:
            lista2.append(i)

    # Crear hilos para procesar las sumas
    thread1 = threading.Thread(target=procesar_suma, args=(lista1,))
    thread2 = threading.Thread(target=procesar_suma, args=(lista2,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

def download_page(url):
    print(f"Iniciando descarga de: {url}")
    response = requests.get(url)
    print(f"Descargado {url} con tamaño de {len(response.content)} bytes")

def download_multiple_pages_threading(urls):
    threads = []
    
    # Crear hilos para descargar múltiples páginas
    for url in urls:
        thread = threading.Thread(target=download_page, args=(url,))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

def op2():
    urls = [
        "https://www.google.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com"
    ]

    # Tiempo de descarga
    start_time = time.time()
    download_multiple_pages_threading(urls)
    end_time = time.time()

    print(f"Descarga completada en {end_time - start_time:.2f} segundos.")

def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simular un proceso
        print(f"Número: {i}")

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(1)  # Simular un proceso
        print(f"Letra: {letter}")

def op1():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

def main():
    while True:
        print("\n\n1. Simulación de procesamiento concurrente de varias tareas usando multithreading.")
        print("2. Descarga de múltiples páginas web simultáneamente utilizando threading.")
        print("3. Cálculo de la suma de elementos de una lista en hilos separados.")
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
