import sqlite3

# Creando y/o abriendo la conexion con la base de dato
conexion = sqlite3.connect("base.db")
# Creando una tabla
sqlQueryCreateTb = """ CREATE TABLE persona
  (
    id        int primary key not null,
    nombre    text not null,
    pais      char(50)
  );"""

cursor = conexion.cursor()
cursor.execute( sqlQueryCreateTb )
conexion.commit()
conexion.close()