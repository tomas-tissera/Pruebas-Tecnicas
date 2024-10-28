import sqlite3
import csv

conexion = sqlite3.connect('mi_base_de_datos.db')
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario REAL
    )
''')
conexion.commit()

def insertar_empleado(nombre, puesto, salario):
    cursor.execute('''
        INSERT INTO empleados (nombre, puesto, salario)
        VALUES (?, ?, ?)
    ''', (nombre, puesto, salario))
    conexion.commit()
    print(f"Empleado {nombre} insertado con éxito.")

def actualizar_salario(id, nuevo_salario):
    cursor.execute('''
        UPDATE empleados
        SET salario = ?
        WHERE id = ?
    ''', (nuevo_salario, id))
    conexion.commit()
    print(f"Salario del empleado con ID {id} actualizado a {nuevo_salario}.")

def eliminar_empleado(id):
    cursor.execute('''
        DELETE FROM empleados
        WHERE id = ?
    ''', (id,))
    conexion.commit()
    print(f"Empleado con ID {id} eliminado con éxito.")

def mostrar_empleados():
    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)

def op3(consulta_sql, archivo_csv, nombre_db='mi_base_de_datos.db'):  
    conexion = sqlite3.connect(nombre_db)
    cursor = conexion.cursor()    
    cursor.execute(consulta_sql)    
    nombres_columnas = [descripcion[0] for descripcion in cursor.description]    
    filas = cursor.fetchall()
    
    with open(archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(nombres_columnas)
        escritor_csv.writerows(filas)

    conexion.close()
    print(f"Consulta exportada a {archivo_csv} con éxito.")

def op2(consulta_sql, nombre_db='mi_base_de_datos.db'):
    
    conexion = sqlite3.connect(nombre_db)
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute(consulta_sql)
    filas = cursor.fetchall()
    resultados = [dict(fila) for fila in filas]
    conexion.close()
    return resultados

def op1():
    
    insertar_empleado('Juan Pérez', 'Ingeniero', 50000)
    insertar_empleado('Ana Gómez', 'Analista', 45000)
    mostrar_empleados()

    actualizar_salario(1, 55000)  
    mostrar_empleados()

    eliminar_empleado(2)  
    mostrar_empleados()

    conexion.close()

def main():
    while True:
        print("\n\n1. Escribe un programa que se conecte a una base de datos **SQLite**, cree una tabla, y realice operaciones básicas (inserción, actualización, eliminación).")
        print("2. Crea una función que, dada una consulta SQL, extraiga datos de una base de datos y los devuelva en un formato legible.")
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
            consulta = "SELECT * FROM empleados"
            datos = op2(consulta)
            for registro in datos:
                print(registro)
        elif op == 3:
            consulta = "SELECT * FROM empleados"
            archivo_csv = "resultados_empleados.csv"
            op3(consulta, archivo_csv)
        elif op == 7:
            print("Adios ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
