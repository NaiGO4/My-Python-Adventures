# Uso y instalacion de Postgres

### Descarga de Postgres

La vercion de postres es la version de 16: [Postgres](https://www.postgresql.org/)

Informacion de base al momento de usar Postgres
- Puerto de la base de datos: "5432"
- Motor de base de datos Postgres
- usermane: admin y password: admin

### Consultas **SQL**

Selecion la informacion de todo la tabla
```
SELECT * FROM persona
```

Insertar datos en la tabla
```
INSERT INTO persona(nombre, apellido, email) VALUES('Richard','Sanches','sanches@gmail.com')
```

Actualizacion de datos de tablas
```
UPDATE persona SET nombre='Alberto', email='alberto@gmail.com' WHERE id_persona=3
```

Eliminacion de datos de tablas
```
DELETE FROM persona WHERE id_persona=2
```

# Instalacion de entorno vitual venv

Instalacion de venv

```
python -m venv venv
```

Activacion de venv en Windows

```
.\venv\Scripts\activate
```

# Conector de de Postgres y Python

Instalacion de psycopg2
```
pip install psycopg2
```
Para MySQL
```
pip install mysql connector
```