print('*** Bienvenido a la casa de los espejos ***')

edad = int(input('Cual es tu edad: '))
tienes_miedo_ocuridad = input('Tienes miedo a la oscuridad(si/no):')

tienes_miedo_ocuridad = tienes_miedo_ocuridad.strip().lower() == 'si'

if not tienes_miedo_ocuridad and edad >= 10:
    print('Puedes entrar a la casa de los espejos')
else:
    print('Lo siento la Casa de los espejos puede darte miedo.')