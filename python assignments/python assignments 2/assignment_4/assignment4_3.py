from functools import reduce
def FMR():
    N = int(input("enter the number of elements :  "))
    number =[]

    for i in range(N):
        elements = int(input("enter the elements : "))
        number.append(elements)

    print( " list =  ",number)


    filtered = list(filter(lambda x : 70 <= x <= 90 , number ))
    print("the list after filter : ",filtered)

    mapped = list(map(lambda x : x + 10 , filtered))
    print("list after map : ", mapped)


    reduced = reduce(lambda x, y :x*y , mapped)
    print("list after reduce : ",reduced)




if __name__=="__main__":
    FMR()
    