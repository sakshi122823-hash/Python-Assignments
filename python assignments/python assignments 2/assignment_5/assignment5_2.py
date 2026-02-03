import threading

def EvenFactor(n):
    even = 0
    for i in range(1,n+1):
        if n % i ==0 and i % 2 == 0:
            print(i , end=" ")
            even = even + i
        
    print("sum of even factors : ",even)

def OddFactor(n):
    odd = 0
    for i in range(1,n+1):
        if n % i ==0 and i % 2 != 0:
            print(i,end=" ")
            odd = odd + i
    print("sum of odd factors is : ",odd)




def exit():
    print("exit from main ")


def main():
    
    num = int(input("enter the number : "))
    
    
    t1 = threading.Thread(target=EvenFactor,args=(num,))
    t2 = threading.Thread(target=OddFactor,args=(num,))
    t3 = threading.Thread(target=exit)


    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()



if __name__=="__main__":
    main()








