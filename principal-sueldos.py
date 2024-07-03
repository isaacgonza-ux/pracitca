import sueldos as py
eleccion  = 0
while eleccion != 4:
    flag = True
    while flag == True:
        try:
            eleccion = int(input("""
            1.-Registrar trabajador
            2.-Lista de todos los trabajadores
            3.-Imprimir planilla de sueldos
            4.-Salir
            --> """))
            if eleccion < 1 or eleccion > 4:
                print("Fuera de rango")
        except:
            print("Solo números")
        else:
            flag = False
    
    if eleccion == 1:
        print("="*60)
        py.registrar_trabajador()

    elif eleccion == 2:
        print("="*60)
        py.todos_los_trabajadores()

    elif eleccion == 3:
        print("="*60)
        py.imprimir_planillas()

    elif eleccion == 4:
        print("="*60)
        print("Saliendo.............")
