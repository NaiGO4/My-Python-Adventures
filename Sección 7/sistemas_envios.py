print('*** Sistema de Envios ***')

#Definimos las tarifas de envios por kilogramo

Tarifa_Nacional= 10
Tarifa_Internacional = 20

# Solicitamos los valores de distino y peso al usuario

destino = input('Ingresa el destino del paquete (nacional/internacional): ')
peso = float(input('Ingresa el peso del paquete (en kg):'))

#Calculo del envio del paquete

costo_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo_envio = peso * Tarifa_Nacional
elif destino == 'internacional':
    costo_envio = peso * Tarifa_Internacional
else:
    print('Destino no valido: Ingresa el valor de nacional o internacional')

if costo_envio is not None:
    print(f'El costo de envio del paquete es : ${costo_envio:.2f}')