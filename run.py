class Propiedade(object):
  
  def __init__(self):
    self._x = 10
  
  setado = property(lambda self: self._x + 1)
  
  @setado.setter
  def setado(self, x):
    self._x = x
    
obj = Propiedade()

obj.setado = 5

print(obj.setado)
