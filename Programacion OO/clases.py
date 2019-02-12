class Persona(object):
  nombre = ''
  apellidos = ''
  edad = 0

  def __init__(self, nombre, apellidos, edad):
    super(Persona, self).__init__()
    self.nombre = nombre
    self.apellidos = apellidos
    self.edad = edad

  def mostrar_nombre(self):
    print(self.nombre)


class Empleado(Persona):
  cargo = ''
  __genero = ''

  def __init__(self, _nombres, _apellidos, _edad, cargo, genero = 'M'):
    super().__init__(_nombres, _apellidos, _edad)
    self.cargo = cargo
    self.__genero = genero
  
  def mostrar_nombre(self):
    print("Nombre: %s, Apellidos: %s" % (self.nombre, self.apellidos))

  def view_cargo(self):
    print(self.cargo)
  
  def getGenero(self):
    print(self.__genero)

empleado = Empleado('Edwin', 'Melara', 28, 'Estudiante')
empleado.mostrar_nombre()
empleado.view_cargo()
empleado.getGenero()