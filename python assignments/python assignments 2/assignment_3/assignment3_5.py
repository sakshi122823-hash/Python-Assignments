import MarvellousNum

def ListPrime(n):
    lst = []
    for i in range(n):
        num = int(input("Enter element: "))
        lst.append(num)

    total = 0
    for x in lst:
        if MarvellousNum.ChkPrime(x):
            total += x

    return total


n = int(input("Enter number of elements: "))
result = ListPrime(n)
print("Output:", result)
