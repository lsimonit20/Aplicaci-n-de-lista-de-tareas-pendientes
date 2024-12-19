import time
import os

#Aplicacion de lista de tareas pendientes.

var=False
var2=False
var3=False
var4=False
lista_tareas=[]

while var==False: #Ciclo para controlar todo el menu principal de la APP.

    var=False
    var2=False
    var3=False
    var4=False

    #Menu para ir trabajando sobre el sistema.
    os.system("cls")
    print(" --- MENU / LISTA DE TAREAS --- \n")
    print("(1) CREAR TAREA.\n")
    print("(2) ACTUALIZAR TAREA.\n")
    print("(3) ELIMINAR TAREA.\n")
    print("(4) VISUALIZAR TAREAS.\n")

    opcion=input("OPCION: ")

    if opcion>"4" or opcion<="0":

        print("\nError en la opción.\n")
        os.system("pause")

    elif opcion.isdigit()==False:

        print("\nError en la opción.\n")
        os.system("pause")

    elif opcion=="":

        print("\nError en la opción.\n")
        os.system("pause")

    #---------------------- INICIO DE LAS OPCIONES DEL MENÚ -------------------------------------------------

    else:   

        if opcion=="1": #OPCIÓN 1 (Crear)

            while var2==False:

                os.system("cls")
                print("--- CREAR TAREA ---\n")
                tarea=input("Digite una tarea a crear: ")

                if tarea=="":

                    print("\nError.\n")
                    os.system("pause")
                    var2=False

                else:

                    lista_tareas.append(tarea)
                    print("\nTarea creada con exito!!!\n")
                    os.system("pause")
                    var2=True
                    continue
                
                var=False


        elif opcion=="2": #OPCIÓN 2 (Actualizar)

            while var4==False:

                if len(lista_tareas)==0:

                    os.system("cls")
                    print("La lista de tareas se encuentra vacía!!!\n")
                    os.system("pause")
                    var4=True
                    var=False

                else:

                    os.system("cls")
                    print("--- ACTUALIZAR TAREA ---\n\n")

                    print("TAREAS:\n")

                    for i, elemento in enumerate(lista_tareas, start=1):

                        print(f"{i} {elemento}.\n")

                    actualizar=input("\nDigite el numero de la tarea que quiere actualizar: ")

                    if actualizar=="":

                        print("\nError.\n")
                        os.system("pause")
                        var4=False
                    
                    elif actualizar<str(len(lista_tareas)) or actualizar>str(len(lista_tareas)):

                        print("\nEsa tarea no se encuentra registrada.\n")
                        os.system("pause")
                        var4=False

                    else:

                        cambio_act=input("\nDigite la nueva tarea: ")

                        if cambio_act=="":

                            print("\nError.\n")
                            os.system("pause")
                            var4=False

                        else:

                            lista_tareas[int(actualizar)-1]=cambio_act
                            print("\nSe actualizo la tarea con éxito.")
                            os.system("pause")
                            var4=True
                            continue

                    var=False
            

        elif opcion=="3": #OPCIÓN 3 (Eliminar)

            if len(lista_tareas)==0:

                os.system("cls")
                print("La lista de tareas se encuentra vacía!!!\n")
                os.system("pause")
                var=False

            else: 

                while var3==False:

                    os.system("cls")
                    print("--- ELIMINAR TAREA ---\n") 

                    print("TAREAS:\n")

                    for i, elemento in enumerate(lista_tareas, start=1):

                        print(f"{i} {elemento}.\n")

                    print("\n")
                    eliminar=input("Digite el numero de la tarea a eliminar: ")

                    if eliminar=="":

                        print("Error.\n")
                        os.system("pause")
                        var3=False

                    elif eliminar<str(len(lista_tareas)) or eliminar>str(len(lista_tareas)):

                        print("\nEsa tarea no se encuentra.\n")
                        os.system("pause")
                        var3=False

                    else:

                        del lista_tareas[int(eliminar)-1]

                        print("\nLa tarea ha sido eliminada con exito.\n")

                        print("\n")
                        os.system("pause")
                        var3=True
                        continue

                    var=False
            
        elif opcion=="4": #OPCIÓN 4 (Visualizar)

            if len(lista_tareas)==0:

                print("\nLa lista de tareas se encuentra vacía!!!\n")
                os.system("pause")
                var=False

            else:

                os.system("cls")
                print("TAREAS DISPONIBLES: \n")

                for i, elemento in enumerate(lista_tareas,start=1):

                    print(f"{i} {elemento}.")
                    print("--------------------")

                os.system("pause")
                var=False
                    








