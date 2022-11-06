import random, sys

hearts = chr(9829)  
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827) 
# (A list of chr codes is at https://inventwithpython.com/charactermap)
backside= 'backside'



























def getDeck():
    """turn a list of (rank, suit) tuples for all 52 cards"""
    deck = []

    for suit in (hearts, diamonds, spades, clubs):
        for rank in range (2,11):
            deck.append((str(rank), suit)) # Add the numbered cards.
        
        for rank in ('j','q', 'k','a'):
            deck.append((rank, suit)) # Add the face and ace cards.
        
    random.shuffle(deck)
    return deck


def displayCards(cards):
    """Display all the cards in the card list."""
    rows = ['', '', '', '', ''] # The text to display on each row. This

    for i, card in enumerate(cards): 
        rows[0] +=' ___  ' # Print the top line of the card. 

        if card == backside:
            # Print the card's backside
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        
        else:
            #int the card's front:
            rank, suit = card # The card is tuple data structure.

            rows[1] += '|{} | '.format(rank.ljust(2)) 
            rows[2] += '| {} | '.format(suit) 
            rows[3] += '|_{}| '.format(rank.rjust(2,'_')) 
    
    #Print each row on the screen
    for row in rows :
        print(row)


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
    print()
    if showDealerHand: 
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)

    else:
        print('Dealer: ???')
        # Hide the dealer first cards:
        displayCards([backside] + dealerHand[1:])
    
    # Show the player's cards:
    print('Player: ', getHandValue(playerHand))
    displayCards(playerHand)    


def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth 11 or 1 (this funciton picks the most suitable ace value)."""
    value = 0 
    numberOfAces= 0 

    # Add the value for the non-ace cards:
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)

        if rank =='a':
            numberOfAces += 1
        elif rank in ('k','q','j'): # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank) # Numbered cards are woth their number. 

    # Add the values for Aces
    value += numberOfAces # Add 1 per ace cards
    for i in range(numberOfAces):
        #If another 10 can be added iwth busting, do so:
        if value + 10 <= 21:
            value += 10
    
    return value
    


def getMove(playerHand, money):
    """Asks the player for their move, and returns 'H' for hit, 'S' for stand, and 'D'for double down."""
    while True: # Keep asking until player enter a valid value
        #Determine the moves player can make:
        moves = ['(H)it','(S)tand']

        # The player can double down on their first move, which we can tell because the'll hjave exactly two cards:
        if len(playerHand) == 2 and money >0 :
            moves.append('(D)ouble down')

        # Get the player move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player entered a valid value 




def getBet(maxBet): 
    """Ask the player how much they want to bet for this round."""
    while True: # Keep asking until they enter a valid amoutn.
        print('How much do you bet? (1-{}, or quit)'.format(maxBet))
        bet = input('> ').strip()
        if bet.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        
        if not bet.isdecimal():
            continue # If the player didn't enter a number, ask again. 

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Player entered a valid bet.























def main():

    money = 5000
    while True:

        # Chenk if the player have money
        if money <= 0:
            print('You are broke\nThanks for playing.Bye!')
            sys.exit()

        print('Money:',money)
        
        bet= getBet(money)

        # Give the dealer and player two cards from the deck each:

        deck = getDeck()
        dealerHand= [deck.pop(), deck.pop()]
        playerHand= [deck.pop(), deck.pop()]

        #Handle player actions:

        print('Bet: ', bet)
        while True: # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

             #Check if the player has bust: 
            move = getMove(playerHand, money - bet)

            #Handle the player actions:
            if move == 'D':

                additionalBet = getBet(min(bet,(money-bet)))
                bet += additionalBet
                print('Bet increased to {}'.format(bet))
                print('Bet: ', bet)

            if move in ('H','D'):
                # hİT/DOUBLİNG DOWN TAKES ANOTHER CARD.
                newCard = deck.pop() 
                rank, suit = newCard
                print('You drew a {} of {}'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #The player has busted: 
                    continue
            
            if move in ('S','D'):
                # Stand/doubling down stops the player's turn.'
                break
        
        #Handle the dealer's actions:
        if getHandValue(playerHand)  <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)


                if getHandValue(dealerHand) > 21:
                    break # The dealar has busted...
                input('Press Enter to continue...')
                print('\n\n')

            #Show the final hands:
            displayHands(playerHand, dealerHand, True)

            playerValue = getHandValue(playerHand)
            dealerValue = getHandValue(dealerHand)
            # Handle whether teh player won, lost, or tied:
            if dealerValue > 21:
                print(f'Dealer busts! You win ${bet}!.')
                money += bet
            elif playerValue > 21 or( playerValue < dealerValue):
                print('You lost!')
                money -=bet 
            elif playerValue == dealerValue:
                print('It\'s a draw, the bet is returned to you')

            input('Press Enter to continue...')
            print('\n\n')

# Functions 



if __name__ == '__main__':
    main()

