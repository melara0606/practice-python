from Persona.Person import Person

class Empleado(Person):
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