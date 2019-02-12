# ejemplo de funcion
def mi_funcion(par1, par2, par3):
  print("Valor de suma por def %s" % (par1 + par2 + par3))

# mi_funcion(par1=9, par3=19, par2=14)
# mi_funcion(par3=10, par1=5, par2=5)


def main(*args):
  suma  = 0
  for item in args:
    suma += item

  print("suma del valor por *args %s" % suma)

# main(4,5,6,8,7,9,8,9,7,8)
# main(7,6)

def promedio(nombre, seccion = 'A', *args):
  if args:
    promedio = round(sum(args) / 3)
  else:
    promedio = 'INHABILITADO'

  print('================')
  print('Alumno: ', nombre)
  print('Seccion: ', seccion)
  print('Promedio: ', promedio)
  print('================\n')

# promedio('Juan', 'C', 8,5,6)
# promedio('Edwin', 'B')
# promedio('Claudia','C', 8,9,8)

def mostrar_llaves(**kargs):
  for llave in kargs.items():
    print(llave)

# mostrar_llaves(a='Hola', b='Devcode.la')