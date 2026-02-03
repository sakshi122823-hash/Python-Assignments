from functools import reduce


def chk_even():
    n = int(input("enter the number of elements : "))
    numbers = []
    
    for i in range(n):
        
        num = int(input("enter the elements : "))
        numbers.append(num)


    even_nums = list(filter(lambda x : x%2==0 ,numbers))
    print("list after filter",  even_nums)


    sqaure = list(map(lambda x : x*x , even_nums))
    print("list after map",sqaure)
    

    add = reduce(lambda x , y : x + y , sqaure )
    print("list after reduce",add)

if __name__=="__main__":
    chk_even()