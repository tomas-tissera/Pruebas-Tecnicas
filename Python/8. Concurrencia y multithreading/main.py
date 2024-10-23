import threading
import requests
import time

def procesar_suma(lista):
    print("Lista:",lista)
    suma = 0
    for i in lista:
        suma += i
    print("total:",suma) 
def op3(lista):
    lista1= []
    lista2= []
    for i in lista:
        if i % 2 == 0:
            lista1.append(i)
        else:
            lista2.append(i)

    thread1 = threading.Thread(target=procesar_suma(lista1))
    thread2 = threading.Thread(target=procesar_suma(lista2))
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
    for url in urls:
        thread = threading.Thread(target=download_page, args=(url,))
        threads.append(thread)
        thread.start()

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
        print(f"Número: {i}")
def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
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
        print("\n\n1.Crea un programa que simule el procesamiento concurrente de varias tareas usando **multithreading** en Python..")
        print("2. Implementa una función que descargue múltiples páginas web simultáneamente utilizando la librería `threading` o `asyncio`")
        print("3. Escribe un programa que calcule la suma de elementos de una lista dividiendo la lista en dos partes y procesándolas en **hilos** separados.")
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
