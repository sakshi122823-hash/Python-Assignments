def minnum_list():
    n = int(input("enter the number of elements : "))
    list = []
    
    for i in range(n):
        
        num = int(input("enter the elements : "))
        list.append(num)
    

    number = int(input("enter the number which is to be searched  : "))
    count = 0
    for j in list:
        if j == number:
            count = count + 1
        
    print( "frequency of the number is : "    ,count)   




if __name__=="__main__":
    minnum_list()

