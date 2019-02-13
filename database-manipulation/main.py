import sqlite3

conexion = sqlite3.connect('db.sqlite3')

# SQLText = "CREATE TABLE Amigos(id INTEGER, nombre TEXT, edad INTEGER);"

# conexion.execute(SQLText)
# ListDataFriends = [(1, 'Ana', 23), (2, 'Paul', 21), (3, 'Rosy', 18), (4, 'David', 19), (5, 'Martin', 16)]
# cursor = conexion.cursor()

# cursor.executemany("INSERT INTO Amigos(id, nombre, edad) VALUES(?, ?, ?)", ListDataFriends )
# conexion.commit()

# cursor = conexion.execute('SELECT * FROM Amigos')
# amigos = cursor.fetchall()

# for amigo in amigos:
#     print(amigo)

# cursor = conexion.execute('SELECT * FROM Amigos WHERE id=:id', { 'id' : 2 })
# print(cursor.fetchone())

# SQLUpdate = "UPDATE Amigos SET nombre=:nombre, edad=:edad WHERE id=:id"
# parametro = { 'nombre': 'Roberto', 'edad': 14, 'id': 2 }

# conexion.cursor().execute(SQLUpdate, parametro)
# print(conexion.execute('SELECT * FROM Amigos WHERE id=:id', { 'id': 2 }).fetchone())

conexion.close()