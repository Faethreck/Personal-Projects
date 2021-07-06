import random
from random import randrange

def rand5():
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        number = 0
        for x in numbers:
            number = i + x
            number = number * 2
            number = number - 2
            number = number / 2
            if number > 4:
                number = 0
            print(number)
        
rand5()