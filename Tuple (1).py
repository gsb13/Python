# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:51:16 2021

@author: Pankaj Dhas
"""

#TUPLE
#tuple is immutable
#order is applicable
#hetrogeneous object allowed
#indexing & slicing
#()
t=(10,20,30,40)
print(type(t))

#Singled valued tuple
t=(10)#int type
t=(10,)#','is required for tuple
print(type(t))

#creation tuple object
#empty tuple
t=()
#single valued tuple(,)
t=10,
t=(10,)
#multivalued tuple
t=10,20,30,
t=(10,20,30,)
#by using tuple function
#list
l=[10,20,30]
t=tuple(l)
print(type(t))
#range
t=tuple(range(1,11,2))
print(t)
#string
t=tuple("pankaj")
print(t)
#dynamic input
t=eval(input('enter tuple input:'))
print(type(t))

#accessing tuple object by using slice and index
#is as same as list
#mathematical operator(are same as list data type)
#concatination operator(+)
#repetation operator(*)
#concatination eg.(both argument should be tuple)
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
#repetation(repetation operator shold be int type)
t1=(10,20,30)
t2=t1*2
print(t2)
#equality operators for tuple
l1=('cat','rat','dog')
l2=('cat','rat','dog')
l3=('CAT',"RAT",'DOG')
l4=("Dog","cat","rat")

print(l1==l2)
print(l1==l3)
print(l1==l4)

print(l1!=l2)
print(l1!=l3)
print(l1!=l4)

l1=(10,20,30,40)#first elements of two list are compared
l2=(50,60)
l1<l2 
l1<=l2
l1>l2
l1>=l2

l1=(10,20,30,40)#first elements of two list are compared
l2=(5,60)
l1<l2
l1<=l2
l1>l2
l1>=l2


l1=('Roja','Rama')
l2=('Raja','Sunny')

l1<l2
l1<=l2
l1>l2
l1>=l2
#membership operators
l1=(10,20,30,40)

print(10 in l1)
print(50 not in l1)
print(70 in l1)

#len()and count() index()
l=(10,20,30,40)
print(len(l))
print(l.count(10))
print(l.count(50))

print(l.index(10))
print(l.index(50))


#reversing is not possible with tuple because of immutability
#by using python in built function(reversed()) we can change
t=(10,20,30,40)
r=reversed(t)
t1=tuple(r)
print("original tuple:",t)
print("reversed tuple:",t1)

#sorting is not possible with tuple because of immutability
t=(50,5,20,10,30,40)
s=sorted(t)
t1=tuple(s)
print("original tuple:",t)
print("sorted tuple:",t1)
#reverse order sorting
t=(50,5,20,10,30,40)
s=sorted(t,reverse=True)
t1=tuple(s)
print("original tuple:",t)
print("sorted tuple:",t1)

#max min function of Tuple
t=(50,5,20,10,30,40)
print(max(t))
print(min(t))

#append(),insert(),extend() this such function not applicable because of immutability
#remove(),pop()and clear() not applicable

#tuple packing and unpacking function
#packing
a=10
b=20
c=30
d=40
t=a,b,c,b
print(t)
#unpacking
t=(10,20,30,40)
a,b,c,d=t
print(a,b,c,d)

#comprehension(is not appliacable for tuple it shows type as "generator")
t=(x*x for x in range(1,6))
print(type(t))

#haseble or not
import collections
l=[10,20,30]
t=(10,20,30)
print(isinstance(l,collections.Hashable))

print(isinstance(t,collections.Hashable))
print(hash(t))


#due to unhashable list cant be added to set and dictionary
#tuple can be added to set and dict
s={10,20}
l=[10,20,30]
t=(40,30,50)
s.add(t)
print(s)
s.add(l)

d={}
t=(40,30,50)
d[t]='A'
print(d)

#program to take input from keyboard and print and sum and average
t= eval(input('enter tuple :'))
sum=0
for x in t:
    sum=sum+x
print('the sum:', sum)
print("average:",sum/len(t))

#Byusing readymade function
t= eval(input('enter tuple :'))
print('the sum:', sum(t))
print("average:",sum(t)/len(t))


#SET data type
#duplicates are no allowed
#order not applicable
#elements added based on hashcode
#indexing and slicing are not applicable
#{} represented
#hetrogeneous object allowed
#it is mutable

s=set()
s.add(10)
s.add('Z')
s.add("A")
s.add(20)
s.add(10)
print(s)

#creating set function
s=set()
#if objects are available then
s={10,20,30,40}
#by using set function
l=[10,20,30,40]
s=set(l)
print(s)

s=set(range(1,101,10))
print(s)

s=set("apple")
print(s)


s=eval (input("enter set valu:"))
print(s)
print('the sum:', sum(s))

#mathematical operators of set
#concatination(+)and repetation(*)are not applicable for SET

#relational operators for set
s1={10,20,30}
s2={20,10,30}
print(s1==s2)
print(s1!=s2)

s1={10,20,30}
s1={10,2,3,20,40}
print(s1<s2)
print(s1>s2)
print(s1<=s2)
print(s1>=s2)

#membership operator
s1={10,20,30}
print(10 in s)
print(50  in s)
print(50 not in s)

#function and method
s={10,20,30}
print(len(s))
s.add(50)
print(s)

s={10,20}
l=[20,30]
s.update(l)
print(s)
s.update(range(1,6),"durga")

#remove element from set
#remove()#if element is not available then will get key error
s={10,20,30,40}
s.remove(30)
s.remove(50)
print(s)


#discard()if sepcified element is not available then no error
s={10,20,30,40}
s.discard(30)
s.discard(50)
print(s)

#pop() remove random element from set
s={10,20,30,40}
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s)

#clear()
s={10,20,30,40}
print(s.clear())
print(s)


#set specific mathematical operation
#union()combine all element
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.union(s2)
s3=s1|s2 #can be used for union function
print(s3)

#intersection() combine common element
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.intersection(s2)
s3=s1&s2 #can be used for intersection function
print(s3)

#difference method= present in s1 but not in s2
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.difference(s2)
s3=s1-s2#(-)sign can take 
print(s3)


#symetric difference=element present in s1 but s2 and vice versa
s1={10,20,30,40}
s2={30,40,50,60}
s3=s1.symmetric_difference(s2)
s3=s1^s2#(^)sign can take 
print(s3)

#aliasing and cloning
#aliasing
#same concept like list data type


#set comprehension
#square of range(1,6)
s={x*x for x in range(1,6)}
print(s)

#2power square values for range(1,6)
s={2**x for x in range(1,6)}
print(s)


#program to eliminate duplicate element from list
#approch-1(creating list into set)
l=[10,20,10,20,10,30,20,30]
s=set(l)
print(s)

l=[10,20,10,20,10,30,20,30]
s=set(l)
l1=list(s) #approch 2(convert set again into list)
print(l1)


#approch 2(order of element is gaurntee)
l=[10,20,10,20,10,30,20,30]
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)


#program for diff vowel present in the word
word=input("enter some word to searh vowels:")
s=set(word)
v={'a','e','i','o','u'}
result=s.intersection(v)
print(result)










