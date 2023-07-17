import os
import core
import random
from datetime import datetime
diccCitas = {}

def LoadInfoCitas():
    global diccCitas
    if(core.checkFile('citas.json')):
        diccCitas = core.LoadInfo('citas.json')
    else:
        diccCitas = core.crearInfo('citas.json',diccCitas)

def MainMenu():
    horarioMadrugada = ("00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00")
    horarioDia = ("08:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00")
    horarioNoche = ("17:00","18:00","19:00","20:00","21:00","22:00","23:00","24:00")
    isAddMainMenu = True
    isIdPaciente =True
    diccVeterinarios = core.LoadInfo('veterinarios.json')
    diccPacientes = core.LoadInfo('pacientes.json')
    diccCitas = core.LoadInfo('citas.json')
    os.system("cls")
    print('+','-'*55,'+')
    print("|{:^20}{}{:^21}|".format(' ','GESTIÓN DE CITAS',' '))
    print('+','-'*55,'+')
    print("1. Crear cita")
    print("2. Cancelar cita")
    print("3. Consultar cita por fecha")
    print("4. Consultar cita por veterinario")
    print("5. Salir")
    opcion = int(input("Ingresa una opcion: "))
    if(opcion==1):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^21}{}{:^21}|".format(' ','CREAR CITA',' '))
        print('+','-'*50,'+')
        print("NOTA: Para agendar citas se solicita agregar los medicos que cubriran los 3 turnos del día")
        idAleatorio = str(random.randint(1,10000)).zfill(5)
        citaNumero=str(len(diccCitas)+1)
        # if citaNumero == 0:
        #     fechaCita = input("Ingersar fecha en formato (dd-mm-yyyy): ") 
        #     hora=input("Ingresar hora fomato (24 H): ")
        # fechaCita = input("Ingersar fecha en formato (dd-mm-yyyy): ")
        while True:
            fechaCita = input("Ingersar fecha en formato (dd-mm-yyyy): ")
            try:
                fecha = datetime.strptime(fechaCita,"%d-%m-%Y").date()
                break
            except Exception:
                print("El formato o fecha incorrecta")
        fechaFinal=fecha.strftime("%d-%m-%Y")
        while True:
            horaCita = input("Ingersar hora en formato (24H HH:MM): ")
            try:
                hora = datetime.strptime(horaCita,"%H:%M").time()
                break
            except Exception:
                print("El formato o hora incorrecta")
        horaFinal=hora.strftime("%H:%M")
        # hora=input("Ingresar hora: (fomato 24 H 12:00): ")
        for i,item in enumerate(diccCitas):
            if (fechaFinal in diccCitas[item].get('fecha')) and (horaFinal in diccCitas[item].get('horaCita')):
                print("Fecha ingresada ya está ocupada, agregar nueva fecha")
                os.system('pause')
                MainMenu()
        if horaFinal in horarioMadrugada:
            horario = "00:00 a 08:00"
            for i,itemVet in enumerate(diccVeterinarios):
                    if horario in diccVeterinarios[itemVet].get('horario'):
                        idVeterinario = diccVeterinarios[itemVet].get('id')
                        nombreVeterinario = diccVeterinarios[itemVet].get('nombre')
                        break
        if horaFinal in horarioDia:
            horario = "08:00 a 16:00"
            for i,itemVet in enumerate(diccVeterinarios):
                    if horario in diccVeterinarios[itemVet].get('horario'):
                        idVeterinario = diccVeterinarios[itemVet].get('id')
                        nombreVeterinario = diccVeterinarios[itemVet].get('nombre')
                        break
        if horaFinal in horarioNoche:
            horario = "16:00 a 24:00"
            for i,itemVet in enumerate(diccVeterinarios):
                    if horario in diccVeterinarios[itemVet].get('horario'):
                        idVeterinario = diccVeterinarios[itemVet].get('id')
                        nombreVeterinario = diccVeterinarios[itemVet].get('nombre')
                        break
        # while idPaciente not in diccPacientes:
        #     print("No ingresaste un ID de paciente correcto.")
        #     idPaciente = input("Ingresar ID del paciente: ")
        for i,item in enumerate(diccPacientes):
            print(f"Paciente:{i} y su info {diccPacientes[item]}")
        os.system('pause') and os.system('sleep 10')
        idPaciente = input("Ingresar ID del paciente: ")
        encontrado = False
        for i,item in enumerate(diccPacientes):
            if idPaciente in diccPacientes[item].get('id'):
                    idPaciente=diccPacientes[idPaciente].get("id")
                    nombrePaciente=diccPacientes[idPaciente].get("nombre")
                    tipo=diccPacientes[idPaciente].get("tipo")
                    raza=diccPacientes[idPaciente].get("raza")
                    edad=diccPacientes[idPaciente].get("edad")
                    propietario=diccPacientes[idPaciente].get("nombrePropietario")
                    encontrado=True
                    break
        if not encontrado:
            print("Id no es valido")
            MainMenu()
        citas={
            'idCita':idAleatorio,
            'numeroCita':citaNumero,
            'fecha':fechaCita,
            'horaCita':horaFinal,
            'informacionVeterinario':{
                'idVeterinario':idVeterinario,
                'nombreVeterinario':nombreVeterinario
            },
            'informacionPaciente':{
                'idPaciente':idPaciente,
                'nombrePaciente':nombrePaciente,
                'tipo':tipo,
                'raza':raza,
                'edad':edad,
                'propietario':propietario
            }
        }
        diccCitas.update({f'{citaNumero}':citas})
        core.crearInfo('citas.json',diccCitas)
        MainMenu()
    elif(opcion==2):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^20}{}{:^19}|".format(' ','CANCELAR CITA',' '))
        print('+','-'*50,'+')
        idCita=input("Ingresa el id de la cita: ")
        busqueda=False
        for i,item in enumerate(diccCitas):
            if idCita == diccCitas[item].get('idCita'):
                diccCitas.pop(item)
                core.EditarData('citas.json',diccCitas)
                os.system('pause')
                busqueda=True
                break
        if not busqueda:
            print("No se encontro cita con ese Id.Ingresa otro Id")
    elif(opcion==3):
        os.system("cls")
        print('+','-'*50,'+')
        print("|{:^14}{}{:^14}|".format(' ','CONSULTAR CITAS POR FECHA',' '))
        print('+','-'*50,'+')
        while True:
            fechaCita = input("Ingersar fecha en formato (dd-mm-yyyy): ")
            try:
                fecha = datetime.strptime(fechaCita,"%d-%m-%Y").date()
                break
            except Exception:
                print("El formato o fecha incorrecta")
        fechaFinal=fecha.strftime("%d-%m-%Y")
        while True:
            horaCita = input("Ingersar hora en formato (24H HH:MM): ")
            try:
                hora = datetime.strptime(horaCita,"%H:%M").time()
                break
            except Exception:
                print("El formato o hora incorrecta")
        horaFinal=hora.strftime("%H:%M")
        for i,item in enumerate(diccCitas):
            if (fechaFinal in diccCitas[item].get('fecha')) and (horaFinal in diccCitas[item].get('horaCita')):
                print(diccCitas[item])
                os.system('pause')
                MainMenu()
    elif(opcion==4):
        os.system("cls")
        busqueda = []
        print('+','-'*50,'+')
        print("|{:^11}{}{:^13}|".format(' ','CONSULTAR CITAS VETERINARIO',' '))
        print('+','-'*50,'+')
        for i,item in enumerate(diccVeterinarios):
            print(f"Veterinario:{i+1}, información: {diccVeterinarios[item]}")
        idVeterinario=input("Ingresar el id del veterinario: ")
        for i,item in enumerate(diccCitas):
            if (idVeterinario in diccCitas[item]['informacionVeterinario'].get('idVeterinario')):
                busqueda.append(diccCitas[item])
        for i,veterinario in enumerate(busqueda):
            print(f"Cita # :{i+1}. Información: {veterinario}")
        os.system('pause')
        MainMenu()
    elif(opcion==5):
        isAddMainMenu=False
    elif(isAddMainMenu(opcion)):
        MainMenu()
