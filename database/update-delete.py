import sqlite3

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()
# Actualizado los datos
cursor.execute('update persona set pais = "Venezuela" where id = 4 ')
# Eliminado los datos
cursor.execute('delete from persona where id = 1')
conexion.commit()
conexion.close()