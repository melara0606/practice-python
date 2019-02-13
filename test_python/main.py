import unittest

class Calculadora(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def suma(self):
    return self.a + self.b
  
  def restar(self):
    return self.a - self.b
  
  def multiplicar(self):
    return self.a * self.b
  
  def dividir(self):
    return self.a/self.b


calculadora = Calculadora(9,5)

class CalculadoraTestCase(unittest.TestCase):
  def test_01(self):
    self.assertEqual(calculadora.suma(), 14)
  
  def test_02(self):
    self.assertEqual(calculadora.restar(), 4)

  def test_03(self):
    self.assertEqual(calculadora.multiplicar(), 45)

  def test_04(self):
    self.assertEqual(calculadora.dividir(), 1.8)

if __name__ == '__main__':
  unittest.main()