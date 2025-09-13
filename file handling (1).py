
  # -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:43:20 2021

@author: Pankaj Dhas
"""

#File Handling
#permenant storage of data 
# Types of file
#1.text file
#2.Binary file

#file opening python inbult function open()
# file=open(file name,mode)
# there are 7 mode r,w,a,r+,w+,a+,x
#r--read mode
# file= open ('abc.txt','r')
# if specified file does not find then FileNotfound error occurs

#w--write mode
#file =open ('abc.txt",'w')
#if specified file not found then it will be created
#data is over written

#a--append mode
#file=open('abc.txt','a')
#data is appended previous data keep as it is
#file is created if not available

# r+ -- read write mode
#file=open('abc.txt','r+')
#it will be used for read write operation
#data is over written 
#if file does not found then filenotfound error occurs

#w+ -- write read mode
#file=open('abc.txt','w+')
#it will uesd to write read operation
#data is over written
#if file not available then file will be created

#a+ -- append and read mode
# file=open('abc.txt','a+')
#data is not overwritten it will be appended
#file is created if not available

# x -- exclusive mode
# it is used for write operation
#if file is already available then file exist error occurs
# it is ment for new file to be written

#modes for binary file
#rb,wb,ab,r+b,w+b,a+b,xb

##closing a file
# f.close() is the function used

#various properties of file object
# f.name
# f.mode
# f.close

# f.readable()
# f.writable()

#methods to write test in file
# file =open('abc.txt', 'w')
#f.write(str)
# f.writelines(list of strings)
#eg. f.write(str)
file = 'F:\\xyz.txt'
f = open(file, 'w')
f.write("pankaj\n")
f.write("ramesh\n")
f.write("dhas\n")
f.write("aurangabad\n")
f.close()
print("data written suceesfully")

f = open('abc.txt', 'a')
f.write("pankaj\n")
f.write("ramesh\n")
f.write("dhas\n")
f.write("aurangabad\n")
f.close()
print("data written suceesfully")

#eg.f.writelines(list of strings)
f=open("abc.txt",'w')
l=['pankaj\n','shourya\n','raj\n']
f.writelines(l)
print('data written sucessfully')
f.close()

#write program to specify file name and data dynamically from keyboard
fname = input('enter file name:')
f=open(fname,'w')
while True:
    data= input('enter some string:')
    f.write(data + '\n')
    option=input('do you want add some more data [yes/no]:').lower()
    if option.lower()=="no":
        break
print('your provided data written to file sucessfully')
f.close()

#reading character data from text file
# f= open ('abc.txt','r')
# f.read()
# f.read(n)-- to read specific characters
# f.readline()--to read data line by line
# f.readlines()-- to read all lines at a time

#f.read()
f=open('abc.txt','r')
data=f.read()
print(data)
f.close()

#f.read(n)
f=open('abc.txt','r')
data=f.read(10)
print(data)
f.close()

f=open('abc.txt','r')
data=f.read(10000)
print(data)
f.close()

f=open('abc.txt','r')
data=f.read(-1)
print(data)
f.close()

#f.readline()
f=open('abc.txt','r')
line1=f.readline()
print('first line data:',line1, end='')
line2=f.readline()
print('second line data:',line1, end='')
line3=f.readline()
print('third line data:',line1, end='')
f.close()

##another method
f=open('abc.txt','r')
line=f.readline()
while line !="":
    print(line, end='')
    line=f.readline()
f.close()

# f.readlines()
f=open('abc.txt','r')
l=f.readlines()
for line in l :
    print(line,end='')
f.close()

#prog to read data from one file and writhing to another file
f1 = open('abc.txt','r')
f2 = open('output.txt','w')
data = f1.read()
f2.write(data)
f1.close()
f2.close()
print('data written succesfully')

f1=open('cricket.txt','r')
f2=open('output','w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()
print('data copied sucessfully')

## opening file "with" statement
#closing of file done automatically
with open ("abc.txt",'w') as f:
    f.write("pankaj\n")
    f.write('ramesh\n')
    f.write('dhas\n')
    f.write('aurangabad\n')
    print('is file closed:',f.closed)
print('is file closed:',f.closed)

## tell() -- it is used to ask current cursor position
f=open("abc.txt",'r')
print(f.tell())
f.read(2)
print(f.tell())
f.read(3)

#seek()--it is used to move cursor to specified location
f.seek(3)

#demo program for tell() and seek() method
f= open ('abc.txt','r')
print(f.tell())
f.seek(3)
print(f.tell())
print(f.read(3))
f.seek(20)
print(f.read())
f.seek(0)
print(f.read())


##demo
f = open ('abcd.txt', 'w')
f.write('All Students are stupids!!!')
with open ('abcd.txt', 'r+') as f:
    text = f.read() 
    print('data before modification:')
    print(text)
    print('the current cursor position:', f.tell())
    # seek from begining
    f.seek(17)
    f.write('Geems!!!')
    # seek to begining position
    f.seek(0)
    text = f.read()
    print('data after modification')
    print(text)
## How to check wether specified file available or not
## for this special library need to use i.e. "os'
## os.path.isfile(file name)

##program to read the file content 
import os
fname=input('enter file name:')

if os.path.isfile(fname):
    print('file exist:', fname)
    f=open(fname, 'r')
    text=f.read()
    print('the file content is')
    print('*' * 40 )
    print(text)
    print('*'*40)
    f.close()
else:
    print('file does not exist:', fname)
    
    
## program to read the program to count the no of lines,character and words
import os
fname=input('enter file name:')
if os.path.isfile(fname):
    print('file exist:',fname)
    lcount=wcount=ccount=0
    f=open(fname,'r')
    for line in f:
        lcount=lcount+1
        no_of_words_in_current_line=len(line.split())
        wcount=wcount+no_of_words_in_current_line
        no_char_in_current_line=len(line)
        ccount=ccount+no_char_in_current_line
        
    print('the no of lines is:', lcount)
    print('the no of word is:', wcount)
    print('the no of character is:', ccount)
else:
    print('file does not exist:', fname)
    
    
# writting data to csv file by using csv module
# for writting data csv writer must be required
# csv.write(file name)
import csv
with open('emp.csv', 'w', newline='') as f:
    w=csv.writer(f)
    w.writerow(['ENO', 'ENAME', 'ESAL', 'EADD'])
    while True:
        eno = int(input('enter employee no.:'))
        ename=input('enter employee name:')
        esal= float(input('enter employee salary:'))
        eadd= input('enter employee address:')
        w.writerow([eno,ename,esal,eadd])
        option=input('do you want to enter more record [yes/no]:')
        if option.lower()=='no':
            break
print('all employee record inserted sucessfully')
    
# reading date from csv file
# csv reader is required
with open ('emp.csv','r')  as f:
    r=csv.reader(f)
    data = list(r)
    print(data)
    
with open ('emp.csv','r')  as f:
    r=csv.reader(f)
    data = list(r)
    print(data)   
    for row in data:
        for coloumn in row:
            print(coloumn,'\t', end='')
        print()
        
# file zipping and unzipping
# filezip module is used
#zipping operation code
from zipfile import *
f=ZipFile('file15062021.zip', 'w', ZIP_DEFLATED)
f.write('abc.txt')
f.write('cricket.txt')
f.write('log.txt')
print('file15062021.zip created successfuly')
    

#unzip operation
from zipfile import *
f=ZipFile('file15062021.zip', 'r', ZIP_STORED)
names=f.namelist()
print('the file names:', names)
for name in names:
    f1=open("abc.txt",'r')
    text=f1.read()
    print('the file name:', names)
    print('the content of file')
    print()
    
    
    
#### Serialization and Deserialization
# Serialization-is conversion of python form to file supported form
# it is also called marshaling and pickling
# Deserialization- is conversion of file supported form into python supported form  
# it is also called unmarshalling and unpickling

# object serialization by using "Pickle module"
# for serialization dump()keyword is used
# for deserialization load() keyword is used
# eg
import pickle
emp= employee(100,"pankaj",1000,'raj')
with open ('emp.ser','w') as f:
    pickle.dump(emp,f)
    
with open ('emp.ser', 'r') as f :
    pickle.load(f)
    
#employee object serialization and deserialization using pickle 
class Employee:
    def __init__(self,ename,eno,esal,eadd):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadd=eadd
        
    def display(self):
        print('name:{} eno:{} esal:{} eadd:{}'.format(self.ename,self.eno,self.eadd,self.eadd))
e=Employee(100,'pankaj',5000,'aurangabad')
with open("employee.ser", 'wb') as f:
    pickle.dump(e,f)

with open('employee.ser','rb') as f:
    newobject=pickle.load(f)
newobject.display()  
    
## multiple employee object serialization and deserialization using pickle 
class Employee:
    def __init__(self,ename,eno,esal,eadd):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadd=eadd
        
    def display(self):
        print('name:{} eno:{} esal:{} eadd:{}'.format(self.ename,self.
                                            eno,self.eadd,self.eadd))
### object serialization
import pickle
f=open("employee.ser",'wb')
print('object serialization started')
while True:
    ename=input('enter employee name:')
    eno= int(input('enter employee no.:'))
    esal=float(input("enter salary:"))
    eadd= input('enter employee address:')
    e=Employee(ename,eno,esal,eadd)
    pickle.dump(e,f)
    option= input("do you want enter another employee detail[yes/no]:")
    if option.lower() == 'no':
        break
### object deserialization
f= open("employee.ser",'rb')
print('object deserialization is started')
while True:
    try:
        e=pickle.load(f)
        e.display()
    except EOFError:
        break
print('all object deserialization is done')
    
### JASON===Java Script Object Notation
# JASON is similar to dict data type in python
# for serialization in JASON dumps() and dump() keywords are used
# for deserialization loads() and load keywords are used
# jason module is inbuilt module in python

# when we want to conver python dict object to jason string then dumps() is used 
# for deserialization from jason string to python dict object then loads() is used

# when we want to python object to jason file then dump() keyword is used
# for deserialization of jason file to python dict object then load is used

# demo program to serialization of python dict to jason string
import json
employee={'name':'pankaj','age':35,'salary':25000, 'ismarried': True,'ishavinGF':None}

json_string= json.dumps(employee, indent=4,sort_keys=True) # serializing to string
print(json_string)

with open ('emp.json','w') as f:
    json.dump(employee,f,indent=4, sort_keys=True)   # file serialization
print('open emp.json file to read the data')


#object deserialization of jason string to python dict
json_string='''{
    "age": 35,
    "ishavinGF":null,
    "ismarried": true,
    "name": "pankaj",
    "salary": 25000
}'''

employee=json.loads(json_string)
print(employee)


# deserialization of jason file to python dict

with open ('emp.json','r') as f:
    employee=json.load(f)
print(employee)
for k,v in employee.items():
    print(k,':',v)


import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
bitcoin_info=response.json()
print(bitcoin_info)
print('Bitcoin Prise as on',bitcoin_info['time']['updated'])
print('1 Bitcoin prize=$',bitcoin_info['bpi']['USD']['rate'])


#serialize and deserialize customise class object
class Employee:
    def __init__(self,ename,eno,esal,eadd):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadd=eadd
    def display(self):
        print('ENAM:{} ENO:{} ESAL:{} EADD:{}'.format(self.ename,self.eno,self.esal,self.eadd))
e=Employee("pankaj",100,25000,'Pune')
#in jason object should be in dict
#e_dict={'ename':ename,'eno': eno,'esal':esal,'eadd':eadd}
e_dict= e.__dict__
json_string=json.dumps(e_dict) # string serialisation

#serialization to json file
with open ('emp.json', 'w') as f:
    json.dump(e_dict,f,indent=4)
    
# Deserialization
with open ('emp.json','r') as f:
    edict=json.load(f)
e=Employee(edict['ename'],edict['eno'],edict['esal'],edict['eadd'])
e.display()

## Jsonpickle module to overcome problem of json module
# here in this there is a encode() and decode() function
#demo program
import jsonpickle
class Employee:
    def __init__(self,ename,eno,esal,eadd,ismarried):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.eadd=eadd
        self.ismarried=ismarried
    def display(self):
        print('ENAM:{} ENO:{} ESAL:{} EADD:{} ismarried:{}'.format(self.ename,self.eno,self.esal,
                                                                   self.eadd,self.ismarried))
e=Employee("raj",100,25000,'Pune',True)
# serialization to json string
json_string = jsonpickle.encode(e)
print(json_string)

# serialization in json file
with open ('emp.json', 'w') as f:
    f.write(json_string)

#Deserialization of json string
e2= jsonpickle.decode(json_string)
e2.display()
# Deserialization of json file
with open ("emp.json", 'r') as f:
    json_string=f.readline()
e3=jsonpickle.decode(json_string)
e3.display()


# Yaml
emp_dict={'name':'pankaj',
          'age':30,
          'salary':25000.0,
          'ismarried':True}

from pyaml import *
# object serialization
yaml_string = yaml.dump(emp_dict)
print(yaml_string)
 
#serialization of yaml file
with open ('emp.ymal', 'w') as f:
    yaml.dump(emp_dict,f)

# Deserialization of yaml strin

new_dict = yaml.safe_load(yaml_string)
print(new_dict)

#deserialization of yaml file
with open ('emp.ymal','r') as f :
    new_dict2 = yaml.safe_load(f)
print(new_dict2)


















