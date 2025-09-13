# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 19:08:41 2021

@author: Pankaj Dhas
"""

#excetion Handaling
#synatax Error:this error because synatical mistake
#run time error also called exception
#this error because of end user 
#exception handling is applicable to run time error
#not for syntax erroe
#errors are: 1.zero division error,2.file not found error, 3.
#unwanted,unexpected event occur and distrub the normal flow is exception

#Objective of excetion handling
#graceful/normal termination of resources
#resources should not get blocked
#nothing should be missed due to abnormal termination

#by using alternative way you continue you work is exception handling
#at run time something goes wrong then we have alternative to handle it normaly
#is nothing but exception handling

##Default exception hadling by python
#if any excetion is occured and exception handling code is not available
#then python terminate program there only is abnormal termination
#if exception hadling code is available then code get executed normally
#eg
print('hello')
print(10/0)
print('hi')

#customized exception handling by using try-except 
#code may rise exception is called risky code
#risky code is always take into try block
#try:
    #risky code
#except:
    #handling code
    
print('hello')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print('hi')

#Control flow in try and except
try:
    print("stm-1")
    print("stm-2")
    print("stm-3")
except :
    print("stm-4")
print("stm-5")

## there is no exception
#1,2,3,5 Normal termination

#if there exception raise at stm-2 and corresponding except is matched
#then 1,4,5 normal termination
#in this situation remaining try block statement wont be executed
#so the all risky code should be taken into try block only
#because after exception occured there is no gaurantee of execution of remaining try block statement
#length of try compulsary should be less

#if there exception raise at stm-2 and corresponding except block is not matched
# then 1,Abnormal termination

#if exception raise at stm-4 or stm-5
#which does not belong to try block
#always abnormal termination

## How to print exception information to the consol
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("the type of exception:",type(msg))
    print('the type of exception:',msg.__class__)
    print('the exception class name is:',msg.__class__.__name__)
    print('the discription of exception:',msg)


##eg
try:
    x=int(input('enter first no:'))
    y=int(input('enter second no:'))
    print('the result:',x/y)
except BaseException as msg:
    print("the type of exception:",type(msg))
    print('the type of exception:',msg.__class__)
    print('the exception class name is:',msg.__class__.__name__)
    print('the discription of exception:',msg)

###try with multiple except block
try:
    x=int(input('enter first no:'))
    y=int(input('enter second no:'))
    print('the result:',x/y)
except ZeroDivisionError:
    print('the value cant divided by zero')
except ValueError:
    print('enter int value only')
    
## order of exception handling is from top to bottom
try:
    print(10/0)
except ZeroDivisionError:
    print('zero division error')
except ArithmeticError:
    print('arithmetic error')
    
##
try:
    print(10/0)
except ArithmeticError:##is parent class of zero division error
    print('arithmetic error')
except ZeroDivisionError:
    print('zero division error')

#single except block that can handle multiple exception
try:
    x=int(input('enter first no:'))
    y=int(input('enter second no:'))
    print('the result:',x/y)
except(ZeroDivisionError,ValueError) as msg:
    print('the exception name:',msg.__class__.__name__)
    print('enter valid no.')

##default except block- it can handle any exception
#default except block must be last except block
try:
    x=int(input('enter first no:'))
    y=int(input('enter second no:'))
    print('the result:',x/y)
except ZeroDivisionError:
    print('the value cant divided by zero')
except:    #default except block
    print("deafult except block: enter valid input")

## various syntax for except block
# except ZeroDivisionError:
# except (ZeroDivisionError):
# except ZeroDivisionError as msg:
# except ZeroDivisionError) as msg:
# except (ZeroDivisionError,ValueError):
# except (ZeroDivisionError,ValueError) as msg:
# except:
 
    
##Finally Block
#resource deallocation code/clean up code wont be used in try block
#because if it is not used then resources remain in use condition
##resource deallocation code/clean up code wont be used in except block
# if exception dont come in try block then except code will never execute
#then finally block is recommanded to use for resource deallocation/clean up
# finally block is always execute wether exception raised or not

# case-1: if no exception 
try:
    print('try')
except ZeroDivisionError:
    print('exception')
finally:
    print('finally')
# case-2: if exception raised 
try:
    print('try')
    print(10/0)
except ZeroDivisionError:
    print('exception')
finally:
    print('finally')
# case-3: if exception raised but not handled 
try:
    print('try')
    print(10/0)
except ValueError:
    print('exception')
finally:
    print('finally')
    
# os._exit(0)-in this senario only finally block does not execute
import os
try:
    print('try')
    os._exit(0)
except ZeroDivisionError:
    print('exception')
finally:
    print('finally')

#Control flow in try, except and finally
try:
    print("stm-1")
    print("stm-2")
    print("stm-3")
except :
    print("stm-4")
finally:
    print("stm-5")
print("stm-6")

## there is no exception
1,2,3,5,6
#if there exception raise at stm-2 and corresponding except is matched
1,4,5,6 #normal termination
#if there exception raise at stm-2 and corresponding except block is not matched
1,5 #abnormal termination
#if exception raise at stm-4
#it is abnormal termination only finally block get executed
5
#if exception raise at stm-5 or stm-6
#it is abnormal termination

### Nested Try-Except-Finally
#where too much risky code then we can use nested try-except 
#eg.
try:
    print('outer try block')
    try:
        print('inner try block')
    except ZeroDivisionError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')

##ge exception raised
try:
    print('outer try block')
    try:
        print('inner try block')
        print(10/0)
    except ZeroDivisionError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')

###eg.exception raised to inner try block and not matched with inner except block
##control goes to outer finally block
#before going control to outside except block inner finally block get executed
try:
    print('outer try block')
    try:
        print('inner try block')
        print(10/0)
    except ValueError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')
##eg exception raised inside outer try block
#then inner try block does not start using any inside block resoureces
#due to that inside finally block wont execute
try:
    print('outer try block')
    print(10/0)
    try:
        print('inner try block')
        
    except ZeroDivisionError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')
    
### control flow in nested try-except-finally
try:
    stm-1
    stm-2
    stm-3
    try:
        stm-4
        stm-5
        stm-6
    except xxx:
        stm-7
    finally:
        stm-8
    stm-9
except yyy:
    stm-10
finally:
    stm-11
stm-12

#case-1 if there is no exception
1,2,3,4,5,6,8,9,11,12 #execute(NT)

#case-2 if exception raised at stm-2 and corresponding block matched
1,10,11,12 #execute (NT)

#case-3 if exception raised at stm-2 and corresponding block not matched
1,11 #(abnormal termination)

#case-4 if exception raised at stm-5 and inner corresponding except block matched
1,2,3,4,7,8,9,11,12 #normal termination

#case-5 if exception raised at stm-5 and inner corresponding except block not matched
# but outer except block matched
1,2,3,4,8,10,11,12 #(NT)

#case-6 if exception raised at stm-5 and inner corresponding except block not matched
# and outer except block not matched
1,2,3,4,8,11 # abnormal trmination

#case-7 if exception raised at stm-7 and corresponding except block matched
#1,2,3,(4,5,6)#may or may not execute 8,10,11,12 execute (normal termination)

#case-8 if exception raised at stm-7 and corresponding except block not matched
#1,2,3,(4,5,6)#may or may not execute 8,11 execute (abnormal termination)

#case-9 if exception raised at stm-8 and corresponding except block matched
#1,2,3,(4,5,6,7)may or may not execute 10,11,12 #NT

#case-10 if exception raised at stm-8 and corresponding except block not matched
#1,2,3,(4,5,6,7)may or may not execute 11 abmormal termination

#case-11 if exception raised at stm-9 and corresponding except block matched
#1,2,3,(4,5,6,7)may or may not execute 8,10,11,12 #NT

#case-12 if exception raised at stm-9 and corresponding except block not matched
#1,2,3,(4,5,6,7)may or may not execute 8,11 abnormal termination


###Various combination of try except finally 

#types of exception
##preddefined
## user defined or customized exception
#how to raise and define customized exception
# raise keyword is used
class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg=msg
raise TooYoungException("wait for some more tear u will get best match....")

##demo prog of matrimonial site

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg=msg     
age= int(input('enter your age:'))

if age >60:
    raise TooOldException("your age is not compatable for marriage....sorry")
elif age<18:
    raise TooYoungException("you are too young....wait some time")
else:
    print('best match will be email to you soon....')
    



















