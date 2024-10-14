#Black Jack 
import random
#class Card
class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __str__(self):
         return f"{self.value} of {self.suit}"
    
#class Deck
class Deck:
    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self.cards = [Card(suit,value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()
#class Hand
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self,card):
        self.cards.append(card)
    
    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.value in ['Jack','Queen','King']:
                value += 10
            elif card.value == 'Ace':
                aces += 1
            else:
                value += int(card.value)
        
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value +=1
        return value
    
    def __str__(self):
        return ", ". join(str(card) for card in self.cards)


#class BlackJack
class BlackJack:
    def __init__(self, balance = 100):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.balance = balance
        self.bet = 0
        self.player_wins = 0
        self.player_losses = 0
    
    def place_bet(self):
        while True:
            try:
                bet = int(input(f"Your balance: ${self.balance}. Enter your bet:"))
                if 0 < bet <= self.balance:
                    self.bet = bet 
                    self.balance -= bet
                    break
                else:
                    print("Invalid bet amount. Please enter a valid bet!")
            except ValueError:
                print("Invalid input. Please enter a number")
    
    def deal_initial_card(self):
        self.deck.shuffle()
        self.player_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
    
    def player_turn(self):
        while True:
            print(f"\nYour cards: {self.player_hand}")
            print(f"Your hand value: {self.player_hand.get_value()}")
            print(f"Dealer's visible card: {self.dealer_hand.cards[0]}")

            choice = input("Would you like to hit (h) of stand (s)?").lower()
            if choice == 'h':
                self.player_hand.add_card(self.deck.draw())
                if self.player_hand.get_value() > 21:
                    print(f"\nYour cards: {self.player_hand}")
                    print(f"Your hand value: {self.player_hand.get_value()}")
                    print("You went over 21! You lose this round.")
                    self.player_losses += 1
                    return False
                elif choice == 's':
                    return True
                else:
                    print("Invalid choice. Please enter 'h' for hit or 's' to stand.")
    
    def dealer_turn(self):
        print(f"\nDealer's cards: {self.dealer_hand}")
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.draw())
            print(f"Dealer draws a card: {self.dealer_hand.cards[-1]}")
            print(f"Dealer's cards: {self.dealer_hand}")
        
        dealer_value = self.dealer_hand.get_value()
        print(f"\nDealer's hand value: {self.dealer_hand.get_value()}")

        if dealer_value > 21:
            print("Dealer went over 21! You win this round!")
            self.balance += self.bet * 2
            self.player_wins += 1 
            return True
        return False
    
    def compare_hands(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        print(f"\nYour hand value: {player_value}")
        print(f"Dealer's hand value: {dealer_value}")

        if player_value > dealer_value:
            print("You win this round!")
            self.player_wins += 1
            self.balance += self.bet * 2
        elif dealer_value > player_value:
            print("Dealer wins this round!")
            self.player_losses += 1
        else:
            print("It's a tie! you get your bet back.")
            self.balance +=self.bet
    
    def play(self):
        while self.balance > 0:
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.place_bet()
            self.deal_initial_card()
            if self.player_turn():
                if not self.dealer_turn():
                    self.compare_hands()
            print(f"\nYour balance: ${self.balance}")
            print(f"Wins: {self.player_wins} | Losses: {self.player_losses}")
            if input("Play another round? (y/n):").lower != 'y':
                break
        print("Game over! You're out of money.")


def main():
    print("Welcome to BlackJack!")
    game = BlackJack()
    game.play()

main()