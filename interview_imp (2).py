# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 19:31:06 2024

@author: Lenovo
"""
# replace first two letters
a = 'Nokia Network'
l= a.split()

n = l[0][0:2]
n # No 
m = l[1][0:2]
m # Ne
l1 = a.replace(m,n,1)
l1
l1 = l1.replace(n,m,1)
l1

l = a.split()
n = l[0][0:2]
m = l[1][0:2]

l1 = a.replace(m,n,1)
l1 = l1.replace(n,m,1)
print(l1)
#anagram word list in seperate nested list
words = ["eat","ate","bat","tea","tab","cat",'tac']
print([''.join(sorted(word)) for word in words])
sort_word = set([''.join(sorted(word)) for word in words])

print(sort_word)

anagram_word = [[word for word in words if ''.join(sorted(word)) == word_sort] for word_sort in sort_word]

print(anagram_word)

# sort_word = set([''.join(sorted(word)) for word in words])
# anagramWord = [[ word for word in words if ''.join(sorted(word))== word1] for word1 in sort_word]
# print(anagramWord)
# written occurances of open close bracket
def return_occurrences(s):
    count = 0
    result = ""
    for i in range(len(s)):
        if s[i:i+2] == "()":
            count += 1
            result += "()"
    return result,count

s = "(()) ((() () () ))"
return_occurrences(s)
#('()()()()', 4)

def occurance(s):
    count = 0
    result = ''
    for i in range(len(s)):
        if s[i:i+2] == '()':
            count +=1
            result += '()'
    return result,count
a = occurance(s)
print(a)

occurrences = return_occurrences(s)
print(occurrences)

# palindrome and symmetrical
####
string = 'amaama'
half = int(len(string) / 2)
print(half)

first_str = string[:half]
print(first_str)
second_str = string[half:]
print(second_str)
# symmetric
if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')

# find the difference between two smallest no
l = [10,9,4,6]
sorted_l = sorted(l)
print(sorted_l)
smallest_difference = sorted_l[1] - sorted_l[0]
print(smallest_difference)



# addition of each number in the list
test_list = [12, 67, 98, 34]
#[1+2, 6+7, 9+8,3+4]
# [3, 13, 17, 7]
lis = []
for digit in test_list:
    sum = 0
    for ele in str(digit):
        sum += int(ele)
    lis.append(sum)
print(lis)

## unique
s = 'geeksforgeeks'
t =''
for i in s :
    if i in t:
        pass
    else:
        t = t +i
print(t)

# minimum and maximum key 
s = 'geeksforgeeks'
d = {}
for i in s:
    d[i] = d.get(i,0)+1
for key,value in d.items():
    s1 =  d.get(min(key))
print(d)
print(s1)

# word freq in string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
d = {key:test_str.count(key) for key in test_str.split()}
print(str(d))

lis = test_str.split()
d = {}
for i in range(len(lis)):
    d[lis[i]] = d.get(lis[i],0) + 1
print(d)
for k , v in d.items():
    print(f'{k} appears {v} times')

# sort string items on the basis of len
l = ['apple','banana','mango','kiwi']
l.sort(key = len, reverse=True)
print(l)

# rearrange with even no in descendin ordeer
#i/p = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#o/p = [1, 8, 3, 6, 5, 4, 7, 2, 9]
def rearrange(lst):
    result = []
    for i in range(len(lst)):
        if i%2 == 0:
            result.append(lst[i])
        else:
            result.append(lst[-i-1])
    return result
l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
output = rearrange(l)
print(output)

# Find twice occurance 
s = [1,1,2,2,2,3,3,5]
d = {}

for i in range(len(s)):
    d[s[i]] = d.get(s[i],0)+1
print(d)
output = []
for k,v in d.items():
    if v == 2:
        output.append(k)
print(output)

# bubble sort
arr = [10, 20, 4, 45, 99]  

for i in range(len(arr)-1):
    print(i)
    for j in range(len(arr)-1-i):
        print('j',j)
        print(arr[j],arr[j+1])
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)
l = arr
l[-2]

## replace character
def str_replace(text,ch):
    result = ''
    for i in text: 
            if i == ' ': 
                i = ch  
            result += i
    return result

text = "D t C mpBl ckFrid yS le"
ch = "a"

str_replace(text,ch)

# second high number
l =[2,4,6,7,8]
l1 = [l[i] for i in range(len(l)) if i < max(l)]
print(l1)
print(max(l1))

#create dictionary 
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

dict_word = {test_keys[i]:test_values[i] for i in range (len(test_keys))}
print(dict_word)

# three consecative number
arr = [1, 1, 1, 64, 23, 64, 22, 22, 22]

size = len(arr)
#print(size)

for i in range(size-2):
    if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
        print(arr[i])
        
lis = [1,2,3]
def comm(l):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(l[i],l[j],l[k])
    
comm(lis)

# find the list is in given range
test_list = [4, 5, 6, 7, 3, 9]

i,j = 3,9
res = True
for ele in test_list:
    if ele < i or ele >= j:
       res =  False
       break
print('the given list is in range :', res)

# count of add even number
list1 = [10, 21, 4, 45, 66, 93, 1]

c1 = 0
c2 = 0

for num in list1 :
    if num%2 == 0:
        c1 +=1
    else:
        c2 += 1
print(f'number of even numbers are {c1}')
print(f'number of odd numbers are {c2}')

# find positive numbers
list1 = [-10, 21, -4, -45, -66, 93]
for ele in list1:
    if ele >=0 :
        print(f'{ele}', end = ',')

# multiplication unique no
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
lis = []
for ele in test_list:
    if ele not in lis:
        lis.append(ele)
print(lis)
res =1
for i in lis:
    res = res * i
print(res)

# febbonacci series
def febbo():
    a,b = 0,1
    while True :
        yield a
        a,b = b,a+b
f = febbo()
print(next(f))

# joint two list with alterate words
s1 ='RAVIKIRAN'
s2 ='RAJA'

output = ''

i,j = 0,0

while i < len(s1) or j < len(s2):
    if i <len(s1):
        output += s1[i]
        i +=1
    if j < len(s2):
        output += s2[j]
        j +=1
print(output)

# generate new word from three string
s1 = 'abcdef'
s2 = 'xyz'
s3 = '12345'

output = ''
i=j=k=0

while i<len(s1) or j<len(s2) or k<len(s3):
    if i < len(s1):
        output = output + s1[i]
        i = i +1
    if j < len(s2):
        output = output + s2[j]
        j = j+1
    if k<len(s3):
        output = output +s3[k]
        k = k+1
        
print(output)

# function to write vowels count int string
def vowel_count(s):
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    d ={}
    for ch in s:
        if ch in vowel:
            d[ch] = d.get(ch,0) + 1
    for k , v in d.items():
        print('{} is occurs {} times'.format(k,v))
s = input('enter string:')
vowel_count(s)

# in the form of functio 
#character first and then count
# AAABBBBCD = A3B4C1D1
def int_chr(s):
    d ={}
    for ch in s :
        d[ch] = d.get(ch,0)+1
    output = ''
    for k,v in d.items():
        output = output +str(v)+k
    print(output)
    
s = 'AAABBBBCD'
int_chr(s)      
####
s = 'AAABBCCDDDFFFGGG'
# 3A2B2C3D3F3G
d ={}

for ch in s:
    d[ch] = d.get(ch,0) + 1
output = ''
for k,v in d.items():
    # output is str so v is int so converted in str
    output = output + str(v) + k
    
print(output) 

# a4b3c2 = aaaabbbcc

s = 'a423b3c2'
output= ''

for i in s:
    if i.isalpha():
        x = i
    else:
        output = output + x * int(i)
print(output)

# aaaabbbccz = 4a3b2c1z

# list comprihension function 
l =[2,4,6,7,8]
l1 = [x  if x%2 != 0 else 'Even' for x in l]
l1 

# common letter in two string
def common_ltr():
    s1 = input('enter a first string :')
    s2 = input('enter a second string :')
    
    str1 = set(s1)
    print(str1)
    str2 = set(s2)
    print(str2)
    comm = str1 & str2 
    
    print(comm)
    
common_ltr()

# two list to dictionary 
def list_to_dict():
    l1 = [1,2,3]
    l2 = ['one','two','three']
    d = dict(zip(l1,l2))
    print(d)
list_to_dict()

##
def max_num(num):
    max = num[0]
    
    for i in range(0,len(num)):
        if num[i] > max:
            max = num[i]
    return max
num = [2,3,5,8]
max_num(num)

##
def armstrong(num):
    orig_num = num
    len_num = len(str(num))
    output = 0
    while num > 0:
        reminder = num% 10
        output = (reminder ** len_num) + output
        num = num //10
        
    if output == orig_num :
        print('num is armstrong nu')
    else:
        print('no is not')
        
armstrong(153)
#9474

##
def palindrome(num):
    orig_num = num
    output = 0
    while num >0:
        reminder = num %10
        output =(output*10) + reminder
        num = num //10
        
    if orig_num == output :
        print('num is palindrome')
    else:
        print('no is not')
palindrome(151)

###
def primeno(num):
    count = 0
    if num >1:
        for i in range(1,num+1):
            if num%i == 0:
                count = count + 1
                
        if count ==2:
            print('num is prime')
        else:
            print('no')
            
primeno(5)

##
def fact(num):
    return 1 if num == 1 or num == 0 else num * fact(num-1)
        
fact(5)

# Input list
input_list = [1, 1, 2, 3, 4, 4, 5, 4, 6, 9, 9]

# Create a result list to store the elements and their occurrences
result = []

# Iterate through the input list
for i in input_list:
    # Check if the element is already processed
    is_processed = False
    for item in result:
        if item[0] == i:
            is_processed = True
            break
    
    # If not processed, count its occurrences
    if not is_processed:
        count = 0
        for j in input_list:
            if i == j:
                count += 1
        # Append the element and its count as a tuple to the result
        result.append((i, count))

# Print the output in the desired format
print(result)
for item in result:
    print(f"{item[0]}={item[1]}")
    

def is_balanced(s):
    # Stack to hold opening brackets
    stack = []
    
    # Dictionary to map closing brackets to their corresponding opening brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in brackets.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in brackets.keys():
            # Check if the stack is empty or if the top of the stack doesn't match
            if not stack or stack[-1] != brackets[char]:
                return False
            # If it matches, pop the top of the stack
            stack.pop()
    
    # If the stack is empty, the string is balanced
    return len(stack) == 0

# Example usage
input1 = "([]){}"
input2 = "([]{}"

print(is_balanced(input1))  # Output: True
print(is_balanced(input2))  # Output: False


def flatten_list(nested_list):
    """
    Function to flatten a nested list into a single-level list.
    
    Parameters:
    nested_list (list): A list that may contain other nested lists.

    Returns:
    list: A single-level flattened list.
    """
    # Initialize an empty list to hold the flattened elements
    flat_list = []

    # Define a helper function to recursively flatten the list
    def recursive_flatten(sublist):
        """
        Helper function to recursively process elements in the nested list.

        Parameters:
        sublist (list): A sublist (nested or not) to be processed.
        """
        for item in sublist:
            # Check if the current item is a list
            if isinstance(item, list):
                # If it's a list, call the function recursively
                recursive_flatten(item)
            else:
                # If it's not a list, append it to the flat_list
                flat_list.append(item)

    # Start the flattening process with the input nested list
    recursive_flatten(nested_list)

    # Return the fully flattened list
    return flat_list

# Input: Nested list
input_list = [1, [2, 3, [4, 5]], 6, [[7], [8, 9]]]

# Output: Flattened list
output = flatten_list(input_list)

# Print the output
print("Flattened List:", output)

# give pair of numbers which returns sum as 10 
nums = [10, 15, 3, 7, 1, 8, 4, 6, 2, 9]
target_sum = 10

lis = []

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target_sum:
            lis.append((nums[i],nums[j]))
print(lis)
     
#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class Divisiblebyseven:
    def __init__(self,n):
        self.n = n
    def generator(self):
        for num in range(self.n+1):
            if num%7 ==0:
                yield num
            
n = 50
divisible = Divisiblebyseven(n)

for n in divisible.generator():
    print(n)
    
##
# Sort by values in descending order
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict_desc = dict(sorted(my_dict.items(),key = lambda item : item[1]))

print("Sorted dictionary (descending):", sorted_dict_desc)
######################
import time

# Decorator function that logs the time of function execution
def log_function_call(func):
    """
    A decorator that logs the time and result of function execution.
    """
    def wrapper(*args, **kwargs):
        # Record the start time before function execution
        start_time = time.time()
        print(f"Function {func.__name__} called with arguments: {args} and keyword arguments: {kwargs}")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Record the end time after function execution
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds.")
        print(f"Result of the function call: {result}")
        
        return result
    
    return wrapper


# Example usage of the decorator:

# Applying the decorator to a function
@log_function_call
def add(a, b):
    """Adds two numbers."""
    return a + b

@log_function_call
def multiply(a, b):
    """Multiplies two numbers."""
    return a * b


# Calling the decorated functions
add(10, 5)
multiply(3, 4)


# Monkey patching 
class Class:
    def greet(self):
        print('Hello World')
        
obj = Class()
print(obj.greet())

def new_greet():
    print('hello from monkey patching')
    
Class.greet = new_greet()

print(obj.greet())

###
class A:
    def method(self):
        print("Method in A")

class B:
    def method(self):
        print("Method in B")

class C(A, B):
    pass

c = C()
c.method()  # Which method is called?

#### Example of the Diamond Problem:


class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")

class C(A):
    def method(self):
        print("Method in C")

class D(B, C):
    pass

d = D()
d.method()

### What is the Diamond Problem?

'''The **diamond problem** occurs when a class inherits from two or more classes 
that ultimately inherit from the same base class. This creates a "diamond-shaped"
 inheritance pattern.'''

###
import copy
# Shallow copy
original_list = [[1, 2, 3], [4, 5, 6]]

shallow_copied_list = copy.copy(original_list)

original_list[0][0] = 99  # Modifying the original list

print(shallow_copied_list)  # Changes are reflected in the shallow copy
    
import copy
# Deep copy 
original_list = [[1, 2, 3], [4, 5, 6]]

deep_copied_list = copy.deepcopy(original_list)

original_list[0][0] = 99  # Modifying the original list

print(deep_copied_list)  # Deep copy remains unchanged
        