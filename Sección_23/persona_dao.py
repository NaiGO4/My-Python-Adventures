from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create Read Update Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:  # Crear cursor a partir de la conexión
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []  # Lista para almacenar objetos Persona
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)  # Agregar el objeto Persona a la lista
                return personas
        
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona a insertar: {persona}')
                conexion.commit()  # Confirmar los cambios en la base de datos
                return cursor.rowcount

if __name__ == '__main__':
    # Insertar objeto:
    # persona1 = Persona(nombre='Pedro', apellido='Jara', email='jara@gmail.com')
    # persona_insertar = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {persona_insertar}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
