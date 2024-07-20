import random
from auxiliere import *
from abc import ABC, abstractmethod


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

# class rectangl:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class square(rectangl):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#     def _area_(self):
#         return self.length * self.width
        

# class Cube (rectangl):
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#     def __volume__(self):
#         return self.height * self.width * self.length


# # Summary : 
# # So on python we have the oop olso so that Mean this language use object , when we talk a bout a classs we can Define as 
# # user defined data TYPE
# #object is an instance of this class so the object will ontian all attributes 
# mysquare = square(9, 3)
# cube = Cube(1, 2 ,8)

# print(mysquare._area_());

# print(cube.__volume__());

class vehicul(ABC):
    @abstractmethod
    def _max_speed_(self, distance, temps):
        pass

class Car(vehicul):
    def __init__(self, distance, temps):
        self.Distance = distance
        self.Temps = temps

    def _max_speed_(self):
        print(int(self.Distance / self.Temps))

# myVeh = Car(150, 50);
# myVeh._max_speed_()

class Pontalon:
    color = None
    def _print_color(self):
        print(self.color)

def _set_color_(pntobj , color):
    pntobj.color = color


pnt = Pontalon()

# pnt._print_color();

_set_color_(pnt, 'Yellow')

# pnt._print_color();

# print(name := 'Hello mother Fucker')
# Assign a variable to a function
# say = print

# say('What The Fuck')

#Higher Order Fucntion : accept a function as an argument
#return a function

def UpperIt(name):
    name = name.lower();
    print(name)

def _give_name_(funct, Name):
    funct(Name)

# _give_name_(UpperIt, 'AbdelalI')

def funct1(n1):
    def func2(n2):
        return n1 / n2
    return func2
# essai1 = funct1(10)
# print(essai1(5))


#lambda fUNCRION ARE A FUNCTION writen on one line beginning by lambda keyword 
# they accept more thatn one param and have only on expression

# year = 2024
agecalc = lambda year: 2024 - year

# print(agecalc(1996))
#Sorted Return a list of sorted iterable on python 
# sort() sort in place for lists
# for iterables you can Use sorted()

# sort a list
Abreviation = (
               {'MAR' : 'Maroc'},
               {'GAB' : '9elawa'},
               {'USA' : 'United State of America'}
            )

store = [
        ('foul' , 20),
        ('oil'  , 5),
        ('Tango', 90)
]

effector = lambda data:data[1] >= 18

NewStore =list(filter(effector, store))

# print(NewStore)
# print(NewStore)
# Define a custom function to extract the key from each dictionary in the tuple
# get_key = lambda tuple: tuple[0].items()

# print(get_key(Abreviation))
# Sort the tuple using sorted and the custom key function
# sorted_tuple = sorted(Abreviation, key=get_key)

# print(sorted_abbr)
# status = lambda Abreviation: Abreviation[0]

# print(status(Abreviation))

# for dictelem in Abreviation:
#     for key, value in dictelem.items():
#         print(key, value)

# value = lambda values: values.keys()

# mySortedList = sorted(Abreviation, key=value);

# print(mySortedList)

# new

marks = [100, 50, 40, 33, 16, 48]

accepted = [i for i in marks if i >=50]
# result = [float(i / 2) for i in range(4, 10)]
# print(accepted)

weather = {
    'New York': 'sunny',
    'Boston' : 'snny',
    'Los Angles' : 'bunny',
    'Chicago' : 'sunny',
    }

weather_filter = {key: value for (key, value) in weather.items() if value == 'sunny'}
# {key: (expression) fro (key, value) in iterable if condition}
# print(weather_filter)

username =  ['user1', 'user2', 'user3']
passwords = ['@@@212', '#$%20']

usersData = list(zip(username, passwords))

# [print(i) for i in usersData]

# {key: print('pass : ' + value) for (key, value) in usersData.items()}
# import time
# print(time.ctime(2))

# import threading

# amount = 150

# def first_run():
#     print('first increme')

# def sec_run():
#     print('sec increme')

# print('Hola')

# x = threading.Thread(target=first_run, args=())
# x.start()

# y = threading.Thread(target=sec_run, args=())
# y.start()

# print(amount)

# print(threading.active_count())

# print(threading.enumerate())

import smtplib 
sender = 'aittalbabdelalie@gmail.com'
receiver = 'hamzayounsi006@gmail.com'
subject = 'python email test'
body = 'python email test by Me '

message = f"""From: {sender}
To: {receiver}
Subject = {subject}\n
{body}

"""