#################################FUNCIONES PARA CALCULAR VOLUMEN TOTAL DEL MEDIO################################################
""""
Con la combinación de las siguientes funciones se establece el volúmen final a utilizar de medio de expansión, 
de acuerdo a los requerimientos del cliente.
"""
def listaVCDtarget(cantPasajes):
    """"
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
    """"
    Realizar el cálculo del volumen final que tendrá cada pasaje y a su vez generar una lista en la que se almacenen estos volúmenes,
    recibe como parámetro VCD inicial de la etapa de expansión, cantidad de pasajes de la etapa de expansión y volúmen inicial del primer pasaje, todos ingresados por teclado (por el usuario); y VCD target (objetivo) que cada pasaje deberá alcanzar, este último dato se toma de la lista generada en la función anterior (listaVCDtarget).
    """
    listavolFinalPasajes = []
    for i in range(cantPasajes):
        volFinalPasaje = (VCDi * volInicialExp) / VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi = VCDstarget[i]
        volInicialExp = volFinalPasaje 
    return listavolFinalPasajes

def calcularMedioExp(listavolFinalPasajes, volInicialExp):
    """"
    Sumar los pesos de los volumenes finales de cada pasaje para calcular el volumen final de medio de expansión necesario, 
    recibe como parámetro la lista de los volúmenes de los pasajes calculados en la función anterior (calcularVolFinalPasajes).
    """
    volMedioExp = sum(listavolFinalPasajes) + volInicialExp
    return volMedioExp

#######################################################################################
def agregar_solucion_adicional():
    """"
    Preguntar si se desea agregar una solución adicional durante la etapa productiva, 
    en caso afirmativo consultar qué volumen de esta solución se agregará.
    """
    agregar_solucion = input("¿Desea agregar una solución adicional durante la etapa productiva? (si/no): ").strip().lower().replace('í', 'i') # Comandos para pasar la respuesta ingresada por teclado a minúscula y remover el acento de ser necesario.
    if agregar_solucion == "si" or agregar_solucion == "sí" or agregar_solucion == "Si" or agregar_solucion == "Sí":
        volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml que se añadirá en cada agregado: "))
        periodo_sol_adicional = float(input("¿Por cuantos días agregará esta solución?: "))
        volumen_adicional_total = volumen_adicional * periodo_sol_adicional
        return volumen_adicional_total
    else:
        return None

#######################################################################################
def cargar_datos_proceso(nombre_molecula, volInicialFB, cantdiasFB, calcular_dias_Exp, cantFeedPorAgregado):
    """"
    Crear una lista que será completado con las características de la molécula.
    Parámetros de ingreso: nombre_molecula,volInicialFB,cantdiasFB,calcular_dias_Exp.
    """
    proceso = []

    proceso.append(nombre_molecula)
    
    proceso.append("{:.1f}".format(calcular_dias_Exp))

    proceso.append(volInicialFB)
    
    proceso.append(cantFeedPorAgregado)

    proceso.append(calcular_dias_Exp + cantdiasFB)
        
    volumen_sol_adicional = agregar_solucion_adicional()
    if volumen_sol_adicional is not None:
        proceso.append("{:.1f}".format(volumen_sol_adicional))
    else:
        proceso.append("No se agrega solución adicional")
    return proceso         
#######################################################################################

def mostrar_proceso(proceso):
    """
    Mostrar los detalles de un proceso guardados en la función "cargar_datos_proceso" como valores de las claves.
    """
    print(f"Nombre de la molécula: {proceso[0]}")
    print(f"Duración del Proceso: {proceso[4]}")
    print(f"Volumen de Medio de Expansión necesario: {proceso[1]} ml")
    print(f"Volumen de Medio Productivo con el que se debe iniciar el proceso: {proceso[2]} litros")
    print(f"Volumen de Solución Feed a añadir en cada agregado: {proceso[3]} litros")
    print(f"Volumen de Solución Adicional: {proceso[5]} ml")
    
#######################################################################################
"""
#Programa Principal bloque 1= Menu interactivo principal:

"""
procesos_guardados = []
while True:
        print("\nBienvenido al menú principal, seleccione una opción para continuar\n")
        print("1. Cargar nuevo proceso")
        print("2. Ver procesos guardados")
        print("3. Salir")
        
        opcion = int(input("Ingrese el número de la opción seleccionada: "))
        
        if opcion == 1:
            print("SE ENCUENTRA EN LA SECCIÓN DE CARGA DE DATOS PARA GENERAR UN NUEVO PROCESO")
            """
            Datos de ingresos, llamados de funciones y funciones lambda necesarios:
            """
            nombre_molecula = input("Ingrese el nombre de la molécula: ")

            VCDinicial = input("Ingrese el valor de VCD con la que desea iniciar cada pasaje: ").replace(',', '.')
            VCDi = float(VCDinicial)

            cantPasajes = int(input("Ingrese la cantidad de pasajes que desea efectuar durante la etapa de expansión: "))
            diasxpasaje = int(input("Ingrese la cantidad de días que desea que tenga cada pasaje: "))

            calcular_dias_Exp = cantPasajes * diasxpasaje

            volInicialExp = int(input("Ingrese el volumen inicial del primer pasaje, en ml: "))
            VCDstarget = listaVCDtarget(cantPasajes)
            ListavolFinalPasajes = calcularVolFinalPasajes(VCDi,VCDstarget,cantPasajes,volInicialExp)

            max_y_min_BRX = ("BRX500: de 150 a 550; BRX1000: de 300 a 1100; BRX2000: 600 a 2200")
        
            print("Considerando los siguientes volúmenes mínimos y máximos permitidos por los biorreactores disponibles: ", max_y_min_BRX)
            
            #Bloque para determinar el volumen inicial de la etapa productiva:
            volFinalFB = int(input("Ingrese el vólumen final al cual desea llegar en su etapa productiva en litros: "))
            volFinalFB = max(min(volFinalFB, 2200), 300)
            Bandera = True
            while Bandera:
                if volFinalFB <= 550 and volFinalFB >= 300:
                    volInicialFB = 150
                    Bandera = False
                elif volFinalFB > 550 and volFinalFB <= 1100:
                    volInicialFB = 300
                    Bandera = False
                elif volFinalFB > 1100 and volFinalFB <= 2200:
                    volInicialFB = 600
                    Bandera = False  # Salir del bucle si el valor es válido
                else:
                    print("El valor de volúmen Final ingresado no está dentro del rango permitido.")
                    volFinalFB = float(input("Ingrese un nuevo valor para volFinalFB dentro del rango permitido: "))
                    volFinalFB = max(min(volFinalFB, 2200), 300)
            cantdiasFB = int(input("Ingrese la cantidad de días de la etapa productiva que tendrá su proceso: "))
            periodoFeed = int(input("Ingrese cada cuántos días se agregará el Feed: "))
            
            """
            Función lambda para armar una lista con números en un rango de 0 hasta n-1 de acuerdo a la cantidad de días de la etapa productiva: 
            
            """
            diasFB = list(range(cantdiasFB))
            
            diasAgregadoFeed = diasFB[1::periodoFeed]
            cantFeedPorAgregado = "{:.1f}".format((volFinalFB-volInicialFB) / (len(diasAgregadoFeed))) 
            
        
            proceso = cargar_datos_proceso(nombre_molecula, volInicialFB, cantdiasFB, calcular_dias_Exp, cantFeedPorAgregado)
        
            procesos_guardados.append(proceso)
            print(f"Proceso para {proceso[0]} guardado exitosamente.\n")          
            
        elif opcion == 2:
            if not procesos_guardados:
                print("No hay procesos almacenados.")
            else:
                for i, proceso in enumerate(procesos_guardados):
                    print(f"\nProceso {i + 1}:")
                mostrar_proceso(proceso)
        
        
        elif opcion == 3:
            print("Saliendo del menú principal :)...")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

#######################################################################################