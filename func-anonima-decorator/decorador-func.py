import sqlite3

def decorador_usuario_existe(nombre_funcion):
  def verificar(persona_id):
    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute('select * from persona where id = ' + str(persona_id))
    usuario = cursor.fetchone()
    conexion.close()
    return usuario

  def funcion_decorada(argumento):
    try:
      persona = verificar(argumento)
    except Exception as e:
      print(e)
    else:
      nombre_funcion(persona)
  return funcion_decorada

@decorador_usuario_existe
def mi_reporte_de_sesiones(persona):
  print("Id: {}, nombre: {} y pais {}".format(persona[0], persona[1], persona[2]))

mi_reporte_de_sesiones(3)
