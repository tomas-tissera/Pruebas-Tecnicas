import nbformat as nbf
import os

def crear_notebook_desde_carpetas(rutas_carpetas, nombre_notebook):
    # Crear un nuevo notebook
    nb = nbf.v4.new_notebook()
    nb.cells = []

    # Recorrer las carpetas proporcionadas
    for ruta in rutas_carpetas:
        if os.path.exists(ruta):
            for filename in os.listdir(ruta):
                file_path = os.path.join(ruta, filename)
                if filename.endswith('.py'):
                    # Leer archivo .py
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            codigo = file.read()
                            # Añadir el código al notebook
                            nb.cells.append(nbf.v4.new_code_cell(codigo))
                    except UnicodeDecodeError:
                        print(f"Error decodificando el archivo {file_path}. Intenta con un encoding diferente.")
                elif filename.endswith('.md') or filename.endswith('.txt'):
                    # Leer archivo .md o .txt
                    try:
                        with open(file_path, 'r', encoding='utf-8') as file:
                            texto = file.read()
                            # Añadir texto explicativo al notebook
                            nb.cells.append(nbf.v4.new_markdown_cell(texto))
                    except UnicodeDecodeError:
                        print(f"Error decodificando el archivo {file_path}. Intenta con un encoding diferente.")
        else:
            print(f"La carpeta {ruta} no existe.")

    # Guardar el notebook
    with open(nombre_notebook, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

    print(f"Notebook '{nombre_notebook}' creado exitosamente.")

# Ejemplo de uso
carpetas_a_leer = [
    "./1. Estructuras de datos/",
    "./10. Manipulación de fechas y horas/",
    "./11. Algoritmos avanzados/",
    "./2. Manipulación de cadenas/",
    "./3. Manejo de archivos/",
    "./4. Algoritmos de ordenación y búsqueda/",
    "./5. Programación orientada a objetos (OOP)/",
    "./6. Funciones y recursividad/",
    "./7. Manejo de excepciones/",
    "./8. Concurrencia y multithreading/",
    "./9. Pruebas unitarias (Unit Testing)/",
    "./12. Ejercicios con librerías externas/",
    "./13. Generación de gráficos y visualización/",
    "./14. Bases de datos/",
    "./15. Optimización y eficiencia/"
]
nombre_del_notebook = 'ejercicios_generados.ipynb'
crear_notebook_desde_carpetas(carpetas_a_leer, nombre_del_notebook)
