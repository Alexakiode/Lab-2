# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 00:31:08 2022

@author: Beth_El 2
"""

#Defining the half_pyramid
def half_pyramid(rows):
#Higlighting the input function
    rows=int(input("Enter the number of rows: "))
#Defining the rows and columns in range fucntion
    for r in range(1,rows + 1):
        for c in range(1, r + 1):
#Printing the result and terminating it on the same line
            print("*", end=" ")
        print()
            
half_pyramid(5)
            
            
            