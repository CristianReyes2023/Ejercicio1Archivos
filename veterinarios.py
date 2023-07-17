import os
import json
import core
from datetime import datetime
diccVeterinarios = {}

def LoadInfoVeterinarios():
    global diccVeterinarios
    if(core.checkFile('veterinarios.json')):
        diccVeterinarios = core.LoadInfo('veterinarios.json')
    else:
        diccVeterinarios = core.crearInfo('veterinarios.json',diccVeterinarios)


def MainMenu():
    isAddMainMenu = True
    diccVeterinarios = core.LoadInfo('veterinarios.json')
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^17}{}{:^17}|".format(' ','GESTIÓN DE VETERINARIOS',' '))
    print('+','-'*55,'+')
    print("1. Agregar veterionarios")
    print("2. Buscar veterionarios")
    print("3. Mostrar informacion del veterinario")
    print("4. Salir")
    opcion = int(input("Ingresa una opcion: "))
    if(opcion==1):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^16}{}{:^17}|".format(' ','AGREGAR VETERINARIO',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del veterinario:")
        contador=len(diccVeterinarios)
        if contador !=0:
            for i,item in enumerate(diccVeterinarios):
                if id == item:
                    print("El cliente ya esta registrado")
                    MainMenu()
        nombre=input("Ingresa el nombre del veterinario:").upper()
        os.system('cls')
        print("Ingresa Especialidad")
        print("1.CIRUJANO")
        print("2.ONCOLOGIA")
        print("3.FISIOTERAPIA")
        opcion=int(input("Ingrese opción: "))
        if(opcion==1):
            tituloProfesional="CIRUJANO"
        elif(opcion==2):
            tituloProfesional="ONCOLOGIA"
        elif(opcion==3):
            tituloProfesional="FISIOTERAPIA"
        os.system('cls')
        print("Ingresa horario")
        print("1.00:00 a 08:00")
        print("2.08:00 a 16:00")
        print("3.16:00 a 24:00")
        opcion=int(input("Ingrese opción: "))
        if(opcion==1):
            horario="00:00 a 08:00"
        elif(opcion==2):
            horario="08:00 a 16:00"
        elif(opcion==3):
            horario="16:00 a 24:00"
        veterinario={
        'id':id,
        'nombre':nombre,
        'tituloProfesional':tituloProfesional,
        'horario':horario,
        }
        diccVeterinarios.update({f'{id}':veterinario})
        core.crearInfo('veterinarios.json',diccVeterinarios)
        print(diccVeterinarios)
        os.system('pause')
    elif(opcion==2):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^17}{}{:^17}|".format(' ','BUSCAR VETERINARIA',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del veterinario:")
        for i,item in enumerate(diccVeterinarios):
            if id == item:
                print(f'Id:{diccVeterinarios[id].get("id")}')
                print(f'Nombre:{diccVeterinarios[id].get("nombre")}')
                # print(f'titulo Profesional:{diccVeterinarios[id].get("tituloProfesional")}')
                os.system('pause')
    elif(opcion==3):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^12}{}{:^13}|".format(' ','INFORMACIÓN DEL VETERINARIO',' '))
        print('+','-'*50,'+')
        id=input("Ingresa el id del veterinario:")
        for i,item in enumerate(diccVeterinarios):
            if id == item:
                print(f'Id:{diccVeterinarios[id].get("id")}')
                print(f'Nombre:{diccVeterinarios[id].get("nombre")}')
                print(f'Veterinario con especialidad en:{diccVeterinarios[id].get("tituloProfesional")}')
                print(f'Horario:{diccVeterinarios[id].get("horario")}')
                os.system('pause')
    elif(opcion==4):
        isAddMainMenu=False
    elif(isAddMainMenu(opcion)):
        MainMenu()
