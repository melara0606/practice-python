import threading
import time

global cantidad
cantidad = 100

semaforo = threading.Semaphore(1)

class MyThread(threading.Thread):
  def __init__(self, usuario, monto):
    threading.Thread.__init__(self)
    self.usuario = usuario
    self.monto = monto

  def run(self):
    global cantidad
    try:
      semaforo.acquire()
      
      cantidad = cantidad + {
        'Jean': lambda x: -x,
        'Carlos': lambda x: +x,
        'Julio': lambda x: -x
      }[self.usuario](self.monto)

      print("%s esta realizado operaciones y su valor es %s" % (self.usuario, cantidad))
      time.sleep(2)
      semaforo.release()
    except Exception as e:
      print(e)

if __name__ == '__main__':
  hilos = [MyThread('Jean', 20), MyThread('Carlos', 40), MyThread('Julio', 60)]

  for hilo in hilos:
    hilo.start()