# ####################### FUNCIONES PARA CALCULAR VOLUMEN TOTAL DEL MEDIO ##########################

def listaVCDtarget(cantPasajes):
    VCDstarget = []
    for i in range(cantPasajes):
        VCDtargetIngreso = float(input(f"Ingrese el valor de VCD target para el pasaje {i+1} (considerando que debe aumentar progresivamente el valor entre cada pasaje): ").replace(',', '.'))
        while VCDtargetIngreso < 1 or VCDtargetIngreso > 8:
            print("El valor de VCD target debe estar entre 8 y 1.")
            VCDtargetIngreso = input(f"Ingrese el valor de VCD target para el pasaje {i+1} (considerando que debe aumentar progresivamente el valor entre cada pasaje): ").replace(',', '.')
        VCDtarget = float(VCDtargetIngreso)
        VCDstarget.append(VCDtarget)
    return VCDstarget

def calcularVolFinalPasajes(VCDi, VCDstarget, cantPasajes, volInicialExp):
    listavolFinalPasajes = []
    for i in range(cantPasajes):
        volFinalPasaje = (VCDi * volInicialExp) / VCDstarget[i]
        listavolFinalPasajes.append(volFinalPasaje)
        VCDi = VCDstarget[i]
        volInicialExp = volFinalPasaje
    return listavolFinalPasajes

def calcularMedioExp(listavolFinalPasajes, volInicialExp):
    volMedioExp = sum(listavolFinalPasajes) + volInicialExp
    return volMedioExp

def agregar_solucion_adicional():
    agregar_solucion = input("¿Desea agregar una solución adicional durante la etapa productiva? (si/no): ").strip().lower()
    if agregar_solucion in ["si", "sí"]:
        volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml que se añadirá en cada agregado: "))
        
        while volumen_adicional < 50 or volumen_adicional > 500:
            print("El volumen de la solución adicional debe estar entre 50 y 500 ml.")
            volumen_adicional = float(input("Ingrese el volumen de la solución adicional en ml que se añadirá en cada agregado: "))

        periodo_sol_adicional = int(input("¿Por cuántos días agregará esta solución?: "))

        while periodo_sol_adicional < 1 or periodo_sol_adicional > 9:
            print("El periodo de la solución adicional debe ser entre 1 y 9 días.")
            periodo_sol_adicional = int(input("¿Por cuántos días agregará esta solución?: "))

        volumen_adicional_total = volumen_adicional * periodo_sol_adicional
        return volumen_adicional_total
    else:
        return 0
