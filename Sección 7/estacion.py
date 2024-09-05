print('*** Estacion del año ***')

mes = int(input('Proporciona el valor de la estacion del (1/12): '))
estacion = None

#Revicion del mes porporcionado

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif  mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Varano'
elif mes == 9 or mes == 10 or mes == 12:
    estacion = 'Otoño'
else:
    estacion = 'Estacion desconocidad'

# Resultado

print(f'La estacion para el; mes {mes} es {estacion}')