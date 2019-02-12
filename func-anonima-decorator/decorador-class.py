import sqlite3

class Verificar(object):
  def __init__(self, f):
    self.f = f
  
  def exists(self, id):
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM persona WHERE id = ' + str(id))
    usuario = cursor.fetchone()
    conexion.close()

    return usuario
  
  def __call__(self, usuario_id):
    try:
      u = self.exists(usuario_id)
    except Exception as e:
      print(e)
    else:
      return self.f(u)

@Verificar
def search_usuario(persona):
  print(persona)

search_usuario(2)
