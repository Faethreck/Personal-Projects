import random 
#||||||||||||||||||||||^Libraries^||||||||||||||||||||||||||
rock = 0
spock = 1
paper = 2
lizard = 3
scissors = 4

rpsls_list = ['rock','spock','paper','lizard','scissors']
numbers_list = ['0','1','2','3','4']

player_choice = input('Choose your move!')

#|||||||||||||||||||^Global Variables^|||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    
def name_to_number(name):
    #this function converts the name to number    
        if name in rpsls_list:
            def returning_value(name):
            #this function returns the input value      
                
                if name == 'rock':
                    return '0'
                elif name == 'spock':
                    return '1'
                elif name == 'paper':
                    return '2'
                elif name == 'lizard':
                    return '3'
                elif name == 'scissors':
                    return '4'
            return returning_value(name) 
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||
def number_to_name(number):
#this function converts the choice from number to name    
    if number in numbers_list:
        def returning_value(number):
        #this function returns the input value    
                         
            if number == '0':
                return 'rock'
            elif number == '1':
                return 'spock'
            elif number == '2':
                return 'paper'
            elif number == '3':
                return 'lizard'
            elif number ==  '4':
                return 'scissors'
        return str(returning_value(number))

def comp_choice():
#this function runs the randomizer for the computers choice
    result = str(random.randrange(0,5))
    return str(result)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
comp_response = comp_choice()
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def rpsls(player_choice):
#this function contains the other needed functions    
    rpsls_list = ['rock','spock','paper','lizard','scissors']
    numbers_list = ['0','1','2','3','4']
    #|||||||||||||||||^Local Variables^||||||||||||||||||||||||||||
    if player_choice in numbers_list:
        return number_to_name(player_choice)
        calculator(player_choice,comp_response)
    elif player_choice in rpsls_list:
        return player_choice
        player_choice = name_to_number(player_choice)
        calculator(player_choice,comp_response)
        
        
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def calculator(player_choice,comp_response):
    rpsls_list = ['rock','spock','paper','lizard','scissors']
    numbers_list = ['0','1','2','3','4']
    if player_choice in numbers_list:
        result = (int(player_choice) - int(comp_response)) % 5
        if result == 0:
            return "Player and Computer tie!"
        elif result < 3:
            return "Player Wins!"
        else:
            return "Computer Wins!"
    elif player_choice in rpsls_list:
        
        result = (int(name_to_number(player_choice)) - int(comp_response)) % 5
        if result == 0:
            return "Player and Computer tie!"
        elif result < 3:
            return "Player Wins!"
        else:
            return "Computer Wins!"
        
if player_choice in rpsls_list:
    runner = name_to_number(player_choice)
    calculator(runner,comp_response)
elif player_choice in numbers_list:
    calculator(player_choice,comp_response)
        
def comp_number(comp_response):
    if comp_response in numbers_list:
        return number_to_name(comp_response)
    elif comp_response in rpsls_list:
        return comp_response
       


#|||||||||||||||||||||||game runner|||||||||||||||||||||||||||||||

print('Player chooses ' + rpsls(player_choice) + '\n')
print('Computer chooses ' + comp_number(comp_response) + '\n')
print(calculator(player_choice,comp_response))