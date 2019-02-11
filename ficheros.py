# para poder escribir un archivo
# archivo = open("nuevo.txt", "w")
# archivo.write("Aprendiendo a escribir en archivo con python")

# archivo.close()

# para poder leer en un archivo

# archivo = open("nuevo.txt", 'r')
# lectura = archivo.read()
# print(lectura)
# archivo.close()

archivo = open("nuevo.txt", 'r+')
while True:
  print(archivo.tell())
  cadena = archivo.readline()
  if cadena:
    print(cadena[:-1])
  else:
    break
# archivo.seek(45, 0)
# archivo.write("Todo esta excelente")
# archivo.seek(78, 0)
# archivo.write("\nEstamos Aprendiendo python")

# archivo.seek(13, 0)
# cadena = archivo.read()
# archivo.seek(7, 0)
# archivo.write("Edwin Melara Landaverde\n"+ cadena)
# archivo.close()