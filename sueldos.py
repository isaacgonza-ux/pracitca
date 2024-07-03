import csv

lista_todos_trabajadores = []
cargos = ["ceo","jefe","desarrollador","analista"]

def registrar_trabajador():
    nombre   =input("Ingrese su nombre: ")
    while len(nombre) == 0:
        print("El nombre no puede estar vacio")
        nombre = input("Ingrese su nombre: ")
    apellido =input("Ingrese su apellido: ")
    while len(apellido) == 0:
        print("El apellido no puede estar vacio")
        apellido = input("Ingresw su apellido: ")
    print("Cargos disponibles: Ceo, Jefe,desarrollador,analista")
    cargo    =input("Ingrese su cargo: ")
    while cargo not in cargos:
        print("El cargo no es valido")
        cargo = input("Ingrese su cargo: ")
    sueldo_bruto=int(input("Ingrese su sueldo bruto: "))
    while (sueldo_bruto) < 0:
        print("El sueldo bruto no puede ser negativo")
        sueldo_bruto = int(input("Ingrese su sueldo bruto: "))
    desc_salud = sueldo_bruto * 0.07
    desc_afp =sueldo_bruto * 0.12
    pago_liquido = sueldo_bruto - desc_salud -desc_afp
    trabajador = {
     "nombre":nombre,
        "apellido":apellido,
        "cargo":cargo,
        "sueldo liquido":pago_liquido
        }
    if len(trabajador) == 0:
        print("Faltan datos ")
    else:
        lista_todos_trabajadores.append(trabajador)
        print("Registro exitoso")

def todos_los_trabajadores():
    if len(lista_todos_trabajadores) == 0:
        print("No hay trabajadores registrados")
    else:
        for i in range(len(lista_todos_trabajadores)):
            print(f"Estos son todos los trabajadores {i+1} {lista_todos_trabajadores[i]}")


def imprimir_planillas():
        
            opc  = ""
            opc == input("1.- Para imprimir por cargo \n2.- Imprimir todos")
            if opc == "1":
                search_cargo= input("Ingrese cargo: ").lower()
                for i in lista_todos_trabajadores:
                    if i[cargos] in lista_todos_trabajadores:
                        file = open("archivo.txt","w") 
                        file.write(f"{i}")
                        file.close()
                        print("Archivo creado")
                        

            elif opc == "2:":
                try:
                  with open("lista_trabajadores.csv","w",newline="") as file:
                    write = csv.wirter(file,delimiter=",")
                    write.writerows(lista_todos_trabajadores)
                    print("Archivo creado")
                   
                except Exception as error:
                  print("Error al escribir el archivo",error)
                  

def leer_archivo():
    lista = []
    try:
        with open("archivo.csv","w",newline="") as file:
            lector = csv.DictReader(file)
            for i in lector:
                lista.append(i[lista_todos_trabajadores])
                print("Archivo leido")
    except Exception as error:
        print("Error al leer el archivo",error)
                    
                         