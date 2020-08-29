import random

OPTIONS = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(OPTIONS)

def get_human_choice():
    choice_number = int(input('Enter the number of your choice: '))
    return OPTIONS[choice_number - 1]

print ('(1) Rock\n(2) Paper\n(3) Scissors')
human_choice = get_human_choice()
print(f'You chose {human_choice}')
computer_choice = get_computer_choice()
print (f'The computer chose {computer_choice}')
if human_choice == 'rock':
    if computer_choice == 'paper':
        print('Sorry, paper beat rock')
    elif computer_choice == 'scissors':
        print('Yes, rock beat scissors!')
    else:
        print('Draw!')
if human_choice == 'paper':
    if computer_choice == 'scissors':
        print('Sorry, scissors beat paper')
    elif computer_choice == 'rock':
        print('Yes, paper beat rock!')
    else:
        print('Draw!')
if human_choice == 'scissors':
    if computer_choice == 'rock':
        print('Sorry, rock beat scissors')
    elif computer_choice == 'paper':
        print('Yes, scissors beat paper!')
    else:
        print('Draw!')
