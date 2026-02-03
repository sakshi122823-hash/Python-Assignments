import threading





def small_thread(s):
    count = 0
    for i in s:
        if i.islower():
            count = count + 1
    print("Lowercase characters:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    
    


def capital_thread(s):
    count = 0
    for i in s:
        if i.isupper():
            count += 1
    print("Uppercase characters:", count)
    
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    


def digits_thread(s):
    count = 0
    for i in s:
        if i.isdigit():
            count += 1
    print("Digits:", count)
    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    
    

if __name__ == "__main__":
    inputstring = input("Enter a string: ")

    t1 = threading.Thread(target=small_thread, args=(inputstring,))
    t2 = threading.Thread(target=capital_thread, args=(inputstring,))
    t3 = threading.Thread(target=digits_thread, args=(inputstring,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
