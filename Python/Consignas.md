Listado con ejercicios de **pruebas técnicas sobre Python**, organizados por temas, que puedes usar para practicar o evaluar habilidades. Incluyo diferentes niveles de dificultad y descripciones breves de cada ejercicio.

### 1. **Estructuras de datos**
   - **Listas**:
     - Dado una lista de números, escribe una función que devuelva el segundo número mayor.
     - Crea una función que, dado un número entero, genere una lista con los primeros 'n' números de Fibonacci.
   - **Diccionarios**:
     - Crea una función que cuente la frecuencia de cada palabra en una cadena de texto.
     - Dado un diccionario con varios productos y sus precios, escribe una función que devuelva el producto más caro y el más barato.
   - **Conjuntos**:
     - Escribe una función que, dadas dos listas de números, devuelva los elementos comunes usando conjuntos.
     - Dado un conjunto de palabras, elimina todas las palabras duplicadas e imprime las restantes en orden alfabético.

### 2. **Manipulación de cadenas**
   - Escribe una función que invierta una cadena, manteniendo el orden de las palabras pero invirtiendo las letras de cada palabra.
   - Dada una cadena, escribe una función que compruebe si es un **palíndromo** (se lee igual de adelante hacia atrás).
   - Escribe una función que elimine todos los caracteres duplicados de una cadena.
   
### 3. **Manejo de archivos**
   - Escribe un programa que lea un archivo de texto y cuente el número de líneas, palabras y caracteres.
   - Crea un programa que lea un archivo CSV y lo convierta en un diccionario de Python, donde las claves sean los nombres de las columnas.
   - Escribe un script que copie el contenido de un archivo de texto en otro, pero elimine las líneas en blanco.

### 4. **Algoritmos de ordenación y búsqueda**
   - Implementa el algoritmo **bubble sort** y **quick sort** para ordenar una lista de números.
   - Escribe una función que implemente **búsqueda binaria** para encontrar un número en una lista ordenada.
   - Crea una función que utilice el algoritmo de **ordenación por inserción** para ordenar una lista de palabras alfabéticamente.

### 5. **Programación orientada a objetos (OOP)**
   - Crea una clase **Empleado** que tenga los atributos: nombre, salario y puesto. Incluye un método para incrementar el salario y otro para imprimir los detalles del empleado.
   - Crea una clase **CuentaBancaria** con métodos para depositar, retirar y consultar el saldo. Implementa control de saldo negativo.
   - Diseña un sistema de **Herencia** en el que una clase `Vehículo` se extienda a clases como `Coche` y `Bicicleta`, cada una con sus métodos específicos (por ejemplo, encender motor o pedalear).
   
### 6. **Funciones y recursividad**
   - Escribe una función recursiva que calcule el **factorial** de un número.
   - Implementa una función que calcule el **máximo común divisor** (MCD) de dos números usando el **algoritmo de Euclides**.
   - Crea una función recursiva que resuelva el problema de la **torre de Hanoi** con 'n' discos.

### 7. **Manejo de excepciones**
   - Escribe un programa que solicite al usuario dos números, los divida, y maneje la excepción de división por cero.
   - Crea una función que lea un archivo y maneje la excepción en caso de que el archivo no exista.
   - Escribe un script que maneje una lista de números, solicitando al usuario un índice, y maneje la excepción de índice fuera de rango.

### 8. **Concurrencia y multithreading**
   - Crea un programa que simule el procesamiento concurrente de varias tareas usando **multithreading** en Python.
   - Implementa una función que descargue múltiples páginas web simultáneamente utilizando la librería `threading` o `asyncio`.
   - Escribe un programa que calcule la suma de elementos de una lista dividiendo la lista en dos partes y procesándolas en **hilos** separados.

### 9. **Pruebas unitarias (Unit Testing)**
   - Escribe una serie de **tests unitarios** para una función que calcule el área de un círculo, manejando casos como radios negativos o no numéricos.
   - Implementa tests unitarios para la clase `Empleado` del ejercicio de OOP, verificando que los métodos de incremento salarial funcionen correctamente.
   - Crea un conjunto de pruebas para un programa que simule una calculadora básica (suma, resta, multiplicación y división).

### 10. **Manipulación de fechas y horas**
   - Escribe una función que calcule cuántos días han pasado entre dos fechas dadas.
   - Crea un programa que imprima la fecha y hora actual en distintos formatos (por ejemplo, ISO 8601).
   - Escribe una función que, dado un rango de fechas, imprima todos los lunes dentro de ese rango.

### 11. **Algoritmos avanzados**
   - Implementa el algoritmo de búsqueda de la **subcadena más larga** que no se repite en una cadena dada.
   - Escribe una función que resuelva el problema del **cambio de monedas**: dado un valor en centavos y una lista de denominaciones de monedas, encuentra la mínima cantidad de monedas necesarias para hacer el cambio.
   - Crea un algoritmo que resuelva el problema del **caminante borracho** (random walk) en una cuadrícula de 2D.

### 12. **Ejercicios con librerías externas**
   - Usa la librería `requests` para hacer una petición a una API REST y obtener datos en formato JSON. Deserializa el JSON y extrae algunos valores clave.
   - Utiliza la librería `pandas` para leer un archivo CSV y realizar estadísticas básicas como promedio, mediana y moda de una de sus columnas.
   - Crea un gráfico de barras con la librería `matplotlib` a partir de una lista de valores numéricos.
   
### 13. **Generación de gráficos y visualización**
   - Crea un script que genere una gráfica de **líneas** que muestre la evolución de una lista de valores en el tiempo.
   - Usa la librería `matplotlib` para crear un gráfico de **torta** que represente la distribución de una lista de categorías.
   - Escribe un programa que simule datos de una distribución normal y los represente mediante un **histograma**.

### 14. **Bases de datos**
   - Escribe un programa que se conecte a una base de datos **SQLite**, cree una tabla, y realice operaciones básicas (inserción, actualización, eliminación).
   - Crea una función que, dada una consulta SQL, extraiga datos de una base de datos y los devuelva en un formato legible.
   - Escribe un script que convierta los resultados de una consulta SQL a un archivo CSV.

### 15. **Optimización y eficiencia**
   - Dado un array muy grande de números enteros, escribe una función que encuentre el valor máximo y mínimo en el menor tiempo posible.
   - Implementa una función que resuelva el problema de la mochila (**Knapsack problem**) usando programación dinámica.
   - Optimiza una función que calcule el número de pasos para reducir un número entero `n` a 1, donde en cada paso puedes restar 1 o dividir entre 2 si es divisible.

Estos ejercicios cubren una amplia variedad de áreas en Python y pueden servir tanto para mejorar habilidades individuales como para preparar entrevistas técnicas.