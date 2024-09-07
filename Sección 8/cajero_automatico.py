print('*** Cajero Automatico***')

saldo = 1000
salir = False

while not salir:
    print(f'''Opereaciones que puedes realizar.
          1. Consultar saldo
          2. Retirar
          3. Depocitar
          4. Salir
''')
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        if retiro <=saldo:
            saldo -= retiro # saldo = retiro - saldo
            print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 3:
        depocito = float(input('Ingresa el depocito:'))
        saldo += depocito #saldo: saldo + depocito
        print(f'Tu nuevo saldo es de: ${saldo:.2f}\n')
    elif opcion == 4:
        print(f'Saliendo del sistema del cajero. Gracias')
        salir = True
    else: 
        print('Operacion invalidad escoja una opcion.\n')
else:
    print('Termino de la aplicacion de Cajero Automatico. \n')
