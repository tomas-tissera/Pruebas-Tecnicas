def op6():
    conjunto_palabras = {"manzana", "banana", "naranja", "uva", "piña", "sandía", "fresa", "kiwi"}
    palabras_ordenadas = sorted(conjunto_palabras)
    return palabras_ordenadas

def op5():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    elementos_comunes = set(lista1) & set(lista2)
    return elementos_comunes

def op4():
    productos = {
        "manzana": 0.5,
        "banana": 0.3,
        "naranja": 0.4,
        "leche": 1.2,
        "pan": 1.0,
        "huevo": 0.2,
        "arroz": 1.5,
        "pasta": 1.3,
        "tomate": 0.8,
        "pollo": 5.0
    }
    producto_caro = max(productos, key=productos.get)
    producto_barato = min(productos, key=productos.get)
    
    return (producto_barato, productos[producto_barato]), (producto_caro, productos[producto_caro])

def op3():
    texto = "La programación en Python es divertida y poderosa. Python es utilizado en diversos campos, como desarrollo web, análisis de datos, inteligencia artificial y automatización. Aprender Python puede abrir muchas oportunidades en el mundo tecnológico."
    cadena_texto = texto.lower()
    busqueda = input("Ingrese la palabra a buscar:\n-> ").lower()
    
    palabras = cadena_texto.split()
    frecuencia = palabras.count(busqueda) / len(palabras) * 100 if palabras else 0
    
    return frecuencia

def op2():
    pos = int(input('Escriba que posición quiere de la serie de Fibonacci: '))
    if pos < 0:
        return "La posición debe ser un número entero positivo."
    
    iniFibo, finFibo = 0, 1
    for x in range(pos):
        if x == 0:
            finFibo = 0
        elif x == 1:
            finFibo = 1
        else:
            finFibo, iniFibo = finFibo + iniFibo, finFibo
    
    return finFibo

def op1():
    numeros = [23, 45, 12, 78, 34, 56, 89, 1, 67, 90, 22, 11, 33]
    numeros.sort()
    return numeros[-2]

def main():
    print("\n\n1. Dado una lista de números, escribe una función que devuelva el segundo número mayor."
          "\n2. Crea una función que, dado un número entero, genere una lista con los primeros 'n' números de Fibonacci."
          "\n3. Crea una función que cuente la frecuencia de cada palabra en una cadena de texto."
          "\n4. Dado un diccionario con varios productos y sus precios, escribe una función que devuelva el producto más caro y el más barato."
          "\n5. Escribe una función que, dadas dos listas de números, devuelva los elementos comunes usando conjuntos."
          "\n6. Dado un conjunto de palabras, elimina todas las palabras duplicadas e imprime las restantes en orden alfabético."
          "\n7. Salir")
    
    while True:
        op = int(input("Ingrese una opción\n\t-> "))
        if op == 1:
            print("El segundo número mayor es:", op1())
        elif op == 2:
            print(f'Valor en la serie de Fibonacci: {op2()}')
        elif op == 3:
            print("La frecuencia es del:", op3(), "%")
        elif op == 4:
            barato, caro = op4()
            print(f"Producto más barato: {barato[0]} (${barato[1]:.2f})")
            print(f"Producto más caro: {caro[0]} (${caro[1]:.2f})")
        elif op == 5:
            print("Elementos comunes:", op5())
        elif op == 6:
            print("Palabras ordenadas:", op6())
        elif op == 7:
            print("Adiós ;)")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
