print('*** Sistema de Administracion de cuenta ***')

salir = False
while not salir:
    print(f'''Menu:
          1: Crear Cuenta.
          2: Borrar Cuenta.
          3: Salir.''')
    opcion = int(input('Escoje una opcion:'))
    if opcion == 1:
        print('Creando cuenta...\n')
    elif opcion == 2:
        print('Elimando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema')
        salir = True
    else:
        print('Opcion invalida, proporciona otra opcion. \n')