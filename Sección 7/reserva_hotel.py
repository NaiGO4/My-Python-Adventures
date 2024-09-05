print('*** Sistema de reserva de hotel ***')

#variable del hotel

tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_vista_mar = 190.50

# Pedimos la informacion al usurio

nombre_cliente = input('Cual es tu nombre: ')
dias_estadias = int(input('Dias de estadia: '))
vista_al_mar_txt = input('Con vista al mar (si/no)?')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

#Calculo del costo total de la estadia

if vista_al_mar:
    costo_total =  dias_estadias * tarifa_diaria_vista_mar
else:
    costo_total = dias_estadias * tarifa_diaria_sin_vista_mar

#Mostramos los detalles de la reeserva

print('\n-------------------------Detaller de la Reservacion-------------------------')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de estadia: {dias_estadias}')
print(f'Costo total: ${costo_total:.2f}')
print(f'Habitacion con al mar: {'Si'if vista_al_mar else 'No'}')