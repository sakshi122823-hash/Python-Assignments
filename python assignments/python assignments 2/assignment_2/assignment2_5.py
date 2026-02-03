def is_prime(n):
    
    
    for i in range(2,n):
        n % i == 0
        print("it is not prime")
        return  

    print("it is prime")

        

  


number = int(input("enter number :"))

if __name__=="__main__":
    is_prime(number)