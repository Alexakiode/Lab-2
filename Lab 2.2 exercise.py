# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 11:19:35 2022

@author: Beth_El 2
"""

#Develop a Python function which either returns the 
#float square of its parameter x if the parameter is a number, 
#or prints the string "Sorry Dave, I'm afraid I can't do that" 
#if the parameter is a string, and then returns 0.0.

#Define square
def square(x):
#If function
    if type (x) == type(float(0.0)):
#Display format definition
        print("%d squared is equal to %.2f," %(x,x*x))
        return True
#Else function
    else:
         print("Sorry Dave, I'm afraid I can't do that")
#Printing both scenarios
square(4.0)
square("hello")

  #  num = float(1,2,3,4)
   # if num in num:
   #     print(2**2)
  #  else:
   #     print("Sorry Dave, I'm afraid I can't do that")

#square = x**x
#x = 2
#print(float(square))
#if square:
  #  print()
#else: 
 #   print("Sorry Dave, I'm afraid I can't do that")
    
    