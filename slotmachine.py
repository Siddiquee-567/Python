import random
import time

class SlotMachine:
    def __init__(self,balance):
        self.balance = balance

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}\n")

    def bet(self,amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return False
        self.balance -= amount
        return True
    def spin(self):
        symbols=['🍒','🔔','🍊','🍋','⭐','💎']
        spin_result=[random.choice(symbols) for _ in range(3)]
        return spin_result
    def calculate_payout(self, spin_result, bet_amount):
        if len(set(spin_result))==1:
            payout=bet_amount*10
            print(f"JACKPOT! You won ${payout:.2f}!")
        elif len(set(spin_result))==2:
            payout=bet_amount*2
            print(f"You won ${payout:.2f}!")
        else:
            payout=0
            print("No match. Better luck next time!")
        self.balance += payout
    def play_round(self):
        self.display_balance()

        while True:
            try:
                bet_amount=float(input("Enter your bet amount: $"))
                if bet_amount <=0:
                    print("Bet amount must be greater than zero!")
                else:
                    break
            except ValueError:
                print("Please enter a valid number!")
        if not self.bet(bet_amount):
            return
        print("Spinning...")
        time.sleep(1)
        spin_result=self.spin()
        print(f"Result: {'|'.join(spin_result)}")
        self.calculate_payout(spin_result, bet_amount)

def main():
    print("Welcome to the slot Machine Game!")
    initial_balance=100.0
    slot_machine = SlotMachine(balance=initial_balance)

    while slot_machine.balance >0:
        slot_machine.play_round()
        play_again=input("Do you want to play again?(yes/no): ").lower()
        if play_again != 'yes':
            break
    print(f"\nGame over! you're leaving with ${slot_machine.balance:.2f}.")

if __name__ =="__main__":
    main()