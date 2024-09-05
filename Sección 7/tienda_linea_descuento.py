print('*** Sistema de tienda en linea con descuento ***')


#Condiciones
Monto_compra_desc = 1000

monto_compra = float(input('Cual fue el monto de tu compra?: '))
es_mienbro = input('Eres mienbro de  la tienda (si/no)?:')

descuento = 0
#Verificar cada caso, con los datos proporcionados
if monto_compra >= Monto_compra_desc and es_mienbro.strip().lower() == 'si':
    descuento = 0.1 #Descuento del 10%
elif es_mienbro.strip().lower()== 'si':
    descuento = 0.5 # Decuento del 5%
elif monto_compra >= Monto_compra_desc:
    descuento = 0.3 # Decuento del 3%
else:
    descuento = 0

# Hacemos los calculos respectivos para obtener el monto final

if descuento !=0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra: ${monto_compra:.2f}')
    print(f'Monto de la compra: ${monto_descuento:.2f}')
    print(f'Monto final de la compra con decuento: ${monto_final:.2f}')
else:
    print('\nNo obtubiste ningun tipo de descuento')
    print('Te invitamos a hacerte miento de la tienda')
    print(f'Monto final de la compra: {monto_compra:.2f}')


