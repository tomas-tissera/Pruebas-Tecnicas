def op3():
    cadena = input("Ingresa la cadena: ")
    listado = []
    for i in cadena:
        if i not in listado:
            listado.append(i)
    return listado

def op2():
    palabra = input('Escriba la palabra: ')
    palabra_invertida = palabra[::-1]
    
    if palabra == palabra_invertida:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"

def op1():
    cadena = input("Ingrese la cadena: ")
    palabras = cadena.split()
    palabras_invertidas = ' '.join(palabra[::-1] for palabra in palabras)
    return palabras_invertidas

def main():
    print("\n\n1. Invierta una cadena, manteniendo el orden de las palabras."
          "\n2. ¿Es un palíndromo?"
          "\n3. Elimine todos los caracteres duplicados de una cadena"
          "\n4. Salir")
    
    while True:
        op = int(input("Ingrese una opción\n\t-> "))
        if op == 1:
            print("Cadena invertida:", op1())
        elif op == 2:
            print(op2())
        elif op == 3:
            print("Caracteres únicos:", op3())
        elif op == 4:
            print("Adiós ;)")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
