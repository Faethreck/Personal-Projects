import random 
from random import randrange

################################ VARIABLES / LISTS ##############################################################

characters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!','@','#','$','%',
              '^','&','*','(',')','-']
password = ''
password_state = True

################################ HELPER FUNCTIONS ###############################################################

def password_input(): # function to input your password
    global password
    password = input('Enter your password here: ')
    return str(password)

def rnd_char(start,stop): # picks a random value from the list characters
    number = random.randrange(start,stop)
    return characters[number]

def password_generator(): # generates a random password with all the requirements
    global range 

    gen_password = ''
    letter = 0
    symbol = 0
    numbers = 0

    for first in range(6):
        start = 0
        stop = 25
        char = rnd_char(start,stop)
        gen_password += char
    
    for second in range(3):
        start = 25
        stop = 36
        num = rnd_char(start,stop)
        gen_password += num

    for third in range(3):
        start = 36
        stop = 46
        sym = rnd_char(start,stop)
        gen_password += sym

    for x in gen_password:
        if x in characters[25:36]:
            numbers += 1
        elif x in characters[0:25]:
            letter += 1
        elif x in characters[36:46]:
            symbol += 1

    total = letter + symbol + numbers

    if total > 12:
        password_state = True
    if symbol == 0:
        password_state = True
    if numbers < 2:
        password_state = True
    if total < 8:
        password_state = True
    
    if total >= 8 and total <= 12 and symbol > 0 and numbers >= 2:
        password_state = False
    
    print(gen_password)

def input_receiver(): # in case the user suggests a password this function will check for conditions
    global password_state
    
    letter = 0
    symbol = 0
    numbers = 0

    for x in password:
        if x in characters[25:36]:
            numbers += 1
        elif x in characters[0:25]:
            letter += 1
        elif x in characters[36:46]:
            symbol += 1

    total = letter + symbol + numbers

    if total > 12:
        print("The maximum capacity for the password is 12.")
    if symbol == 0:
        print("You need at least one symbol in your password.")
    if numbers < 2:
        print("You need at least two numbers in your password.")
    if total < 8:
        print("You need at least eight characters in your password. ")
    
    if total >= 8 and total <= 12 and symbol > 0 and numbers >= 2:
        print("Perfect password! ")
        password_state = False


################################### PROGRAM ###############################################################

while password_state == True:

    question = input('Do you want a generated password? ')
    if question == 'yes':
        password_generator()
    elif question == 'no':
        password_input()
        input_receiver()
    
