# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 16:27:33 2024

@author: Lenovo
"""

# Pyramid pattern printing 
# first alalise how many spaces required 
# second analise how many symabol required and then cod 
# input number of symbol need to print 
n = 4 
# two print * first spaces required are three and decreasing it n-i-1(n is 4 i is 0 and 1 =you will get 3 and so on )
# * symabol are in incrementing order 1,2,3 and son so to print i+1(0+1 = 1, and so on ) 
''' * 

   * * 

  * * * 

 * * * * 

* * * * *  '''
for i in range(n):
    print(" "*(n-i-1)+'* '*(i+1))
    print()

''' * * * * * 

    * * * * 

     * * * 

      * * 

       *  '''
n = 5 
for i in range(n):
    print(' '*(i) + '* '*(n-i))
    print()
    

#Diamond pattern printing
''' *     i =0
   * *    i = 1  space = (n-i-1)
  * * *   i = 2  star = (i+1)
 * * * *  i =3
* * * * * i = 4 ----- First half
 * * * * i = 0
  * * *  i = 1    space(i+1)
   * *   i = 2    star (n-i-1)
    *    i = 3'''

n = 5

for i in range(n): # i = 0,1,2,3
    print(' '*(n-i-1) + '* '*(i+1))
for i in range(n-1):
    print(' '*(i+1) + '* '*(n-i-1))
    
    
#  triangle
'''  * 
     * * 
     * * * 
     * * * * 
     * * * * *  '''
n = 5
for i in range(n):
    for j in range(i+1):
        print('* ', end = '')
    print()
    
# inverted triangle
''' 
* * * * * 
* * * * 
* * * 
* * 
* 
'''


''' 
    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5
'''
n = 5 
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
    

n = 5
for i in range(n):
    print(' '*(n-i-1), end = '')
    for j in range(i+1):
        print(j+1,end = ' ')
    print()
    

n = 5
for i in range(n):
    print(' '*(n-i-1), end = '')
    for j in range(i+1):
        print(chr(65+i),end = ' ')
    print()
    
n = 5
for i in range(n):
    print(' '*(n-i-1), end = '')
    for j in range(i+1):
        print(chr(65+j),end = ' ')
    print()
    


        
  