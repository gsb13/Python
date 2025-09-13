# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:08:49 2021

@author: Pankaj Dhas
"""

#python Function
#wheneever any code repeatedly required then function recommended
def calculate(a,b):
    print("the sum:",a+b)
    print("the difference:",a-b)
    print("the product:",a*b)
calculate(20, 10)
calculate(200, 100)
calculate(2000,1000)
#advantage code reusability

#types of function
#built in functions or predefine function
id()
type()
print()


#user defined function/customised function
#syntax:
#def function_name(parameter):
    #'''doc_string'''
    
        #body of function
        
        #return some value
        
#keywords (1)def-mandatory (2)return-optional

#write prog to print wish
def wish():
    print("hello friends good morning")

wish()

#function parameter
#write program to wish student with name
def wish (name):
    print("hello",name,"good morning!!!")
wish("pankaj")

#write function to print the square the input no.
def squareit(num):
    sq=num*num
    print("the square of {},is:{}".format(num,sq))
squareit(2)
squareit(4)
squareit(2.0)

#return statement
#write function to accept two no and returns the sum
def add(a,b):
    sum=a+b
    return sum
result=add(20,10)
print("the sum:",add(20,10))

def f():
    print('hello')
    
x=f()
print("The return value is:",x)

#write a program to print the factorial of positive int value
def factorial(num):
    result=1
    while num >=1:
        result=result*num
        num=num-1
    return result
print("the factorial of 3 is:", factorial(3))

for i in range (1,6):
    print("the factorial of" ,i,"is:",factorial(i))
    
#returning multiple values from the function
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(20,10)
print("the sum is :",x)
print('the sub is:',y)

def cal(a,b):
    sum=a+b
    sub=a-b
    pro=a*b
    div=a/b
    return sum,sub,pro,div
t=cal(20,10)
print(t)
print("the results are:",t)
for x in t:
    print(x)
    
#types of arguments
#positional argument
def sub(a,b):
    print(a-b)
sub(200,100)#positional argument
sub(200,300)

#keyword argument
def sub(a,b):
    print(a-b)
sub(a=200,b=100)#keyword argument
sub(b=200,a=100)

def sub(a,b):
    print(a-b)
sub(a=200,b=100)#keyword argument
sub(200,100)#positional argument
sub(200,b=100)#first argument must be postional(valid)
sub(a=200,100)#first keyword argument is invalid

#default argument
def wish(name="guest"):#default argument
    print('hello',name,"good morning...")
wish()
wish("pankaj")

def wish(name,msg):#valid
    pass
wish('pankaj',"good")
def wish(name="guest",msg='good morning'):#valid
    pass

def wish(name,msg='good morning'):#valid
    pass

def wish (name:'guest',msg):#not valid because after default argument 
    pass                    #non argument not valid

#variable length argument-declare by *n
#n is internally tuple
def f(*n):
    print("variable length argument")
f()
f(10)
f(10,20,30)



def f(*n):
    print(n)
f()
f(10,20)
f((10,20,30),(40,50,60))

#types of argument
#1
def f(x,*y):
    print(x)
    print(y)
f(10,20,30,40)
f(10)
f()
#2
def f(*x,y):#variable length argument must be after normal argument(valid)
    print(x)
    print(y)
f(10,20,30,40)
f(10,20,30,y=40)

#3
#def f(*x,*y):
    #pass
     #cant take more than one variable lenth argument
      
#difference between *args and **kwargs
#*args is variable length argument
#f(*n)
#it is always tuple
#eg.
def f(*n):
    print(n)
f() # ()
f(10) #(10)
f(10,20) #(10,20)




#**kwargs 
#variable length keyword args
#f(**n)
#it is always Dictonary
def f(**x):
    print(x)
f() #{}
f(name="pankaj",marks=100) #{"pankaj":100}


#can *args and **kwargs is valid?
def f(*arg,**kwarg):
    print(arg)
    print(kwarg)
f(10,20,A=30,B=40)

#def f(**kwarg,*arg) after kwargument we can take normal argument

#case study
def f(agr1,arg2,arg3=4,arg4=3):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(10,20,30,40)
f(25,50,arg4=100)
f(arg4=5,arg1=6,arg2=9)
f()
f(arg3=20,arg4=30,40,50)#not valid
f(4,5,arg2=6)
f(4,5,arg3=6,arg5=9)#not valid

#types of variable(Local and GLobal)
#Global Variable=variable declare outside the function is called global variable
a=10
def f1():
    print(a)
    
def f2 ():
    print(a)
    
f1()
f2()

#local variabl=which declare inside the function is local variable
def f1():
    a=10
    print(a)
f1()

def f2():
    print(a)
f2()

#case
a=10
def f1():#whenever global variable are there then local variable are prefered
    a=20
    print(a)
def f2():
    print(a) #if variable is not define inside function the global variable is prefered
    
f1()
f2()


#global keyword
a=10 #global
def f1():
    global a
    a=20 #local
    print(a)
def f2():
    print(a)  
    
f1()
f2()
###
def f1():
    global a
    a=10
    print(a)
    
def f2():
    print(a)
    
f1()
f2()

#
a=777
def f():
    global a
    print(a)
    a=999
    print(a)
f()
#globals()for all global variable
a=888
def f():
    a=999
    print(a)
    print(globals().get(a))
    print(globals().d[a])
f()

#recursive function
#complex can be solve
#length of code reduced
#call it self is called recursive function

#factorial by using recursion
#n!=n*(n-1)!
#factorial(n)=n*factorial(n-1)
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print('Factorial of 3 is:',factorial(3))
factorial(5)

# to find factorial of 1-10
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
for i in range(1,11):
    print("the factorial of {} is : {}".format(i,factorial(i)))
    
#internal tracing of factorial function
def factorial(n):
    print('Execusion of factorial function with n values:',n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    print("Returning result of factorial({}),is:{}".format(n,result))
    return result
print(factorial(3))
factorial(3)=3*factorial(2)
factorial(3)=3*2*factoria(1)
factorial(3)=3*2*1*factoria(0)
factorial(3)=3*2*1*1

#Maximum recurssion depth in python#995
count=0
def factorial(n):
    global count
    count=count+1
    print('Execusion of factorial function with n values:',n)
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(3))
print("the no of times factorial function executed:",count)

#Lambda function= nameless function is called ananimous function
#nameless
#instant use/one time use
s=lambda n: n*n
print(s(4))
s=lambda n: n*n
for i in range(1,11):
    print("the square of {} is :{}".format(i,s(i)))
#write lambda function to find sum of two no
s= lambda a,b:a+b
print(s(10,20))

#finding bigger value
#2 input
s=lambda a,b : a if a>b else b
print(s(10,20))

#3 input
s= lambda a,b,c : a if a>b and a>c else b if b>c else c
print(s(10,20,30))


#Function as argument
filter(function, sequenc)
map(func, sequenc)
reduce(function,sequenc)

#filter() to reduce code
#to find even no.from list
#without filter function
l=[0,1,2,3,4,5,6,7,8,9,10]
def iseven(n):
    if n%2==0:
        return True 
    else:
        return False
l1=[]
for n in l:
    if iseven(n)==True:
        l1.append(n)
print(l1)

#with filter function
l=[0,1,2,3,4,5,6,7,8,9,10]
def iseven(n):
    if n%2==0:
        return True 
    else:
        return False
l1=list( filter(iseven, l))
print(l1)

#filter with lambda function
l=[0,1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda n : n%2==0,l))
print(l1)

#for odd no
l=[0,1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda n : n%2!=0,l))
print(l1)

#WAP for no divisible by three and odd no
l=[0,1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda n:n%3==0 and n%2!=0,l))
print(l1)

#WAP for heroiens name starts with "k"
heroiens=["katrina",'karina','anushka','sunny','dipika']
startswithk=list(filter(lambda name:name[0]=='k',heroiens))
print(startswithk)

#name length divisible by 5
heroiens=["katrinakaif",'karinakapoor','anushka','sunnyleoni','dipika']
divisibleby5=list(filter(lambda name:len(name)%5==0,heroiens))
print(divisibleby5)

#name length is odd
heroiens=["katrinakaif",'karinakapoor','anushka','sunnyleoni','dipika']
odd=list(filter(lambda name:len(name)%2!=0,heroiens))
print(odd)

#map()
#square of element
#without lambda funtion
l=[1,2,3,4,5]
def squareit(n):
    return n*n
l1=list(map(squareit,l))
print(l1)

#with lambda
l=[1,2,3,4,5]
l1=list(map(lambda n: n*n,l))
print(l1)

#map function multiple sequences

l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)

#
l1=[1,2,3,4,5,6,7,8]#extra elements are ignored
l2=[5,10,15,20,25]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)


#
l1=[1,2,3,4,5]
l2=[5,10,15,20,25]
l3=[2,4,6,8,9]

l4=list(map(lambda x,y,z:x*y+z,l1,l2,l3))
print(l4)

#reduce()function number of elements in to single element
#need not required list
#reduce is not inbuilt function of python
from functools import reduce
l=[5,10,15,20,25]
result=reduce (lambda x,y:x+y,l)
print(result)

#WAP for reduce the firs 100 no into sum
result=reduce(lambda x,y:x+y,range(1,101))
print(result)

