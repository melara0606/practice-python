import sqlite3

conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()

consulta = cursor.execute('select * from persona')

for e in consulta:
  print("id: {}, nombres: {} y su pais de origen es: {}".format(e[0], e[1], e[2]))
conexion.close()