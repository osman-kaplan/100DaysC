import random 
import os

os.system('clear')

def main():
    def deal_card():
        """Returns a list of two cards"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card= random.choice(cards)
        return card

    def get_Cards():
        global user_cards
        global computer_cards
        user_cards = []
        computer_cards = []



        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

    # Calculate the score of total cards for each
    def calculate_score(cards):
        """Accept a list of cards and return the sum of the card values"""

        # if (100 in cards) and (11 in cards) and len(cards)==2:
        if sum(cards) ==21 and len(cards) ==2:
            return 0 
        #Hint 8: İnside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 adn replace it with a 1. 
        # method 1: 
        # if sum(cards) >21 and 11 in cards:
        #     cards.append(-10)
        # Method 2: 
        if sum(cards) >21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    # 13 Create a fuction callled compare() and pass in the user_score and computer_score.

    def compare(player_score, computer_score):
        
        if player_score == computer_score :
            return 'Its a draw'
        
        elif computer_score ==0:
            return 'Player lost!'
        
        elif player_score == 0:
            return 'Player won!'
        elif player_score > 21:
            return 'Player lost!'
        elif computer_score > 21 :
            return 'Computer lost'
        
        else:
            if player_score > computer_score:
                return 'Player won!'
            else:
                return 'Player lost!'



    get_Cards()
    #Variables
    is_game_over= False
    user_score= calculate_score(user_cards)
    computer_score= calculate_score(computer_cards)






    while not is_game_over:
        print(f'Pc cards: \n#{computer_cards[1]}; \nScore: \n{computer_score}')
        print(f'User cards: \n{user_cards}; \nScore: \n{user_score}')

        if user_score ==0 or computer_score ==0 or user_score > 21:
            is_game_over= True
        else:
            response= input('Draw another card? (Y/N)> ')
            if response.lower().startswith('y'):
                user_cards.append(deal_card())
                user_score= calculate_score(user_cards)
            else:
                is_game_over = True

    # Hint 12 ; once dealr hand is done, get the pc hand 

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'Computer last hand: \n{computer_cards}, \nits score: \n    {computer_score}')
    print(f'User last hand: \n{user_cards}, \nits score: \n    {user_score}')


    print(compare(user_score, computer_score))

# hin14:  Ask the user if they want to restart the game. If they answer yes thenclear the console and start a new game of blackjack and show the logo from art.py

    may_continue= input('You wanna continue palying balckjack? Y/N > ')

    if may_continue.lower().startswith('y'):
        os.system('clear')
        main()


if __name__ == '__main__':
    main()






















