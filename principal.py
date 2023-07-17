import os
import pacientes
import veterinarios
import citasmedicas

if __name__ == '__main__':
    os.system('cls')
    isAddPrincipal =True
    while isAddPrincipal:
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^10}{}{:^10}|".format(' ','ADMINISTRACIÓN DEL CENTRO VETERINARIO',' '))
        print('+','-'*55,'+')
        print("1. Gestión de pacientes.")
        print("2. Gestión de veterinarios.")
        print("3. Gestión de citas médicas.")
        print("4. Salir")
        opcion = int(input("Ingresa la opción: "))
        if opcion == 1:
            pacientes.LoadInfoPacientes()
            pacientes.MainMenu()
        elif opcion == 2:
            veterinarios.LoadInfoVeterinarios()
            veterinarios.MainMenu()
        elif opcion == 3:
            citasmedicas.LoadInfoCitas()
            citasmedicas.MainMenu()
        elif opcion == 4:
            isAddPrincipal=False
        else:
            print("Opción incorrecta")  
            os.system("pause")

