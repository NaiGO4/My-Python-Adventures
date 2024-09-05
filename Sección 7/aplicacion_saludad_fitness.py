print('*** Aplicacion Salud y Fitness ***')

#Constantes

Meta_pasos_diarios = 10000
Calorias_por_paso = 0.04 # Valor aproximado, son kilocarias

#Pedimos los datos del usurio

nombre_usuria = input('Cual es tu nombre: ')
pasos_diario = int(input('Cuantos pasos has caminado hoy?: '))

#Varificar si el usurio alcanzo la meta de pasos diarios

meta_alcanzada = pasos_diario >= Meta_pasos_diarios
meta_alcanzada_txt = 'si' if meta_alcanzada else 'no'

#Calculamos los calorias quemadas

calorias_quemas = pasos_diario * Calorias_por_paso

#Mostramos la informacion
print(f'\nUsurio: {nombre_usuria}')
print(f'Pasos dados hoy: {pasos_diario}')
print(f'Calorias quemadas: {calorias_quemas} kcal')
print(f'Meta de pasos diario alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {Meta_pasos_diarios} pasos')
