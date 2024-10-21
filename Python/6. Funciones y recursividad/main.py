def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"\t->Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"\t->Mover disco {n} de {origen} a {destino}")
        hanoi(n - 1, auxiliar, destino, origen)
def op2(n1 , n2):
    r = n1%n2
    if r != 0:
        n1 = n2
        n2 = r
        return op2(n1,n2)
    else:
        print(f"MCD = {n2}")

def op1(n):
    if n == 1:
        return 1
    else:
        return n  * op1(n-1)
    
def main():

    while True:
        print("\n\n1.Escribe una función recursiva que calcule el **factorial** de un número.")
        print("2. Implementa una función que calcule el **máximo común divisor** (MCD) de dos números usando el **algoritmo de Euclides**.")
        print("3. Crea una función recursiva que resuelva el problema de la **torre de Hanoi** con 'n' discos.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            n = int(input("\tingrese el numero: "))
            print("Nº = ",op1(n))
        elif op == 2:
            n1 = int(input("\tingrese el numero 1: "))
            n2 = int(input("\tingrese el numero 2: "))
            op2(n1 , n2)
        elif op == 3:
            n = int(input("Ingrese la cantidad de Discos:"))
            print("Movimientos:")
            hanoi(n, 'A', 'B', 'C')
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
