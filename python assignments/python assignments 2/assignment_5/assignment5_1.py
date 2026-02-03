import threading

def display_even():
    for i in range(1,21):
        if i % 2 == 0:
            print(i)


def display_odd():
    for i in range(1,20):
        if i % 2 != 0:
            print(i)






def main():
    t1 = threading.Thread(target=display_even)
    t2 = threading.Thread(target=display_odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()




if __name__=="__main__":
    main()








