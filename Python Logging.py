# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:53:10 2021

@author: Pankaj Dhas
"""

##Python Logging
#pyhton cantains its inbuilt "Logging" module
# there are 6  level
#CRITICAL(50)
#ERROR(40)
#WARNING(30)
# INFO(20)
# DEBUG (10)
# NOTSET(0)

#how to implement logging
#logging is inbuilt module in python
#in that basic config 
import logging
#loggin.basicConfig(filename='lof.txt: level=logging.WARNING)
# byusing which function we can write msg to the log file
#logging.critical(msg)
#logging.error(msg)
#logging.warning(msg)
#logging.info(msg)
#logging.degub(msg)

## write a program to create a log file to show WARNING and higher level msegges
import logging
logging.basicConfig(filename="log.txt", level=logging.WARNING)
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

##
import logging
logging.basicConfig(filename="log.txt", level=10)
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')


### data aapend
import logging
logging.basicConfig(filename="log.txt", level=logging.WARNING,filemode='a')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

### data overwrite
import logging
logging.basicConfig(filename="log.txt", level=logging.WARNING,filemode='w')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

#if file name is not specified then by default msg is displayed to consol
#if level is not specified then default level will be warning
#if file mode not specified then by default will be "a" append
import logging
logging.basicConfig()
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

### How to format log message
# using format keyword argument is used
logging.basicConfig(format='%(levelname)s')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

#
logging.basicConfig(format='%(levelname)s:%(message)s')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

#
logging.basicConfig(format='%(levelname)s:%(name)s:%(pathname)s:%(message)s')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

## how to add date and time to log msg
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

#to format date in dd/mm/yyyy format use datefmt
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p")
print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

#how to add exception information to log file
#sample prog.
import logging
logging.basicConfig(filename="mylog12062021.log",level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info("A new request came")
try:
    x=int(input("enter first no:"))
    y=int(input('enter second no:'))
    print ("the result :",x/y)
    logging.info("the result is generated successfully",x/y)
except ZeroDivisionError as msg:
    print('the value cant divide by zero')
    logging.exception(msg)
except ValueError as msg:
    print('enter int value')
    logging.exception(msg)
logging.info("request processing completed")























