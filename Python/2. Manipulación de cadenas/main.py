def op3():
    print("Op3")
    cadena = str(input("Ingresa la cadena:"))
    listado = []
    for i in cadena:
        if i in listado:
            pass
        else:
            listado.append(i)
    print(listado)

def op2():
    palabra = str(input('Escriba la palabra: '))
    lista2=[]
    palbraInver= ""
    n=-1
    for i in palabra:
        if i != ".":
            lista2.insert(n,i)
        n-=1
        palbraInver = ""
        for l in lista2:
            palbraInver += l
    if palabra == palbraInver:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
def op1():
    cadena = str(input("Ingrese la cadena: "))
    lista = ""
    n=-1
    lista2 = []
    for i in cadena:
        print(i,n)
        if i != ".":
            lista2.insert(n,i)
        n-=1
        print(lista2)
        if i == " " or i == ".":
            palabraInv = ""
            for l in lista2:
                palabraInv += l
            lista += palabraInv 
            lista += " "
            lista2 = []
    lista += "."
    print(lista)

def main():
    print("\n\n1.invierta una cadena, manteniendo el orden de las palabras.\n2.Es un palíndromo?\n3.Elimine todos los caracteres duplicados de una cadena")
    op = int(input("ingrese una opcion\n\t-> "))
    while True:
        if op == 1:
            op1()
        elif op == 2:
            op2()
        elif op == 3:
            op3()
        elif op == 4:
            op4()
        elif op == 5:
            op5()
        elif op == 6:
            op6()
        elif op == 7:
            print("Adios ;)")
            break

if __name__ == '__main__':
    main()