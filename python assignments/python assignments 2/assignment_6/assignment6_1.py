import threading

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def Prime(no):
    for i in no:
        if is_prime(i):
            print("Prime number:", i)

def NonPrime(no):
    for i in no:
        if not is_prime(i):
            print("Non-prime number:", i)

if __name__ == "__main__":

    numbers = [2, 4, 3, 6, 8, 9]

    t1 = threading.Thread(target=Prime, args=(numbers,))
    t2 = threading.Thread(target=NonPrime, args=(numbers,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
