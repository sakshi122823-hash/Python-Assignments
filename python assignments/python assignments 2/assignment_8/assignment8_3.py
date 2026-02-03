class Numbers:
    def __init__(self):
        self.Value = int(input("Enter the number: "))

    def chkprime(self):
        for i in range(2, self.Value):
            if self.Value % i == 0:
                print("it is not a prime number  ")
                return
        print("it is a prime number ")

    def Factors(self):
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        print(total) 

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            print("it is perfect num")
        else:
            
            print("its not perfect num")



        


obj1= Numbers()
obj1.chkprime()
obj1.Factors()
obj1.SumFactors()
obj1.ChkPerfect()

obj2= Numbers()
obj2.chkprime()
obj2.Factors()
obj2.SumFactors()
obj2.ChkPerfect()
        