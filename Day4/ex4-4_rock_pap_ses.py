# ASCII Arts for rock, paper, and scissors by Veronica Karlsson
#https://devdojo.com/kmhmubin/build-a-python3-rock-paper-scissor-game-using-ascii-art

#Rules:

# rock beats scissors
# scissor beats papper
# papper beats rock
from random import randint

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
pool=[rock, paper, scissors]

pc_choice=pool[randint(0,2)]

player_choice=input('What you like to go with?\n Rock-Paper-Scissors\n> ')

if player_choice.lower().startswith('r'):
    player_choice=rock
elif player_choice.lower().startswith('p'):
    player_choice=paper
elif player_choice.lower().startswith('s'):
    player_choice = scissors
else:
    print('Please enter a valid input...')
    



#Who is the winner???

print(f'The PC choice: \n{pc_choice}')
print(f'The Player choice: \n{player_choice}')

#rock
if pc_choice ==rock and player_choice==scissors:
    print('You lost..\nThe winner is PC!!')

elif pc_choice ==rock and player_choice==paper:
    print('You won!')

elif pc_choice ==rock and player_choice==rock:
    print('Even-steven!!')


#paper
elif pc_choice ==paper and player_choice==scissors:
    print('You won!!')

elif pc_choice ==paper and player_choice==paper:
    print('Even-steven!!')

elif pc_choice ==paper and player_choice==rock:
    print('You lost..')


# scissors
elif pc_choice ==scissors and player_choice==scissors:
    print('Even-steven')

elif pc_choice ==scissors and player_choice==paper:
    print('You lost')

elif pc_choice ==scissors and player_choice==rock:
    print('You lost')
else:
    print('Somenting went wrong')
    


    
