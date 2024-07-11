import random
from auxiliere import *

movies = ['WAR', "Demolition", "Memory", "Inception"]

# movies.append('Fight Club') // add Element to the List
# movies.remove('WAR') 
# movies.pop();
# movies.insert(Index, "ElemToInsert")  // insert on a specific index
# .sort() 
# .clear() // clear the list

# 2D Lists : list of a lists :)
# hobbies = ['FootBall', 'Gaming', 'travel']
# enjoy = movies + hobbies
# print(enjoy)

username = 'Huxnnn'

nameHolder = 'Hello {} your welcome'
# print(nameHolder.format(username))

x = random.randint(1, 50);
y = random.random() 

food = ['hamburger', 'pocadios', 'Tajin']

favorite = random.choice(food)
gifts = [1, 3, 5 , 8 , 10, 13 , 15 , 136 , 19, 'A', 'B', 'C', 'd', 'E']

random.shuffle(gifts)

# print(favorite)
# print(gifts)
# try:
# result = 5 / 0
# except Exception:
    # print('Error Bro Here')

import os 

Path = '/Users/abait-ta/Desktop/PYTHON_LEARNING/File'

# if os.path.exists(Path):
#     print('Yes Path Exist')
#     if os.path.isfile(Path):
#         print('This is a file Yes')
# else:
#     print('this Path is not Available')

# try:
#     with open('Fil') as file:
#         print(file.read())
# except Exception as e:
#     hello(e)

# here I start The OOP :

# name should be capital OK: (best practice)
# 0:Model
# There is instance variable 

# class Car:
#     type = 'Cars' #class variable
#     def __init__(self, *args):
#         self.Model  =  args[0] #instance variable
#         self.Year   =  args[1]
#         self.color  =  args[2]
#         self.Horses =  args[3]
#     def CarPresentation(self):
#         print('Hello my name is {:^10}{:^10} {:^10} {:^10}'.format(self.Model, self.Year, self.color, self.Horses))

# CarMazda = Car('MAZDA2', 2024, 'red', 1000)
# Mercedes = Car('mercedes->206', 2010, 'green', 50)

# Car.type = 'ola'
# print(CarMazda.type)
# print('*******')
# print(Mercedes.type)

# CarMazda.CarPresentation()
# Mercedes.CarPresentation()

class Animal :
    alive= True
    def eat (self):
        print('This Animal is eating')
    def sleep (self):
        print('This Animal is sleeping')
    def Sound(self):
        print('This animal is general don\'t have a Sound')
    
class Rabbit(Animal):
     def eat (self):
        print('This Animal is eating yes I eat I\'m a rabbit')

class Fish(Animal):
    pass
class Hawk(Animal):
    pass

# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()


# rabbit.eat()
# fish.Sound()
# hawk.Sound()

class rectangl:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class square(rectangl):
    def __init__(self, length, width):
        super.__init__(length, width)
        

class Cube (rectangl):
    def __init__(self, length, width, height):
        self.height = height
        super.__init__(length, width)























