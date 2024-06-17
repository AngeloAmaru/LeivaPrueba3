import csv
list=[]
def confirm():      #Terminado
    confirm=False
    print(" ¿DESEA ELIMINAR EL PLAN ? ")
    print(" 1- SI")
    print(" 2- NO")
    op=int(input("Ingrese COMANDO:  "))
    while op>2 and op<1:
        print("INGRESE COMANDO VALIDO!!!")
        print("")
        print("")
        print(" ¿DESEA ELIMINAR EL PLAN ? ")
        print(" 1- SI")
        print(" 2- NO")
        op=int(input("Ingrese COMANDO:  "))
    if op==1:
        confirm=True
    elif op==2:
        confirm=False
        print("Volviendo al menu....")
    if confirm==True:
        list.remove(x)
def stats(): #Las estadísticas contemplan imprimir los siguientes datos : ///1.- Porcentaje de efectividad promedio ///2.- Valor del porcentaje de efectividad más alto
    peak=0
    total=0
    for x in list:              #NoTerminado
        porcenta=int((x[2]))
        total=total+porcenta
    lamount=porcenta.len(x[0])
    average=porcenta/lamount
    print("Promedio: ",average)
    print("Porcentaje más Alto ", peak)
def newcsv():               #No Terminado
    with open("plan.csv","w",newline="") as archivo:
        writecsv=archivo.write
        writecsv

def importcsv():            #No terminado
    list.clear
    with open("plan.csv","r",newline="") as archivo:
        csvread=archivo.reader
    print("ARCHIVO CSV CARGADO")
def planlist():         #Terminado
    for x in list:
        print("ID: ",x[0],"Nombre: ",x[1],"Porcentaje: ",x[2],"Categoria: ",x[3])
        
'''La categoría interna es un dato que se genera automáticamente y que varía dependiendo del número del
porcentaje de efectividad. Guíese por los siguientes valores : 0 y 25  Chiste. 26 y 50  anécdota. 51 y 75 
peligro. 76 y 99  atención. 100  esclavitud. Para generar estas categorías deberá crear una función QUE
RETORNE este valor.
d.- Para eliminar un plan de los registros, se debe solicitar el ID del plan. Recuerde solicitar una confirmación al
usuario antes de eliminar.
e.- Cuando se genera la bbdd (opción 4) se crea un archivo CSV.
Subdirección de Evaluación de Resultados de Aprendizaje - Subdirección de Diseño Instruccional 2- 2023'''
def addplan():          #Terminado
    chiste="Chiste"
    anecdota="Anecdota"
    peligro="Peligro"
    atencion="Atencion"
    esclavitud="Esclavitud"
    print("===== AGREGAR PLAN====")
    print("")
    id=int(input("INGRESE ID : "))
    nombre=input("INGRESE NOMBRE : ")
    porcentaje=int(input("INGRESE PORCENTAJE: "))
    while porcentaje>100 and porcentaje<0:  #Confirma si el valor del porcentaje es Valido
        print("!Número Invalido!")
        print(" INGRESE VALORES ENTRE 0 y 100!!!")
    if porcentaje>0 and porcentaje<26:          
        nlist=[id,nombre,porcentaje,chiste]
    elif porcentaje>25 and porcentaje<51:
        nlist=[id,nombre,porcentaje,anecdota]
    elif porcentaje>50 and porcentaje<76:
        nlist=[id,nombre,porcentaje,peligro]
    elif porcentaje>75 and porcentaje<100:
        nlist=[id,nombre,porcentaje,atencion]
    elif porcentaje==100:
        nlist=[id,nombre,porcentaje,esclavitud]
    list.append(nlist)
def menu():         #Terminado
    print("========================")
    print("         M E N U         ")
    print("")
    print("")
    print("")
    print("1.- Agregar plan")
    print("2.- Listar planes")
    print("3.- Eliminar plan por ID")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadísticas")
    print("0.- Salir.")
while True:
    menu()
    op=int(input("INGRESE COMANDO: "))
    if op==1:
        addplan()
    elif op==2:
        planlist()
    elif op==3:
        found=False
        print("======= Eliminar plan por ID =========")
        idsearch=int(input("INGRESE ID A ELIMINAR"))
        for x in list:
            id=int((x[0]))
            if idsearch==id:
                print("PLAN ENCONTRADO")
                found=True
                confirm()
                break
            elif found==False:
                print("Plan no encontrado :C")
    elif op==4:
        newcsv()
    elif op==5:
        importcsv()
    elif op==6:
        stats()
    elif op==0:
        print(" Adios.....")
        break