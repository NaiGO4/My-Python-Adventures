print('*** Sistema de autenticion ***')

Usurio_valido = 'admin'
Password_valido = '123'

usuria = input('Ingresa tu usurio: ')
password = input('Ingresa tu password: ')

if usuria == Usurio_valido and password == Password_valido:
    print('Bienvenido al Sistema')
elif usuria == Usurio_valido:
    print('Password incorrecto, por favor corrigelo.')
elif password == Password_valido:
    print('Usurio incorrecto, por favor corrigelo.')
else:
    print('La contraseña o el usurio son incorrectos')