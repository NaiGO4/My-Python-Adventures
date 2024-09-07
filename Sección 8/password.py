print('*** Creacion y validacion de Contraseña ***')

password = input('Ingresa un password(debe tener al menos 6 caracteres):')

while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener almenos 6 caracteres como minimo.')
    password = input('Ingresa nuevamente la contraseña:')
else:
    print('El valor del Contraseña es valida.')