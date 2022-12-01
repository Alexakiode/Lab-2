# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:07:52 2022

@author: Beth_El 2
"""
#Prime numbers from 2-18
#Defining the integer
i=int(input("Enter number greater than 2 "))
#Stating the condition using while loop
while i<=2:
    print("The number is invalid")
    #Define the integer for while loop again
    i=int(input("Enter number greater than 2 "))
#Define the number n and print n at the start
n = 2
print(n)
#Define the condition for less than i values requested
while n < i:
    #Defining the divisiblity with the if condition, n % 2
    if n % 2 == 0:
        pass
#Defining the else function
    else: print(n)
    #Defining the iteration, we need n = n+1
    n = n + 1