def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"\t-> Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"\t-> Mover disco {n} de {origen} a {destino}")
        hanoi(n - 1, auxiliar, destino, origen)

def mcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

def op2(n1, n2):
    resultado = mcd(n1, n2)
    print(f"MCD = {resultado}")

def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def op1(n):
    return factorial(n)

def main():
    while True:
        print("\n\n1. Escribe una función recursiva que calcule el **factorial** de un número.")
        print("2. Implementa una función que calcule el **máximo común divisor** (MCD) de dos números usando el **algoritmo de Euclides**.")
        print("3. Crea una función recursiva que resuelva el problema de la **torre de Hanoi** con 'n' discos.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            n = int(input("\tingrese el número: "))
            if n < 0:
                print("Por favor, ingrese un número no negativo.")
                continue
            print("Factorial =", op1(n))
        elif op == 2:
            n1 = int(input("\tingrese el número 1: "))
            n2 = int(input("\tingrese el número 2: "))
            op2(n1, n2)
        elif op == 3:
            n = int(input("Ingrese la cantidad de discos: "))
            if n < 1:
                print("Por favor, ingrese un número de discos mayor que cero.")
                continue
            print("Movimientos:")
            hanoi(n, 'A', 'B', 'C')
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
