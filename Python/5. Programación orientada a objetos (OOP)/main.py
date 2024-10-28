class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, combustible):
        super().__init__(marca, modelo)
        self.combustible = combustible
        self.motor_encendido = False

    def encender_motor(self):
        if not self.motor_encendido:
            self.motor_encendido = True
            print("Motor encendido.")
        else:
            print("El motor ya está encendido.")

    def apagar_motor(self):
        if self.motor_encendido:
            self.motor_encendido = False
            print("Motor apagado.")
        else:
            print("El motor ya está apagado.")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_bicicleta):
        super().__init__(marca, modelo)
        self.tipo_bicicleta = tipo_bicicleta

    def pedalear(self):
        print(f"Estás pedaleando tu {self.tipo_bicicleta}.")

def op3(coche, bicicleta):
    print("\n\tSelecciona una opción:")
    print("\t1. Mostrar detalles del Coche")
    print("\t2. Encender el motor del Coche")
    print("\t3. Apagar el motor del Coche")
    print("\t4. Mostrar detalles de la Bicicleta")
    print("\t5. Pedalear la Bicicleta")
    print("\t7. Salir")

    try:
        opcion = int(input("\tIngrese una opción:\n\t\t-> "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    
    if opcion == 1:
        print(coche.mostrar_info())
    elif opcion == 2:
        coche.encender_motor()
    elif opcion == 3:
        coche.apagar_motor()
    elif opcion == 4:
        print(bicicleta.mostrar_info())
    elif opcion == 5:
        bicicleta.pedalear()
    elif opcion == 7:
        print("Saliendo del sistema.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return f"Monto de la cuenta: ${self.saldo}"

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if (self.saldo - cantidad) < -100:
            print(f"No puedes retirar más dinero (superas el límite negativo: {self.saldo})")
        else:
            self.saldo -= cantidad

def op2(b1):
    print(b1)
    print("\t0. Consultar saldo")
    print("\t1. Depositar dinero")
    print("\t2. Retirar dinero")    
    print("\t7. Salir")
    
    try:
        opcion = int(input("\t-> Ingrese una opción:\n\t\t-> "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    if opcion == 0:
        print(b1)  
    elif opcion == 1:
        try:
            cantidad = float(input("Ingrese la cantidad a depositar -> $"))
            b1.depositar(cantidad)
            print(f"Saldo actualizado: {b1.saldo}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == 2:
        try:
            cantidad = float(input("Ingrese la cantidad a retirar -> $"))
            b1.retirar(cantidad)
            print(f"Saldo después del retiro: {b1.saldo}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif opcion == 7:
        print("Saliendo del sistema.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")

class Empleado:
    def __init__(self, nombre, salario, puesto):
        self.nombre = nombre
        self.salario = salario
        self.puesto = puesto

    def __str__(self):
        return f"{self.nombre} (${self.salario}) - {self.puesto}"

    def incrementar_salario(self, cantidad):
        self.salario += cantidad  # Cambiar el salario sumando en vez de reemplazando

def op1(p1):
    op1_1 = input("¿Desea modificar el salario? (1=Sí, 0=No)\n\t-> ")
    
    if op1_1 == '1':
        try:
            cantidad = float(input("Ingrese la cantidad a incrementar -> $"))
            p1.incrementar_salario(cantidad)
            print(f"Salario actualizado: {p1}")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("Ok. No se ha modificado el salario.")

def main():
    p1 = Empleado("John", 600, "Gerente")
    b1 = CuentaBancaria(800)
    coche = Coche("Toyota", "Corolla", "Gasolina")
    bicicleta = Bicicleta("Giant", "Escape 3", "bicicleta de montaña")

    while True:
        print("\n\n1. Ver empleado y salario.")
        print("2. Ver cuenta bancaria (depositar, retirar y consultar saldo).")
        print("3. Ver vehículos.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            print(p1)
            op1(p1)
        elif op == 2:
            op2(b1)
        elif op == 3:
            op3(coche, bicicleta)
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
