import random
import os
import time

width = 20
height = 20
x, y = width // 2, height // 2

def create_area():
    return [['.' for _ in range(width)] for _ in range(height)]
def display_area(area, x, y):
    os.system('cls' if os.name == 'nt' else 'clear') 
    area[y][x] = 'X'  
    for row in area:
        print(' '.join(row))
    area[y][x] = '.' 
def op3(num_steps):
    global x, y
    area = create_area()
    
    for _ in range(num_steps):
        display_area(area, x, y)
        time.sleep(0.1) 
        
        
        move = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  
        x += move[0]
        y += move[1]
        
        
        x = max(0, min(width - 1, x))
        y = max(0, min(height - 1, y))

def op2(centavos, denominaciones):
    dp = [float('inf')] * (centavos + 1)
    dp[0] = 0
    for i in range(1, centavos + 1):
        for moneda in denominaciones:
            if i >= moneda:
                dp[i] = min(dp[i], dp[i - moneda] + 1)
    return dp[centavos] if dp[centavos] != float('inf') else -1

def op1(cadena):
    n = len(cadena)
    if n == 0:
        return 0

    
    ultimo_indice = {}
    max_longitud = 0
    inicio = 0

    for i in range(n):
        if cadena[i] in ultimo_indice and ultimo_indice[cadena[i]] >= inicio:
            
            inicio = ultimo_indice[cadena[i]] + 1

        
        ultimo_indice[cadena[i]] = i

        
        max_longitud = max(max_longitud, i - inicio + 1)

    return max_longitud

def main():
    while True:
        print("\n\n1. Implementa el algoritmo de búsqueda de la **subcadena más larga** que no se repite en una cadena dada.")
        print("2. Escribe una función que resuelva el problema del **cambio de monedas**: dado un valor en centavos y una lista de denominaciones de monedas, encuentra la mínima cantidad de monedas necesarias para hacer el cambio.")
        print("3. caminante borracho (random walk).")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            cadena = "abcabcbb"
            resultado = op1(cadena)
            print("La longitud de la subcadena más larga sin repetir es:", resultado)
        elif op == 2:
            print("Listado de Monedas:")
            denominaciones = [1, 5, 10, 25]  
            valor = int(input("Ingrese la Cantidad que posee:"))
            resultado = op2(valor, denominaciones)
            print(f"El mínimo número de monedas necesarias para {valor} centavos es: {resultado}")

        elif op == 3:
            
            num_steps = int(input("Ingrese la Cantidad de pasos:\n->"))
            op3(num_steps)
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
