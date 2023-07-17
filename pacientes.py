import os
import json
import core
diccPacientes = {}

def LoadInfoPacientes():
    global diccPacientes
    if(core.checkFile('pacientes.json')):
        diccPacientes = core.LoadInfo('pacientes.json')
    else:
        diccPacientes = core.crearInfo('pacientes.json',diccPacientes)


def MainMenu():
    diccPacientes = core.LoadInfo('pacientes.json')
    isAddMainMenu = True
    isAddtipo=True
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^19}{}{:^18}|".format(' ','GESTIÓN DE PACIENTES',' '))
    print('+','-'*55,'+')
    print("1. Agregar paciente")
    print("2. Buscar Paciente")
    print("3. Mostrar informacion de un paciente")
    print("4. Salir")
    opcion = int(input("Ingresa una opcion: "))
    if(opcion==1):
        diccPacientes=core.LoadInfo('pacientes.json')
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^18}{}{:^18}|".format(' ','AGREGAR PACIENTE',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del paciente:")
        contador = len(diccPacientes)
        if contador !=0:
            for i,item in enumerate(diccPacientes):
                if id == item:
                    print("El paciente ya esta registrado")
                    os.system("pause")
                    MainMenu()
        nombre=input("Ingresa el nombre del paciente:").upper()
        while(isAddtipo):
            print("1.Perro")
            print("2.Gato")
            print("3.Reptil")
            print("4.Ave")
            opcionTipo= int(input("Ingresa el tipo de animal:"))
            if(opcionTipo==1):
                tipo="PERRO"
                break
            if(opcionTipo==2):
                tipo="GATO"
                break
            if(opcionTipo==3):
                tipo="REPTIL"
                break
            if(opcionTipo==4):
                tipo="AVE"
                break
            else:
                print("Opcion no valida")
        raza = input(f"Ingresa la raza de {tipo}:").upper()
        edad = int(input("Ingresa la edad del paciente:"))
        nombrePropietario = input("Ingresa el nombre del propietario:").upper()
        paciente={
        'id':id,
        'nombre':nombre,
        'tipo':tipo,
        'raza':raza,
        'edad':edad,
        'nombrePropietario':nombrePropietario
        }
        diccPacientes.update({f'{id}':paciente})
        core.crearInfo('pacientes.json',diccPacientes)
        print(diccPacientes)
        os.system('pause')
        MainMenu()
    elif(opcion==2):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^18}{}{:^19}|".format(' ','BUSCAR PACIENTE',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del paciente:")
        for i,item in enumerate(diccPacientes):
            if id == item:
                print(f'Id:{diccPacientes[id].get("id")}')
                print(f'Nombre:{diccPacientes[id].get("nombre")}')
                os.system('pause')
                MainMenu()
    elif(opcion==3):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^15}{}{:^14}|".format(' ','INFORMACIÓN DE PACIENTE',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del paciente:")
        for i,item in enumerate(diccPacientes):
            if id == item:
                print(f'Id:{diccPacientes[id].get("id")}')
                print(f'Nombre:{diccPacientes[id].get("nombre")}')
                print(f'Tipo:{diccPacientes[id].get("tipo")} y raza {diccPacientes[id].get("raza")}')
                print(f'Edad:{diccPacientes[id].get("edad")}')
                print(f'Propietario:{diccPacientes[id].get("nombrePropietario")}')
                os.system('pause')
    elif(opcion==4):
        isAddMainMenu=False
    elif(isAddMainMenu(opcion)):
        MainMenu()
