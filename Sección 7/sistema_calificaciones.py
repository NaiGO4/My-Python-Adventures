print('*** Sistema de calificaciones ***')

calificacion = float(input('Proporciona una calificacion entre 0 y 20'))
calificacion_letra = NotImplemented
#Revisamos si esta en los siguientes rangos

if 16 <= calificacion <= 20:
    calificacion_letra = 'A'
elif 13 <= calificacion < 15:
    calificacion_letra = 'B'
elif 11 <= calificacion < 12:
    calificacion_letra = 'C'
elif 6 <= calificacion < 10:
    calificacion_letra = 'D'
elif 0<= calificacion < 5:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Calaficacion incorecta'

#Resultado
print(f'Calificacion {calificacion} esequivalente a {calificacion_letra}')