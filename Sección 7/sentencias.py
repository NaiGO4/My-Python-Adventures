print(f'*** Sentencia if ***')

edad = int(input("Ingresa la edad: "))
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años.')
elif 13 <= edad < 18:
    print(f'Eres un adolecente. Tienes {edad} años')
else:
    print(f'Eres menor de edad. Tienes {edad} años')