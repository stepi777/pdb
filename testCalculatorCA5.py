#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:03:32 2018

@author: stepi77
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 15:36:43 2018

@author: stepi77
"""
list1 = [1,2,3,4]
list2 = [1,2,3,4]
    
import unittest

from classCalculatorCA5 import calculator

calc = calculator

class CalculatorTest(unittest.TestCase):
    
    def testAddition(self):
        self.assertEqual([2.0,4.0,6.0,8.0], calc.addition(list1, list2))
        
    def testSubtraction(self):
        self.assertEqual([0,0,0,0], calc.subtraction(list1, list2))
        
    def testMultiplication(self):
        self.assertEqual([1,4,9,16], calc.multiplication(list1,list2))
    
    def testDivision(self):
        self.assertEqual([1,1,1,1,], calc.division(list1,list2))
        self.assertEqual('It is not possible to divide a number by zero' , calc.division(list1,0))
    
    def testPowerOfTwo(self):
        self.assertEqual([1,4,9,16], calc.powerOfTwo(list1))
    
    def testSquareRoot(self):
        self.assertEqual([1.0, 1.4142135623730951, 1.7320508075688772, 2.0],calc.squareRoot(list1))
        
    def testSquare(self):
        self.assertEqual([1.0, 4.0, 9.0, 16.0], calc.square(list1))
    
    def testCube(self):
        self.assertEqual([1,8,27,64], calc.cube(list1))

    def testSine(self):
        self.assertEqual([0.8414709848078965, 0.9092974268256817, 0.1411200080598672, -0.7568024953079282], calc.sine(list1))
    
    def testCosine(self):
        self.assertEqual([0.5403023058681398, -0.4161468365471424, -0.9899924966004454, -0.6536436208636119], calc.cosine(list1))
    
    def testFactorial(self):
        self.assertEqual([1, 2, 6, 24], calc.fact(list1))
        self.assertEqual([1,2,6,1], calc.fact([1,2,3,0]))
        
    def testTangent(self):
        self.assertEqual([1.557407724654902, -2.185039863261519, -0.1425465430742778, 1.1578212823495775], calc.tangent(list1))
    
    def testArcTangent(self):
        self.assertEqual([0.7853981633974483, 1.1071487177940906, 1.2490457723982544, 1.3258176636680326], calc.arcTan(list1))

unittest.main()

