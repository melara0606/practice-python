class Person(object):
  nombre = ''
  apellidos = ''
  edad = 0

  def __init__(self, nombre, apellidos, edad):
    super(Person, self).__init__()
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad

  def mostrar_nombre(self):
    print(self.nombre)