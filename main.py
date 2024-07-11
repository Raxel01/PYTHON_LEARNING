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