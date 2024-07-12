import random
import csv
import os
import time

limpiarpantalla="cls"

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez",
                "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
                "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldos = []

def generar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]

def clasificar_sueldos():
    global sueldos
    menores_800k = []
    entre_800k_2m = []
    mayores_2m = []

    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        if sueldo < 800000:
            menores_800k.append((nombre, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_2m.append((nombre, sueldo))
        else:
            mayores_2m.append((nombre, sueldo))
    
    print("\nSueldos menores a $800.000 - TOTAL:", len(menores_800k))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in menores_800k:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

    print("\nSueldos entre $800.000 y $2.000.000 - TOTAL:", len(entre_800k_2m))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in entre_800k_2m:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

    print("\nSueldos superiores a $2.000.000 - TOTAL:", len(mayores_2m))
    print("{:<20} {:<15}".format("Nombre empleado", "Sueldo"))
    for empleado in mayores_2m:
        print("{:<20} ${:<15,.2f}".format(empleado[0], empleado[1]))

def calcular_estadisticas():
    if not sueldos:
        print("Aun no se han generado los sueldos.")
        return
    
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    media_geometrica = 1
    for sueldo in sueldos:
        media_geometrica *= sueldo
    media_geometrica **= (1 / len(sueldos))

    print("\nEstadisticas de Sueldos:")
    print(f"Sueldo mas alto: ${sueldo_maximo}")
    print(f"Sueldo mas bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geometrica de sueldos: ${media_geometrica:.2f}")

def generar_reporte():
    if not sueldos:
        print("Aun no se han generado los sueldos.")
        return
    
    print("\nReporte de Sueldos:")
    print("{:<20} {:<15} {:<15} {:<15} {:<15}".format("Nombre empleado", "Sueldo Base", 
                                                    "Descuento Salud", "Descuento AFP", "Sueldo Liquido"))
    for i, sueldo in enumerate(sueldos):
        nombre = trabajadores[i]
        desc_salud = sueldo * 0.07
        desc_afp = sueldo * 0.12
        sueldo_liquido = sueldo - desc_salud - desc_afp
        print("{:<20} ${:<14,.2f} ${:<14,.2f} ${:<14,.2f} ${:<14,.2f}".format(nombre, sueldo, desc_salud, desc_afp, sueldo_liquido))

    with open('reporte_sueldos.txt', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        for i, sueldo in enumerate(sueldos):
            nombre = trabajadores[i]
            desc_salud = sueldo * 0.07
            desc_afp = sueldo * 0.12
            sueldo_liquido = sueldo - desc_salud - desc_afp
            csv_writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])

def main():
    while True:
        print("\nBienvenido al sistema de gestion de sueldos de la empresa:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            generar_sueldos()
            time.sleep(2)
            os.system(limpiarpantalla)
            print("\nSueldos aleatorios asignados exitosamente.")
        elif opcion == '2':
            clasificar_sueldos()
            time.sleep(5)
            os.system(limpiarpantalla)
        elif opcion == '3':
            calcular_estadisticas()
            time.sleep(5)
            os.system(limpiarpantalla)
        elif opcion == '4':
            generar_reporte()
            print("\nReporte de sueldos generado y exportado a reporte_sueldos.txt")
            time.sleep(5)
            os.system(limpiarpantalla)
        elif opcion == '5':
            time.sleep(2)
            os.system(limpiarpantalla)
            print("\nestas saliendo del programa..")
            print("desarrollado por Nicolas Gaete")
            print("21.923.612-3")
            break
        else:
            print("\nOpcion no valida. Por favor, seleccione una opcion del (1-5).")

main()