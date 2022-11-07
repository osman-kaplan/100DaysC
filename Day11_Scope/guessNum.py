import random, os


os.system("clear")
#setting  global variables
HARD_LEVEL= 10
EASY_LEVEL=20
# setting num list and a random number

# num_set= [i for i in range(1,101)]
#random_num= random.choice(num_set)
random_num= random.randint(1,100)



def main():
    from art import logo_numbers
    print(logo_numbers)
    #Welcoming 
    print('Welcome to number Guessing Game.\nI am holding a number in my mind between {} and {}.'.format(1,2))

    #Getting num of lives from the user
    level=input('Would you like "esay" or "hard" level? \n> ')

    if level.lower().startswith('h'):
        lives= HARD_LEVEL
    else:
        lives=EASY_LEVEL

    while lives > 0:

        print('You have {} attempts.'.format(lives))
        lives -= 1

        guess= int(input('Guess a number: >'))
        
        if guess > random_num:
            print('Down')
        elif guess < random_num:
            print('Up')
        elif guess == random_num:
            print('Correct Answer')
            break

        if lives ==0:
            print('You\'ve run out of lives...\nGame Over')
            print(f'The correct answer was {random_num}.')

    # Ask user if he wish to continue to play the game
    should_continue= input('Continue to play the game? Y/N > ')
    
    if should_continue.lower().startswith('y'):
        os.system('clear')
        main()
    else:
        print('The game terminated successfully.\nThanks for playing...')
        

if __name__ == '__main__':
    main()

