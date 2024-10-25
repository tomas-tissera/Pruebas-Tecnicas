import requests
import pandas as pd
import matplotlib.pyplot as plt
def op3():
    values = [12, 15, 20, 22, 22, 23, 25, 28, 30, 30, 32, 35, 38, 40, 42, 45, 50, 52, 55, 60]

    indices = range(len(values))

    plt.bar(indices, values, color='skyblue')

    plt.title('Gráfico de Barras de Valores Numéricos')
    plt.xlabel('Índice')
    plt.ylabel('Valor')

    plt.xticks(indices)
    plt.grid(axis='y') 
    plt.show()
    
def op2():
    df = pd.read_csv("./contenido2.csv")

    print(df,"\n")
    mean_age = df["age"].mean()
    median_age = df["age"].median()
    mode_age = df["age"].mode()[0]

    mean_math = df["math_score"].mean()
    median_math = df["math_score"].median()
    mode_math = df["math_score"].mode()[0]

    mean_english = df["english_score"].mean()
    median_english = df["english_score"].median()
    mode_english = df["english_score"].mode()[0]

    mean_science = df["science_score"].mean()
    median_science = df["science_score"].median()
    mode_science = df["science_score"].mode()[0]

    print("Estadísticas de edades:")
    print(f"Promedio de edades: {mean_age}")
    print(f"Mediana de edades: {median_age}")
    print(f"Moda de edades: {mode_age}")

    print("\nEstadísticas de calificaciones en matemáticas:")
    print(f"Promedio de calificaciones en matemáticas: {mean_math}")
    print(f"Mediana de calificaciones en matemáticas: {median_math}")
    print(f"Moda de calificaciones en matemáticas: {mode_math}")

    print("\nEstadísticas de calificaciones en inglés:")
    print(f"Promedio de calificaciones en inglés: {mean_english}")
    print(f"Mediana de calificaciones en inglés: {median_english}")
    print(f"Moda de calificaciones en inglés: {mode_english}")

    print("\nEstadísticas de calificaciones en ciencias:")
    print(f"Promedio de calificaciones en ciencias: {mean_science}")
    print(f"Mediana de calificaciones en ciencias: {median_science}")
    print(f"Moda de calificaciones en ciencias: {mode_science}")

def op1():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)

    if response.status_code == 200:

        user_data = response.json()
        

        name = user_data.get("name")
        username = user_data.get("username")
        email = user_data.get("email")
        city = user_data.get("address", {}).get("city")
        company_name = user_data.get("company", {}).get("name")


        print("Nombre:", name)
        print("Nombre de usuario:", username)
        print("Email:", email)
        print("Ciudad:", city)
        print("Empresa:", company_name)
    else:
        print(f"Error en la solicitud: {response.status_code}")
def main():
    while True:
        print("\n\n1. Usa la librería `requests` para hacer una petición a una API REST y obtener datos en formato JSON. Deserializa el JSON y extrae algunos valores clave.")
        print("2. Utiliza la librería `pandas` para leer un archivo CSV y realizar estadísticas básicas como promedio, mediana y moda de una de sus columnas.")
        print("3. Crea un gráfico de barras con la librería `matplotlib` a partir de una lista de valores numéricos.")
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
