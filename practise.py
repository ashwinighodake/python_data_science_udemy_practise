print("----- Demonstration of List -----")

print("1.List are changeable,heterogenous,allow duplicate,inedexed")
batches=["PPA","LB","ANGULAR","Python"]

print(batches)
print(batches[0])
print(batches[1])
print(batches[-1])
print(batches[1:])
print(batches[:3])

# We can store heterogenous data
data1=[11,"Marvellous",3.14]
print(data1)

data2=[21,"Infosystems",6.10]
print(data2)

combined=[data1,data2]
print(combined)


# There are multiple methods that we can manipulate list.

batches.append("Mean")
print(batches)

batches.insert(2,"LSP")
print(batches)
batches.remove("LSP")

batches.pop()
print(batches)

batches.pop(2)
print(batches)

del batches[1:]
print(batches)

batches.extend(["LB","Python","Angular","Mean"])
print(batches)

batches.sort()
print(batches)

print("-----------------Demostration of tuples-------------------------")
print("1.tuples are immutable,heterogenous,allow duplicate,inedexed")

tup=(11,"Marvellous",3.14,5,"Infosystems")

print(tup)
print(tup[0])
print(tup[1])
print(tup[1:])
print(tup[:2])
print(tup[1:2])

print(len(tup))
print("Marvellous" in tup)

del tup

print("-----------------------------Demonstration of Set---------------------------")
print("1.Heterogenous , Unorderd,unindexed,Immutable,duplicates are not allowed")

set={11,"PPA",21,3.14,"Python"}
print(set)
print(len(set))
set.remove(21)
print(set)

print(set.discard(11))
print(set)
set.add("Angular")
print(set)


print("Demostraion of for loop")
x=[10,20,"ABC","XYZ",30.1]

for i in x:
    print(i)

for i in range(0,9):
    print(i)

print("Demosttration of while loop")
i=1

while(i<5):
    print(i)
    i=i+1

print("Demonstration of break & continue")

print("Demonstration of break")
for i in range(0,9):
    if(i==3):
        break
    print(i)

print("Demonstration of continue")
for i in range(0,9):
    if(i==3):
        continue
    print(i)


print("Demonstration of arrays")
import array as arr

a=arr.array('i',[2,4,6,8])

print("First element:",a[0])
print("Second Element:",a[1])
print("Second last element is:",a[-1])

a=arr.array('f',[2.4,4.5,6.5,8.8])

print("First element:",a[0])
print("Second Element:",a[1])
print("Second last element is:",a[-1])
print(a.typecode)

a.reverse()
for i in range(len(a)):
    print(a[i])

b=arr.array('i',[1,2,1,2])
for i in range(len(b)):
    print(b[i])

i=0
while(i<len(b)):
    print(b[i])
    i+=1

print("Demonstration of lambda:Anonymous function")

#Define regular function
def add(no1,no2):
    return no1+no2

value1=10
value2=5

ret=add(value1,value2)

print("Addition is {} with regular function".format(ret))

#Defining lambda funcction i.e anonymous function 
fp=lambda no1,no2:no1+no2

ret=fp(value1,value2)
print("Addition is {} with lambda function".format(ret))

#Filter,Map,Reduce
# list(function_to_apply,list_of_inputs)

arr=[8,9,5,16,2,4,21,30,11]
evenarr=list(filter(lambda no:(no%2==0),arr))
print("array values with filter:",evenarr)


modarr=list(map(lambda no:no+2,evenarr))
print("array value with map",modarr)

import functools
sum=functools.reduce(lambda a,b:a+b,modarr)
print("after applying reduce:",sum)

print("---------------------Demonstration of class-----------------------")

class Demo:
    def __init__(self,value1,value2):
        print("Inside init method")
        self.i=value1
        self.j=value2

    def fun(self):
        print("Inside fun")
        print(self.i,self.j)
    
    def Add(self):
        print(self.i+self.j)

#Creating object of demo class
obj1=Demo(10,20)
obj1.fun()

obj2=Demo(50,60)
obj2.fun()

obj1.Add()
obj2.Add()

print("-----------------------Demonstration of characteristics of class------------------")

class Demo1:
    x=10
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2

obj1=Demo1(10,20)
obj2=Demo1(11,21)

print(obj1.i)
print(obj1.j)

print(obj2.i)
print(obj2.j)

print(Demo1.x)

print("---------------------Demonstration of behaviour of class----------------------------")

class Demo2:
    def __init__(self):
        self.i=0
        self.j=0
    
    def fun(self):
        print("Inside instance")

    @classmethod
    def gun(cls):
        print("Inside class method")

    @staticmethod
    def sun():
        print("Inside static")

obj1=Demo2()
obj1.fun()
Demo2.gun()
Demo2.sun()

print("--------------------------Demostration of types of function arguments------------------")

print("---------------------------Position arguments---------------------------")

def Batches1(name,fees):
    print("Batch name is:",name)
    print("Fees are:",fees)

Batches1('Python',500)
Batches1(5000,'Angular')

print("------------------Demostration of keyword arguments-----------------------")

def Batches2(name,fees):
    print("Batch name is:",name)
    print("Fees are:",fees)

Batches2(fees=9000,name="PPA")
Batches2(name="LB",fees=7500)


print("Demostration of Default arguments")

def Batches3(name,fees=5000):
    print("Batch name is:",name)
    print("fees are:",fees)

Batches3('Angular',7500)
Batches3('Angular')
Batches3(fees=9000,name='PPA')
Batches3(name='LB')


print("--------------------Demonstrations of variable number of arguments----------------------")
def Add(*no):
    ans=0
    for i in no:
        ans=ans+i
    return ans

ret=Add(10,20,30)
print("Addition is:",ret)

ret=Add(10,20,30,40,50,60)
print("Addition is:",ret)

ret=Add(10,20)
print("Addition is",ret)

def studentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

studentInfo(age=28,address="Sinhgad Road",mobile=7588945488)

print("-------------------------------Demonstration of decorators-----------------------")


def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result) 

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  

print("--------------------------Demonstration of duck typing-----------------")
class Sparrow:
    def fly(self):
        print("Sparrow flying")

class Airoplane:
    def fly(self):
        print("Air Flying")

class Whale:
    def swim(self):
        print("Whale Swimming")

def fun(entity):
    entity.fly()

sparrow=Sparrow()
airoplane=Airoplane()
whale=Whale()

fun(sparrow)
fun(airoplane)


print("--------------------------Demonstration of scope of recursion----------------------")
import sys

print("Maximum number of recursive call are{} in python".format(sys.getrecursionlimit()))
#changing recursion limit
sys.setrecursionlimit(1500)
print("Maximum number of recursive call are{} in python".format(sys.getrecursionlimit()))


#recursive function which goes into infinite recursive calls

def fun():
    print("Inside fun")
    fun()

i=1
def gun():
    global i
    if(i<=10):
        print(i)
        i+=1
        gun()

gun()

def fact(no):
    if(no==0):
        return 1
    
    return no*fact(no-1)

value=5
ret=fact(value)
print("Factorial of {} is {}".format(value,ret))

print("----------------------------------Demonstration of exception handling--------------------")
no1=int(input("Enter the first number:"))
no2=int(input("Enter the second number:"))

try:
    ans=no1/no2
    print("Division is:",ans)
except ZeroDivisionError:
    print("Unable to devide by zero")
finally:
    print("Inside finally block to release all resources")

print("End of exception hanling application")


import threading
amount = 0
def Counter(fun,lock):
    fun(lock)

def Credit(lock):
    value=int(input("Enter the amount to credit"))
    lock.acquire()
    global amount
    amount=amount+value
    print("Balance is:",amount)
    lock.release()

def Debit(lock):
    value=int(input("Enter amount to withdraw"))
    lock.acquire()
    global amount
    if amount<value:
        print("Unable to withdraw")
    else:
        amount=amount+value
        print("Amount withdraw",value)
        print("Balance is:",amount)
    lock.release()

def main():
    print("------------------------Demonstration of threading-----------------------------")
    lock=threading.Lock()
    t1=threading.Thread(target=Counter,args=(Credit,lock))
    t2=threading.Thread(target=Counter,args=(Debit,lock))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()


print("----------------------------Demonstration of python command line arguments----------------------")

import sys 
print("Application name:"+sys.argv[0])
try:
   x=int(sys.argv[1])
   y=int(sys.argv[2])

   z=x+y

except:
    print("Error occured")
    
print(z)

