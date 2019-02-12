import socket

s = socket.socket()

HOSTNAME  = socket.gethostname()
PORT      = 8766

s.connect((HOSTNAME, PORT))
print(s.recv(1024))
s.close()