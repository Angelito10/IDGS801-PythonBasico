class OperasBas:
  #Propiedades
  n1 =0
  n2 =0
  res =0

  #constructor
  def __init__(self) -> None:
      pass

  #metodos
  def sumar(self):
   self.res = self.n1 + self.n2;

  def restar(self):
    self.res = self.n1 - self.n2;

 




def main():
  obj = OperasBas(3,2)
  obj.sumar();

if __name__ == '__main__':
  main()

