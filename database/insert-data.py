import sqlite3

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()
## Vamos a insertar los datos

cursor.execute('insert into persona(id, nombre, pais) values(1, "Pedro Linares", "Chile");')
cursor.execute('insert into persona(id, nombre, pais) values(2, "Carlos Corcuera", "Argentina");')
cursor.execute('insert into persona(id, nombre, pais) values(3, "Julio Mendoza", "Mexico");')
cursor.execute('insert into persona(id, nombre, pais) values(4, "Rosa Loyala", "Peru");')
cursor.execute('insert into persona(id, nombre, pais) values(5, "Angela Paz", "Peru");')
conexion.commit()
conexion.close()