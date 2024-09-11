import psycopg2

conexion = psycopg2.connect(
    user='postgres', 
    password='admin', 
    host = '127.0.0.1', 
    port = '5432', 
    database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona= %s'
            id_persona = input('Ingresa el Id: ')
            cursor.execute(sentencia, (id_persona,))
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print(f'Ocurrio un erro: {e}')
finally:
    conexion.close()
