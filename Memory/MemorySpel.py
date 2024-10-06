#Memory Game
import os
import random
import time


class MemoryGame:
    def __init__(self,difficulty='easy'):
        self.difficulty=difficulty
        self.sequence = []
        self.shuffled_sequence= []
        self.generate_sequence()

    #generate_sequence 
    ## to generate random number sequence based on difficulty
    def generate_sequence(self):
        if self.difficulty == 'easy':
            self.sequence = [str(random.randint(0, 9)) for _ in range(5)]
        else:
            self.sequence = [chr(random.randint(65 , 90)) for _ in range(7)]
        
        self.shuffled_sequence = self.sequence.copy()
        random.shuffle(self.shuffled_sequence)
    
    #display sequence for 2 sec beffore clear the screen 
    def display_sequence(self,sequence,delay = 1):
        print("\nRemember this sequence:")
        for item in sequence:
            print(item, end= ' ', flush=True)
            time.sleep(delay)
        print()
        time.sleep(2)
        self.clear_screen()
    
    #clear_screen 
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #player guess 
    def get_player_guess (self):
        print("Here  is the shuffled sequence:")
        print(' '.join(self.shuffled_sequence))
        guess = input("Enter the original order (separate with spaces): ").split()
        return guess
    
    #to check the guess
    def check_guess(self,guess):
        return guess == self.sequence
    
    #play method 
    def play(self):
        print(f"Welcome to Memory! Difficulty level: {self.difficulty}")
        self.display_sequence(self.sequence)

        attempts = 0
        isEnded = False
        while isEnded == False:
            attempts +=1
            guess = self.get_player_guess()
            if self.check_guess(guess):
                print(f"\nCongratulations! You guessed correctly after {attempts} attempts.")
                isEnded = True
            else:
                print("Unfortunately, that was wrong. Try agian!")
#end class 
        

def main():
    #select difficulty level
    difficulty = input("Select difficulty level (easy/hard): ").lower()
    # chech if invalid input
    while difficulty not in ['easy','hard']:
        difficulty = input("Invalid choice. Select 'easy' or 'hard': ").lower()
    
    #MemoryGame Class
    game = MemoryGame(difficulty)
    game.play()

main()
#Done