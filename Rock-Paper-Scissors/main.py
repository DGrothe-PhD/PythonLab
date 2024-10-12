#rock- scissors- paper Game
#RockPaperScissors
import random


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock","scissors","paper"]
        self.win_conditions={
            "rock":"scissors",
            "scissors":"paper",
            "paper":"rock"
        }
    
    #get computer choice
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    #get user choice
    def get_player_choice(self):
        while True:
            choice = input("Choose rock, scissors, or paper:").lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please try again.")
    
    #determine winner
    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tie"
        elif self.win_conditions[player_choice] == computer_choice:
            return "Player"
        else:
            return "Computer"
    
    #play Game
    def play_game(self):
        while True:
            player_choice = self.get_player_choice()
            computer_choice = self.get_computer_choice()

            print(f"\nYou chose:{player_choice}")
            print(f"The computer chose:{computer_choice}")

            result = self.determine_winner(player_choice,computer_choice)
            if result == "Tie":
                print("It's a tie! Let's play again.")
            elif result =="Player":
                print("Congratulations! You win!")
                break
            else:
                print("Sorry, the computer won. the game is over.")
                break
            



def main():
    print("Welcome to Rock-Paper-Scissors!")
    #RockPaperScissors Class
    game = RockPaperScissors()
    game.play_game()

main()