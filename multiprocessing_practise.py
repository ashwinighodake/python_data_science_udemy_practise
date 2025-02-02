import multiprocessing
import os

print("-------------------------Demonstration of Multiprocessing--------------------------")

def fun(number):
    print("Parent process of fun:",os.getpid())
    print("Process id of fun:",os.getpid())
    for i in range(number):
        print(i)

def gun(number):
    print("Parent process of gun:",os.getpid())
    print("Process id of gun:",os.getpid())
    for i in range(number):
        print(i)

if __name__=="__main__":
    print("Total cores available:",multiprocessing.cpu_count())
    print("Parent process of main:",os.getpid())
    print("Process id main:",os.getpid())

    number=3
    result=None

    P1=multiprocessing.Process(target=fun,args=(number,))
    P2=multiprocessing.Process(target=gun,args=(number,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()