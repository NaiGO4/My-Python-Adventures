import psycopg2

#Conexion a la base de datos
conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan', 'Perez', 'perez@gmail.com',1)
            cursor.execute(sentencia, valores)
            registro_actulizados = cursor.rowcount
            print(f'Registro Insertados: {registro_actulizados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()        
        