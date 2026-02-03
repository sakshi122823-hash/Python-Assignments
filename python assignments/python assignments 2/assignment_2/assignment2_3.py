# factorial of the number


def factorial(A):
    fact = 1
    for i in range (1,A+1):
        fact = fact * i
    print(fact)

number = int(input("enter number :"))
factorial(number)