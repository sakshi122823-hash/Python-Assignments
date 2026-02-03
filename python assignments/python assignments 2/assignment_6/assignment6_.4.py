import threading

sumresult = 0


productresult = 1


def Sum(Num):
    global sumresult
    sumresult = sum(Num)




def Product(Num):
    global productresult
    for i in Num:
        productresult *= i




if __name__ == "__main__":

    numbers = list(map(int, input("enter numbers: ").split()))

    t1 = threading.Thread(target=Sum, args=(numbers,))
    t2 = threading.Thread(target=Product, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements is  :  ", sumresult)
    print("Product of elements is   :  ", productresult)

