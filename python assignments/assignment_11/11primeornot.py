def primenum(num):
    for i in range(2, num):
        if num % i == 0:
            print("it is not prime")
            return   # stop checking

    print("it is prime")


number = int(input("enter number: "))
primenum(number)

    

    