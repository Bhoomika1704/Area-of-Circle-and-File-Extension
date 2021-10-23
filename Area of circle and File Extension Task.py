# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:28:26 2021

@author: Hp
"""
#Area of a circle
from math import pi
r= float(input("Enter radius of circle :"))
print ("Area of the circle is: " +str(pi * r**2))

#File Extension
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))