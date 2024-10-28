from datetime import datetime, timedelta
import pytz

def op3(fecha_inicio_str, fecha_fin_str):
   
    formato = "%d/%m/%Y"
    
    try:
       
        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)

       
        if fecha_inicio > fecha_fin:
            print("La fecha de inicio debe ser anterior a la fecha de fin.")
            return

       
        lunes = []

       
        while fecha_inicio <= fecha_fin:
           
            if fecha_inicio.weekday() == 0:
                lunes.append(fecha_inicio.strftime("%d/%m/%Y")) 
           
            fecha_inicio += timedelta(days=1)

       
        if lunes:
            print("Lunes encontrados en el rango:")
            for lunes_fecha in lunes:
                print(lunes_fecha)
        else:
            print("No se encontraron lunes en el rango.")

    except ValueError as e:
        print("Error en el formato de la fecha:", e)

def op2():
    fecha = datetime.now()
    print("Fecha y hora actual:", fecha)
    print("Formato dd-mm-yy:", fecha.strftime("%d-%m-%y"))

    ts = datetime.now().timestamp()
    dt = datetime.fromtimestamp(ts, pytz.timezone('America/New_York'))
    print('ISO Date Format:', dt.strftime('%Y-%m-%d %H:%M:%S %z (%Z)'))
    
    x_int = int(dt.strftime("%Y%m%d%H%M%S"))
    print("Fecha actual como entero:", x_int)
    dt = datetime.strptime(str(x_int), '%Y%m%d%H%M%S')
    print('DateTime es:', dt)

   
    print("Hora es:", dt.strftime("%d-%b-%Y %I.%M %p"))

   
    print("Hora es:", dt.time().strftime("%H.%M %p"))

def fecha():
    entrada = input("Introduce la fecha (formato: dd/mm/yyyy): ")
   
    formato = "%d/%m/%Y"

    try:
       
        fecha = datetime.strptime(entrada, formato)
        print("Fecha ingresada:", fecha.date()) 
        return fecha
    except ValueError as e:
        print("Error en el formato de la fecha:", e)
        return None 

def op1(entrada1, entrada2):
    try:
        dias = (entrada2 - entrada1).days 
        print("Entre las fechas hay:", dias, "días.")
    except Exception as e:
        print("Error en el cálculo de días:", e)

def main():
    while True:
        print("\n\n1. Calcular cuántos días han pasado entre dos fechas dadas.")
        print("2. Imprimir la fecha y hora actual en distintos formatos.")
        print("3. Imprimir todos los lunes dentro de un rango de fechas.")
        print("7. Salir")
        
        try:
            op = int(input("Ingrese una opción:\n\t-> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue 

        if op == 1:
            print("1ra Fecha (más cercana):")
            entrada1 = fecha()
            if entrada1 is None: 
                continue
            print("2da Fecha (más alejada):")
            entrada2 = fecha()
            if entrada2 is None: 
                continue
            op1(entrada1, entrada2)
        elif op == 2:
            op2()
        elif op == 3:
            print("1ra Fecha (más alejada):")
            entrada1 = fecha()
            if entrada1 is None: 
                continue
            print("2da Fecha (más cercana):")
            entrada2 = fecha()
            if entrada2 is None: 
                continue
            op3(entrada1.strftime("%d/%m/%Y"), entrada2.strftime("%d/%m/%Y"))
        elif op == 7:
            print("Adiós ;)")
            break  
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
