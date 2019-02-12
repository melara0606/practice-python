import socket
import sys

s = socket.socket()
print("Socket creado!")

HOSTNAME  = ''
PORT      = 8766

try:
  s.bind((HOSTNAME, PORT))
except socket.error as e:
  print('> Bind fallo [MESSAGE: {}]'.format(e))
  sys.exit()

s.listen(1)
print('> Escuchando SOCKET en puerto %s' % PORT)

while True:
  connection, address = s.accept()
  print('Connected with %s: %s' % (address[0], address[1]))

  connection.send('HOLA SERVIDOR'.encode())
  connection.close()