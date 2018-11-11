# pdb


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 11:50:10 2018

@author: stepi77
"""

# This is a superclass, the type sedan is not really used in the program, but I created it to have a common class for the 4 subclasses
class Car(object):
    def __init__(self): 
        self.type = 'Sedan'

# The following 4 are subclasses. Each of them is needed for each of the different objects in the carfleet: petrol, electric, diesel and hybrid
class petrolCar(Car):
    def __init__(self):
        self.uses = 'Petrol'
        
class dieselCar(Car):
    def __init__(self):
        self.uses = 'Diesel'
        
class electricCar(Car):
    def __init__(self):
        self.uses = 'Electric'
    
class hybridCar(Car):
    def _init__(self):
        self.uses = 'Hybrid'
        
# This carFleet contains the functions of initialization of the carfleet, 
# the getters and the rest.    
class CarFleet(object):
    
# This function initializes the carfleet
    def __init__(self):
        self.petrolCars = []
        self.dieselCars = []
        self.electricCars = []
        self.hybridCars = []
          
# The following 4 getters return the ammount of the cars available in stock for each type
    def getPetrolCars(self):
        return self.petrolCars
    
    def getDieselCars(self):
        return self.dieselCars
    
    def getElectricCars(self):
        return self.electricCars
    
    def getHybridCars(self):
        return self.hybridCars
 
# The following function creates the original stock, adding for example 20 petrolCars 
# using the function Append
    def createStock(self):
        for i in range(20):
            self.petrolCars.append(petrolCar())
        for i in range(8):
            self.dieselCars.append(dieselCar())
        for i in range(8):
            self.electricCars.append(electricCar())
        for i in range(4):
            self.hybridCars.append(hybridCar())

# This function is requested to advise the user of the program regarding the stock available. 
# It gives the LENGTH of the stock for each type of car
    def checkStock(self):
        print('Availability:')
        print('Petrol Cars:', + len(self.getPetrolCars()))
        print('Diesel Cars:', + len(self.getDieselCars()))
        print('Electric Cars', + len(self.getElectricCars()))
        print('Hybrid Cars:', + len(self.getHybridCars()))
        
# This function allows us to subtract the ammount of car rented from the stock.
# It checks first if the ammount of cars rented is available on the stock. 
# If yes, the rental process can proceed, otherwise it responds "not enough cars in stock
# and brings the user back to the rental process
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print ('Not enough cars in stock')
            return
        total = 0
        while total < amount: 
           car_list.pop()
           total = total + 1

# This function allow the user to return the cars into the corresponding pool 
# or add cars to the stock. If the owner of the Aungier Car Fleet buys more cars, he can 
# use the returnRental function to add them into the stock. I decided, to semplify
# the process of adding new cars to the stock, to unify the return of the cars and 
# the "adding new cars" into the stock in only one function
    def returnRental(self, car_list, amount):
        for i in range(amount):
           car_list.append(amount)
           
           
# This function allows the user to rent the cars asking if he wants to rent a car. If not, the 
# program asks if he wants to return or Add cars into the stock. In both cases it asks 
# what type of cars the user of the program wants to return or add and how many.
    def processRental(self):

        answer = input('Would you like to rent a car? y/n: ')

        if answer == 'y':
            while 1==1:
                try:
                    choice = int(input('What type of car do you need?\n1: Petrol\t2: Diesel\t3: Electric\t4: Hybrid\n'))
                    break
                except:
                    print('Please select a value between 1 and 4')
            if choice >4:
                print("Invalid selection")
            else:
                while 1==1:
                    try:
                        amount = int(input('How many cars would you like to rent?'))
                        break
                    except:
                        print("You must enter a integer value")
                
                if choice == 1:
                    self.rent(self.petrolCars, amount)
                elif choice == 2:
                    self.rent(self.dieselCars, amount)
                elif choice == 3:
                    self.rent(self.electricCars, amount)
                else:
                    self.rent(self.hybridCars, amount)
                self.checkStock()
        elif answer == 'n':
            answer2 = input('Would you like to return a car or add cars to the stock? y/n: ')
            if answer2 == 'y':
                while 1==1:
                    try:
                        ReturnChoice = int(input('What type of car are you returning or adding?\n1: Petrol\t2: Diesel\t3: Electric\t4: Hybrid\n'))
                        break
                    except:
                        print('You must enter a integer value between 1 and 4')
                if ReturnChoice >4:
                    print("Please note that the selection has to be between 1 and 4")
                else:
                    while 1==1:
                        try:
                            amount = int(input('How many cars would you like to return or add?'))
                            break
                        except:
                            print("You must enter a integer value")                
                    if ReturnChoice == 1:
                        self.returnRental(self.petrolCars, amount)
                    elif ReturnChoice == 2:
                        self.returnRental(self.dieselCars, amount)
                    elif ReturnChoice == 3:
                        self.returnRental(self.electricCars, amount)
                    else:
                        self.returnRental(self.hybridCars, amount)
                    self.checkStock()
            else:
                print('Invalid selection')
        else:
            print('Invalid selection')
            
AungierCarFleet = CarFleet()
AungierCarFleet.createStock()
AungierCarFleet.checkStock
proceed = 'y'
while proceed == 'y':
    AungierCarFleet.processRental()
    proceed = input("Would like to continue? select 'y' to continue or any other key to exit: " )










