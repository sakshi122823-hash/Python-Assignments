import threading


def printnum():
    for i in range(1,51):
        print(i)

def reversenum():
    for i in range(51,0,-1):
        print(i)





if __name__ == "__main__":
    t1 = threading.Thread(target=printnum, args=() )
    t2 = threading.Thread(target=reversenum,args=() )

    
    t1.start()
    t1.join()          

 
    t2.start()
    t2.join()
