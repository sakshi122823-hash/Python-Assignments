# addition of all factorial of number 

def add_fact(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0:
            fact = fact + i 
    print(fact)
        
        
    



number = int(input("enter number :"))

if __name__=="__main__":
    add_fact(number)

