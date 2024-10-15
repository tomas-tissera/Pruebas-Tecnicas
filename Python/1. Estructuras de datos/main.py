def op6():
    conjunto_palabras = {"manzana", "banana", "naranja", "uva", "piña", "sandía", "fresa", "banana", "manzana", "kiwi"}
    palabras_ordenadas = sorted(conjunto_palabras)
    print(palabras_ordenadas)
def op5():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    lista1_2 = conjunto1 & conjunto2
    print(lista1_2)
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
    precio_caro = productos[producto_caro]
    
    # Encontrar el producto más barato
    producto_barato = min(productos, key=productos.get)
    precio_barato = productos[producto_barato]
    
    print("barato:",precio_barato,"\ncaro:",precio_caro)
def op3():
    print("Op3")
    texto = "La programación en Python es divertida y poderosa. Python es utilizado en diversos campos, como desarrollo web, análisis de datos, inteligencia artificial y automatización. Aprender Python puede abrir muchas oportunidades en el mundo tecnológico."
    cadena_texto = texto.lower()
    palabra = ""
    buqueda = input("Ingrese la palabra a buscar:\n->")
    bus = buqueda.lower()
    con = 0
    con_palabras = 0
    frecuencia = 0
    for l in cadena_texto:
        if l != " ":
            palabra+=l
        else:
            palabra = ""
            con_palabras+=1
        if palabra == bus:
            con += 1
    frecuencia = con_palabras / con
    print("La frecuencia es del:",frecuencia,"%")
def op2():
    pos = int(input('Escriba que posición quiere de la serie de Fibonacci: '))
    iniFibo = 0
    finFibo = 1
    for x in range(0,pos):
        if x == 0:
            finFibo = 0
        elif x == 1:
            finFibo = 1
        sum = finFibo
        finFibo = finFibo + iniFibo
        iniFibo = finFibo - iniFibo
    print(f'\nPosición Final: {x+1:>4} -- Valor en la serie de Fibonacci:  {sum:>10}  ')
def op1():
    print("Opcion 1")
    numeros = [23, 45, 12, 78, 34, 56, 89, 1, 67, 90, 22, 11, 33]
    print("Numeros:",numeros)
    numeros.sort()
    print("El segundo número mayor es: ",numeros[-2])
    print("*-*"*20)

def main():
    print("\n\n1.Dado una lista de números, escribe una función que devuelva el segundo número mayor.\n2.Crea una función que, dado un número entero, genere una lista con los primeros 'n' números de Fibonacci\n3.Crea una función que cuente la frecuencia de cada palabra en una cadena de texto.\n4.Dado un diccionario con varios productos y sus precios, escribe una función que devuelva el producto más caro y el más barato.\n5.Escribe una función que, dadas dos listas de números, devuelva los elementos comunes usando conjuntos.\n6.Dado un conjunto de palabras, elimina todas las palabras duplicadas e imprime las restantes en orden alfabético.\n7.Salir")
    op = int(input("ingrese una opcion\n\t-> "))
    while True:
        if op == 1:
            op1()
        elif op == 2:
            op2()
        elif op == 3:
            op3()
        elif op == 4:
            op4()
        elif op == 5:
            op5()
        elif op == 6:
            op6()
        elif op == 7:
            print("Adios ;)")
            break

if __name__ == '__main__':
    main()