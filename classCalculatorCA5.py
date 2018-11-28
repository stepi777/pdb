#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:40:55 2018

@author: stepi77
"""

import math
  
class calculator():
    
    def menu():
        print(' 1 Addition\t 2 Subtraction\t 3 Multiplication\n 4 Division\t 5 Exponent\t 6 Square Root\n 7 Square\t 8 Cube\t\t 9 Sine\n 10 Cosine\t 11 Factorial\t 12 Tangent\n 13 Arc Tangent\t 14 Exit')
    
    def choice():
        return int(input('Make your choice (between 1 and 14): '))

    def askList():
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        print('Type list of numbers. Press the letter a when finished')
        value = 0
        sequence = []
        while value != 'a':
            value = input('insert value: ')
            if is_number(value):
                sequence.append(float(value))
            elif value != 'a':
                print('Please input only numers')
        return sequence
        
    def addition(a,b):
        add = list(map(lambda x,y: x+y, a,b))
        return add
        
    def subtraction(a,b):
        sub = list(map(lambda x,y: x-y, a,b))
        return sub
    
    def multiplication(a,b):
        mul = list(map(lambda x,y: x*y, a,b))
        return mul
    
    def division(a,b):
        if b == 0:
            print('It is not possible to divide a number by zero')
        else:
            div = list(map(lambda x,y: x/y, a,b))
            return div
      
    def powerOfTwo(a):
        def powerOf(a):
            return math.pow(a,2)
        power = list(map(powerOf, a))
        return power
    
    def squareRoot(a):
        def squareRootFunction(a):
            return math.sqrt(a)
        values = (list(map(squareRootFunction, a)))
        return values
    
    def square(a):
        def squareFunction(a):
            return (float(a)*float(a))
        values = (list(map(squareFunction, a)))
        return values
    
    def cube(a):
        def cubeFunction(a):
            return(float(a)*float(a)*float(a))
        values = (list(map(cubeFunction, a)))
        return values
    
    def sine(a):
        def sineFunction(a):
            return(math.sin(a))
        values = (list(map(sineFunction, a)))
        return values
    
    def cosine(a):
        def cosineFunction(a):
            return (math.cos(a))
        values = (list(map(cosineFunction, a)))
        return values
    
    def fact(a):
        def factFunction(a):
            return (math.factorial(a))
        values = (list(map(factFunction, a)))
        return values
    
    def tangent(a):
        def tangentFunction(a):
            return (math.tan(a))
        values = (list(map(tangentFunction, a)))
        return values
    
    def arcTan(a):
        def arcTanFunction(a):
            return(math.atan(a))
        values = (list(map(arcTanFunction, a)))
        return values
    
    

        
    