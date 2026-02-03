class Arithmatic:


    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0


    def Accept(self):
        self.Value1 = int(input("enter the first number :")) 
        self.Value2 = int(input("enter the second  number :")) 

    def Addition(self):
        print(" addition is : ",self.Value1 + self.Value2) 
    

    def substraction(self):
        print("substraction is : ",self.Value1 - self.Value2)  
    
    def multiplication(self):
        print("multiplication is : ",   self.Value1 * self.Value2)


    def division(self):
        print("division is : ",self.Value1 / self.Value2)  

obj1 = Arithmatic()

obj1.Accept()
obj1.Addition()
obj1.substraction()
obj1.multiplication()
obj1.division()


obj2 = Arithmatic()
obj2.Accept()
obj2.Addition()
obj2.substraction()
obj2.multiplication()
obj2.division()

         