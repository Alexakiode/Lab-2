# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 02:41:11 2022

@author: Beth_El 2
"""

#Defining the half_pyramid
def pyramid(rows):
#Higlighting the input function
    rows=int(input("Enter the number of rows: "))
#Defining the rows and columns in range fucntion
    for r in range(1,rows + 1):
        for c in range(1,r + 1):
            
#Modifying the function so that it prints pyramid
            for r in range(1,rows):
                for c in range((rows + 1)):
                    print(end="")
                for c in range (r+1):
                    print("*", end=" ")
#Printing the result and terminating it on the same line
                    print("*", end=" ")
                    print()
            
pyramid(5)
            

#Defining the half_pyramid
def half_pyramid(rows):
#Higlighting the input function
    rows=int(input("Enter the number of rows: "))
#Defining the rows and columns in range fucntion
    for r in range(1,rows + 1):
        for c in range(1, r + 1):
            for r in range(1,r):  
                
#Printing the result and terminating it on the same line
                print("*", end=" ")
            print()
            
half_pyramid(5)