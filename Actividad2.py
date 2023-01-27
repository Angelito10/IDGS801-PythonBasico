class Operaciones: 

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2


    def sumar(self):
       print(self.n1 + self.n2)


    def restar(self):
     print(self.n1 - self.n2)


    def multiplicar(self):
     print(self.n1 * self.n2)
     

    def dividir(self):
        print(self.n1 /self.n2)



res = 0

while res != 5:

    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. salir")

    res = int (input("¿Que opcion desea?"))


    if res == 1:
    
        num1Suma = int(input("Inserta el numero 1: "))
        num2Suma = int(input("Inserta el numero 2: "))
        opSuma = Operaciones(num1Suma, num2Suma)

        print("El resultado de la suma es:")
        opSuma.sumar();
        

    
    if res == 2:
        num1Resta= int(input("Inserta el numero 1: "))
        num2Resta = int(input("Inserta el numero 2: "))
        opRestar = Operaciones(num1Resta, num2Resta)
        print("El resultado de la resta es:")
        opRestar.restar()
    
        
    if res == 3:
        num1Multi= int(input("Inserta el numero 1: "))
        num2Multi = int(input("Inserta el numero 2: "))
        opMul= Operaciones(num1Multi, num1Multi)
        print("El resultado de la multiplicacion es: ")
        opMul.multiplicar()
        

    if res == 4: 
        num1Division= int(input("Inserta el numero 1: "))
        num2Division = int(input("Inserta el numero 2: "))
        opDiv = Operaciones(num1Division, num1Division)
        print("El resultado de la division es: ")
        opDiv.dividir()


print("Adios :)")


        


 









