import sqlite3
import csv


def op3(n):
    pasos = [0] * (n + 1)
    for i in range(2, n + 1):
        pasos[i] = pasos[i - 1] + 1
        if i % 2 == 0:
            pasos[i] = min(pasos[i], pasos[i // 2] + 1)
    return pasos[n]

def op2(capacidad, pesos, valores, n):
    tabla = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i-1] > w:
                tabla[i][w] = tabla[i-1][w]
            else:
                tabla[i][w] = max(tabla[i-1][w], tabla[i-1][w - pesos[i-1]] + valores[i-1])    
    return tabla[n][capacidad]

def op1(array):
    if not array:  
        return None, None
    maximo = minimo = array[0]  
    for numero in array:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    return maximo, minimo
    
def main():
    while True:
        print("\n\n1. Dado un array muy grande de números enteros, escribe una función que encuentre el valor máximo y mínimo en el menor tiempo posible.")
        print("2. Inplementa una función que resuelva el problema de la mochila (**Knapsack problem**) usando programación dinámica.")
        print("3. Escribe un programa que simule datos de una distribución normal y los represente mediante un **histograma**.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            array_grande = [25947, 82475, 50429, 91313, 55001, 66851, 37612, 12244, 19465, 30264,
                67799, 14685, 33505, 47767, 74092, 28424, 35358, 59306, 50380, 77598,
                31345, 23402, 97294, 10578, 45040, 18390, 68181, 13800, 63263, 34631,
                29523, 20578, 88973, 97883, 67180, 28258, 44792, 55156, 68802, 17657,
                67132, 77767, 50498, 99386, 21351, 13771, 25181, 98325, 17682, 88925,
                59199, 18458, 97729, 76551, 45188, 46306, 28635, 46256, 73793, 67659,
                44873, 86631, 59967, 77713, 32484, 43056, 73235, 51005, 66867, 22337,
                20451, 72462, 11340, 16907, 22798, 94867, 71547, 74094, 32567, 75952,
                31802, 80419, 99293, 77641, 79942, 25447, 28236, 49916, 63747, 16857,
                31745, 84429, 88448, 72845, 70396, 54655, 83125, 61931, 14167, 15130,
                44236, 52683, 64473, 71515, 37901, 12639, 52455, 19795, 85284, 19422,
                90336, 68862, 89116, 47870, 29869, 78434, 70902, 80295, 58305, 36009]
            
            maximo, minimo = op1(array_grande)
            print(f"Valor máximo: {maximo}")
            print(f"Valor mínimo: {minimo}")
        elif op == 2:
            valores = [60, 100, 120]
            pesos = [10, 20, 30]
            capacidad = 50
            n = len(valores)
            resultado = op2(capacidad, pesos, valores, n)
            print(f"El valor máximo que se puede llevar en la mochila es: {resultado}")
        elif op == 3:
            n = int(input("Ingrese el numero a reducir:\n\t->"))
            resultado = op3(n)
            print(f"Número de pasos para reducir {n} a 1: {resultado}")
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
