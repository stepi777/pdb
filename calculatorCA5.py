#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:40:50 2018

@author: stepi77
"""
    
from classCalculatorCA5 import calculator

calc = calculator

choice = 0

while choice != 14:

    calc.menu()
    choice = calc.choice()
    print ('Choice: ', choice)
    
    if choice != 14:         
        list1 = []
        list1 = calc.askList()
        
        if choice <5:
            list2 = []
            list2 = calc.askList()
              
        if choice == 1:
            result = calc.addition(list1,list2)
            
        elif choice == 2:
            result = calc.subtraction(list1,list2)
        
        elif choice == 3:
            result = calc.multiplication(list1,list2)
        
        elif choice == 4:
            result = calc.division(list1,list2)
        
        elif choice == 5:
            result = calc.powerOfTwo(list1)
        
        elif choice == 6:
            result = calc.squareRoot(list1)
        
        elif choice == 7:
            result = calc.square(list1)
            
        elif choice == 8:
            result = calc.cube(list1)
            
        elif choice == 9:
            result = calc.sine(list1)
        
        elif choice == 10:
            result = calc.cosine(list1)
        
        elif choice == 11:
            result = calc.fact(list1)
            
        elif choice == 12:
            result = calc.tangent(list1)
        
        elif choice == 13:
            result = calc.arcTan(list1)
        
        print ('The result is = ', result)
        print ('')



    
