class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter the name of account holder: ")
        self.Amount = int(input("Enter the name of account holder: "))
        

    def Display(self):
        print("name of account holder : ", self.Name)
        print(" initial amount of account : ", self.Amount)   

    def Deposit(self):
        self.deposit_amount = int(input("enter the deposit amount : "))
        self.Amount += self.deposit_amount
        print("total balace after the deposit : " ,self.Amount)
    
    def Withdraw(self):
        self.withdraw_amount = int(input("enter the withdraw amount : "))
        if self.Amount >= self.withdraw_amount:
            self.Amount -= self.deposit_amount
            print("total balace after the withdraw : ",self.Amount )
        else:
            print("oops !!!! , no sufficent balance ")

    def CalculateIntrest(self):
        print("The intrest is :  ",self.Amount*BankAccount.ROI/ 100 )


obj1= BankAccount()
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateIntrest()

obj2= BankAccount()
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
obj2.CalculateIntrest()
        
    