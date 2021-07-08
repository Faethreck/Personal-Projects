import simplegui
import random
import math

print('|New Game|')
secret_number = random.randrange(0,100)
turns = 1
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    frame = simplegui.create_frame('Guess the number',200,200)
    frame.start
    inputer = frame.add_input('Enter guess: ', input_guess, 50)
    button100 = frame.add_button('100', range100,50)
    button1000 = frame.add_button('1000', range1000,50)
    range100()
    
    
def turn_counter(number):
    if number <= 0:
        print('Nice Try!' + '\n' + '|New Game|' + '\n')
        new_game()
    elif number > 0:        
        calc = number - 1 
        print('You have ' + str(calc) + ' turns')    
        return calc
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    global turns
    turns = 8
    turn_counter(turns)
    print('Range is [0,100)')
    return secret_number

def range1000():
    print('|New Game|')
    global secret_number
    secret_number = random.randrange(0,1000)
    global turns
    turns = 11
    turn_counter(turns)
    
    print('Range is [0,1000)')
    return secret_number 
    
    
def input_guess(guess):
    # main game logic goes here	    
    
    number = str(guess)
    global turns
    convert = int(number)    
    
    if guess == '':
        print('\n' + 'Please enter a valid number' + '\n' + '\n' + '|New game|' + '\n')
        new_game()
    elif convert == secret_number:
        convert = int(guess)
        print('\n' + 'Guess was ' + str(convert) + '\n')
        print('Correct!' + '\n')
        print('_______________New Game________________')
        range100()
        
    elif convert > secret_number:
        convert = int(guess)
        print('\n' +  'Guess was ' + str(convert) + '\n')
        print('Lower' + '\n')
        global turns
        turns -= 1
        turn_counter(turns)
        
    elif convert < secret_number:
        convert = int(guess)
        print('\n' + 'Guess was ' + str(convert) + '\n')
        print('Higher' + '\n')
     
        turns -= 1
        turn_counter(turns)
    else:
        pass
    
    


new_game()


