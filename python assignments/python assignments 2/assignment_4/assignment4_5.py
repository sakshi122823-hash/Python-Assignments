from functools import reduce
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True




def FMR():
    N = int(input("enter the number of elements :  "))
    number =[]

    for i in range(N):
        elements = int(input("enter the elements : "))
        number.append(elements)

    print( " list =  ",number)


    filtered = list(filter(is_prime   , number ))
    print("the list after filter : ",filtered)

    mapped = list(map(lambda x : x * 2 , filtered))
    print("list after map : ", mapped)


    reduced = reduce(lambda  x , y: x if x > y else y, mapped)
    print("list after reduce : ",reduced)




if __name__=="__main__":
    FMR()