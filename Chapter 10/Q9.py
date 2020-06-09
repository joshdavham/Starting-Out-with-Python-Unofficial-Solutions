#Question 9

def main():
    deck = create_deck()


    while len(deck) != 0:

        hand_Value1 = 0
        hand_Value2 = 0
        print("\nNEW GAME", \
              "\n--------")


        #We are now in a game
        while True:

            print("\nPlayer 1 was dealt a: ", end="")
            valueReturned1 = deal_cards(deck,hand_Value1)

            print("Player 2 was dealt a: ", end="")
            valueReturned2 = deal_cards(deck,hand_Value2)

            if valueReturned1 == 0 or valueReturned2 == 0:
                #Then no value was returned from the cards meaning that the deck is now empty
                break
            else:
                hand_Value1 = valueReturned1
                hand_Value2 = valueReturned2

                print("Player 1 has a hand value of:", hand_Value1, \
                      "\nPlayer 2 has a hand value of:", hand_Value2)

                if hand_Value1 >= 21 or hand_Value2 >= 21:
                    if hand_Value1 > hand_Value2:
                        print("\nPlayer 2 wins!")
                        break
                    elif hand_Value1 < hand_Value2:
                        print("\nPlayer 1 wins!")
                        break
                    else:#There was a time
                        print("\nThere was a tie!")
                        break


    print("\n\nThe deck ran out of cards, Game over!", \
          "\n-------------------------------------")



def create_deck():
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    return deck

def deal_cards(deck, hand_value):
    if len(deck) > 0:
        card, value = deck.popitem()
        print(card)
        if value == 1 and hand_value + 11 <= 21:
            value = 11

        return hand_value + value

    else:#The deck is empty
        return 0


main()
