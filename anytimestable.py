# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:09:21 2022

@author: Beth_El 2
"""

#Defining timestable 
def timestable(x):
#Describing the loop using the range function
    for i in range(1,13):
#Printing only the integer lines
        print(i, x, i*x)
#Printing the integer lines with the words "times" and "is" for clarity
        print("%d times %d is %d" %(i, x, i*x))
#To have the timestable in a row and column like the popular table...notice the auto indentation after row line
    for row in range(1, 13):
        for col in range(1, 13):
#Printing the row and the column with appropriate line display
            print(row*col, end= " ")
        print()
        
        
