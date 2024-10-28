import numpy as np
import matplotlib.pyplot as plt

def op1():
    # User input for time and values
    tiempo = input("Ingrese los meses separados por comas (por ejemplo: Enero,Febrero,Marzo): ").split(',')
    valores = list(map(int, input("Ingrese los valores correspondientes separados por comas: ").split(',')))

    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, valores, marker='o', color='b', linestyle='-', linewidth=2)
    plt.title('Evolución de Valores en el Tiempo')
    plt.xlabel('Tiempo')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.show()

def op2():
    # User input for categories and values
    categorias = input("Ingrese las categorías separadas por comas: ").split(',')
    valores = list(map(int, input("Ingrese los valores correspondientes separados por comas: ").split(',')))

    plt.figure(figsize=(8, 6))
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Categorías')
    plt.show()

def op3():
    # User input for mean and std deviation
    media = float(input("Ingrese la media de la distribución normal: "))     
    desviacion = float(input("Ingrese la desviación estándar de la distribución normal: "))
    num_datos = int(input("Ingrese el número de datos a simular: ")) 
    
    datos = np.random.normal(media, desviacion, num_datos)

    plt.figure(figsize=(10, 6))
    plt.hist(datos, bins=30, color='skyblue', edgecolor='black')
    plt.title('Histograma de Datos Simulados de una Distribución Normal')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

def main():
    while True:
        print("\n\n1. Crea un script que genere una gráfica de **líneas** que muestre la evolución de una lista de valores en el tiempo.")
        print("2. Usa la librería `matplotlib` para crear un gráfico de **torta** que represente la distribución de una lista de categorías.")
        print("3. Escribe un programa que simule datos de una distribución normal y los represente mediante un **histograma**.")
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
            op3()
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
