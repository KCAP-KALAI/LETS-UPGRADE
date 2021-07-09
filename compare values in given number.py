# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 05:42:36 2021

@author: KALAI
"""

print("Check the givennumbers are equal or sum of the numbers is 5 or difference of the numbers is 5")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
def check(a,b):
    if a == b or (a-b) == 5 or (a+b) == 5 or (a+b) == 5:
        return True
    else:
        return False
print("Condition of the given number is : ",check(a,b))