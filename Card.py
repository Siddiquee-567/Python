import random
def deal_card():
    """Return a random card from the deck."""
    cards=[2,3,4,5,6,7,8,9,10,10,10,11] 
    return random.choice(cards)
def calculate_score(hand):
    """Calculate the score of the hand."""
    score=sum(hand)
    if score>21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score=sum(hand)
    return score
def compare_scores(player_score, dealer_score):
    """Compare player and dealer scores to determine the winner,"""
    if player_score >21:
        return "you went over. you lose!"
    elif dealer_score >21:
        return "Dealer went over. you win!"
    elif player_score==dealer_score:
        return "It's a draw!"
    elif player_score==21:
        return "Blackjack! you win!"
    elif player_score>dealer_score:
        return "you win!"
    else:
        return "you lose!"
def play_game():
    print("welcome to the 21 Game!")

    player_hand =[deal_card(),deal_card()]
    dealer_hand =[deal_card(),deal_card()]

    game_over=False

    while not game_over:
        player_score=calculate_score(player_hand)
        dealer_score=calculate_score(dealer_hand)

        print(f"your cards:{player_hand}, Current score:{player_score}")
        print(f"Dealer's first card:{dealer_hand[0]}")

        if player_score==21 or dealer_score==21 or player_score>21:
            game_over=True
        else:
            should_continue=input("Type 'y' to get another card, type 'n' to pass:")

            if should_continue=='y':
                player_hand.append(deal_card())
            else:
                game_over= True
    while dealer_score !=21 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score=calculate_score(dealer_hand)
    
    print(f"Your final hand: {player_hand}, final score:{player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))

play_game()
