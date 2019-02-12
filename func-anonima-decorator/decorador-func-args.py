def debug(breakpoint = False):
  def _debug(f):
    def new_function(argumento):
      print("estamos aqui para poder ver los decoradores con argumento, args: " + str(argumento))
      if breakpoint:
        print("El parametro es verdadero")
      else:
        print("El parametro es falso")
      return f(argumento)
    return new_function
  return _debug


@debug(breakpoint=True)
def main(parametro):
  pass

main(5)