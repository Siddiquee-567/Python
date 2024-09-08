import random

class DicerollGame:
    def __init__(self,starting_balance=1000):
        self.balance=starting_balance
    def place_bet(self, amount):
        if amount>self.balance:
            print(f"Insufficient balance! you have ${self.balance}")
            return False
        return True
    def roll_dice(self):
        return random.randint(1, 6)
    def play(self):
        print("Welcome to the Dice Roll Betting Game!")
        while True:
            print(f"\nYour current balance: ${self.balance}")
            bet=int(input("Enter Your bet amount: "))

            if not self.place_bet(bet):
                continue
            guess=int(input("Guess the dice roll(1-6):"))

            if guess<1 or guess>6:
                print("Invalid guess! Please coose a number between 1 and 6 ")

                continue
            dice_result=self.roll_dice()
            print(f"The dice rolles:{dice_result}")

            if guess==dice_result:
                winnings=bet*6
                self.balance += winnings
                print(f"Congratulations! you won ${winnings}")

            else:
                self.balance -= bet
                print(f"Sorry, you lost ${bet}")

            if self.balance <= 0:
                print("you've run out of money! Gaame over.")
                break
            play_again= input("Do you want to play again? (yes/no): ").lower()

            if play_again != 'yes':
                print("Thanks for playing! Goodbye.")
                break

game=DicerollGame()
game.play()