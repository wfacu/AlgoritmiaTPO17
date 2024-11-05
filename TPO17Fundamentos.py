# ####################### FUNCIONES PARA CALCULAR VOLUMEN TOTAL DEL MEDIO ##########################
"""
Con la combinación de las siguientes funciones se establece el volumen final a utilizar de medio de expansión,
de acuerdo a los requerimientos del cliente.
"""


def listaVCDtarget(cantPasajes):
    """
    Generar una lista en la que se almacene la VCD que se desea alcanzar en cada pasaje,
    recibe como parámetro la cantidad de pasajes, la cual es ingresada por teclado (por el usuario).
    """
    VCDstarget = []
    for i in range(cantPasajes):
        VCDtargetIngreso = input(f"Ingrese el valor de VCD target para el pasaje {i+1}: ").replace(',', '.')
        VCDtarget = float(VCDtargetIngreso)
        VCDstarget.append(VCDtarget)
    return VCDstarget

def calcularVolFinalPasajes(VCDi, VCDstarget, cantPasajes, volInicialExp):
    """
    Realizar el cálculo del volumen final que tendrá cada pasaje y generar una lista con estos volúmenes,
    recibe como parámetros VCD inicial, cantidad de pasajes y volumen inicial del primer pasaje.
    """
    listavolFinalPasajes = []
    for i in range(cantPasajes):
        volFinalPasaje = (VCDi * volInicialExp) / VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi = VCDstarget[i]
        volInicialExp = volFinalPasaje 
    return listavolFinalPasajes

def calcularMedioExp(listavolFinalPasajes, volInicialExp):
    """
    Sumar los volúmenes finales de cada pasaje para calcular el volumen total de medio de expansión necesario.
    """
    volMedioExp = sum(listavolFinalPasajes) + volInicialExp
    return volMedioExp

def agregar_solucion_adicional():
    """
    Preguntar si se desea agregar una solución adicional durante la etapa productiva.
    En caso afirmativo, preguntar el volumen de esta solución y el período de días.
    """
    agregar_solucion = input("¿Desea agregar una solución adicional durante la etapa productiva? (si/no): ").strip().lower()
    if agregar_solucion in ["si", "sí"]:
        volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml que se añadirá en cada agregado: "))
        periodo_sol_adicional = int(input("¿Por cuántos días agregará esta solución?: "))
        volumen_adicional_total = volumen_adicional * periodo_sol_adicional
        return volumen_adicional_total
    else:
        return 0  # Retornar 0 en lugar de None para simplificar cálculos posteriores

# ################################## PROGRAMA PRINCIPAL ##################################

# Listas para almacenar los datos de cada proceso
nombres_moleculas = []
dias_expansion = []
volumen_inicial_FB = []
volumen_feed_por_agregado = []
dias_totales_proceso = []
volumen_solucion_adicional = []

while True:
    print("\nBienvenido al menú principal, seleccione una opción para continuar\n")
    print("1. Cargar nuevo proceso")
    print("2. Ver procesos guardados")
    print("3. Salir")
    
    opcion = int(input("Ingrese el número de la opción seleccionada: "))
    
    if opcion == 1:
        print("\nSECCIÓN DE CARGA DE DATOS PARA GENERAR UN NUEVO PROCESO")

        # Solicitud de datos iniciales
        nombre_molecula = input("Ingrese el nombre de la molécula: ")
        VCDinicial = float(input("Ingrese el valor de VCD inicial de cada pasaje: ").replace(',', '.'))
        cantPasajes = int(input("Ingrese la cantidad de pasajes: "))
        diasxpasaje = int(input("Ingrese la cantidad de días de cada pasaje: "))
        
        calcular_dias_Exp = cantPasajes * diasxpasaje
        volInicialExp = float(input("Ingrese el volumen inicial del primer pasaje en ml: "))
        
        # Cálculo de volúmenes finales para cada pasaje
        VCDstarget = listaVCDtarget(cantPasajes)
        listavolFinalPasajes = calcularVolFinalPasajes(VCDinicial, VCDstarget, cantPasajes, volInicialExp)
        
        # Información de volúmenes mínimos y máximos permitidos por los biorreactores
        max_y_min_BRX = "BRX500: de 150 a 550; BRX1000: de 300 a 1100; BRX2000: 600 a 2200"
        print("\nConsiderando los siguientes volúmenes mínimos y máximos permitidos por los biorreactores disponibles:", max_y_min_BRX)
        
        # Determinación de volumen final en la etapa productiva
        volFinalFB = float(input("Ingrese el volumen final deseado en la etapa productiva en litros: "))
        volFinalFB = max(min(volFinalFB, 2200), 300)
        
        # Rango de valores del biorreactor según el volumen final
        if volFinalFB <= 550:
            volInicialFB = 150
        elif volFinalFB <= 1100:
            volInicialFB = 300
        else:
            volInicialFB = 600
        
        # Datos adicionales
        cantdiasFB = int(input("Ingrese los días de la etapa productiva: "))
        periodoFeed = int(input("Ingrese cada cuántos días se agregará el Feed: "))
        
        diasFB = list(range(cantdiasFB))
        diasAgregadoFeed = diasFB[1::periodoFeed]
        cantFeedPorAgregado = "{:.1f}".format((volFinalFB - volInicialFB) / len(diasAgregadoFeed))

        # Agregar datos a las listas correspondientes
        nombres_moleculas.append(nombre_molecula)
        dias_expansion.append(calcular_dias_Exp)
        volumen_inicial_FB.append(volInicialFB)
        volumen_feed_por_agregado.append(cantFeedPorAgregado)
        dias_totales_proceso.append(calcular_dias_Exp + cantdiasFB)
        volumen_solucion_adicional.append(agregar_solucion_adicional())

        print(f"\nProceso para {nombre_molecula} guardado exitosamente.\n")
        
    elif opcion == 2:
        if not nombres_moleculas:
            print("No hay procesos almacenados.")
        else:
            for i in range(len(nombres_moleculas)):
                print(f"\nProceso {i + 1}:")
                print(f"Nombre de la molécula: {nombres_moleculas[i]}")
                print(f"Días de expansión: {dias_expansion[i]}")
                print(f"Volumen inicial de Medio Productivo: {volumen_inicial_FB[i]} litros")
                print(f"Volumen de Solución Feed por agregado: {volumen_feed_por_agregado[i]} litros")
                print(f"Días totales del proceso: {dias_totales_proceso[i]}")
                if volumen_solucion_adicional[i] > 0:
                    print(f"Volumen de Solución Adicional: {volumen_solucion_adicional[i]} ml")
                else:
                    print("No se agrega solución adicional")
    
    elif opcion == 3:
        print("Saliendo del menú principal...")
        break
    
    else:
        print("Opción no válida. Por favor, intente nuevamente.")
