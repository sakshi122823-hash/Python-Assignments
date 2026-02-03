import threading



def MaxElement(no):
    max_num = max(no)
    print("Maximum number is:", max_num)




def MinElement(no):
    min_num = min(no)
    print("Minimum number is:", min_num)



if __name__ == "__main__":

    numbers = list(map(int, input("enter numbers: ").split()))

    t1 = threading.Thread(target=MaxElement, args=(numbers,))
    t2 = threading.Thread(target=MinElement, args=(numbers,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()