#hangman Spel
#loadWordsFromFile
import random


def loadWordsFromFile ():
    with open('./Words.txt','r') as file:
        words = file.read().splitlines()
    return words

#generateWord
def generateWord():
    #read the file in Words 
    words = loadWordsFromFile()
    if words:
        return random.choice(words)
    else:
        return None

#Hangman Class
class Hangman:
    def __init__(self,word,maxAttempt = 6):
        self.wordToGuess = word
        self.maxAttempt = maxAttempt
        self.attemptLeft = maxAttempt
        self.guessedLetters =[]
        self.guessedWord = ['_'] * len(self.wordToGuess)
    
    def guess(self,letter):
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            return 'Ange bara en bokstav!'
        if letter in self.guessedLetters:
            return f"Du har redan gissat bokstaven '{letter}', försök igen!"
        
        self.guessedLetters.append(letter)

        if letter in self.wordToGuess:
            #find the index of the letter
            for index, char in enumerate(self.wordToGuess):
                if char == letter:
                    self.guessedWord[index] = letter
            return f"Bra, Bokstaven '{letter}' finns i ordet."
        else:
            self.attemptLeft -=1
            return f"Fel! Bokvtaven '{letter}' finns det inte i ordet, Försök kvar: {self.attemptLeft}"
        
    def wordGuessed (self):
        return ''.join(self.guessedWord) == self.wordToGuess
    
    def gameIsOver (self):
        return self.attemptLeft == 0 or self.wordGuessed()
    
    def display(self):
        return ''.join(self.guessedWord)   


#main
def main ():
    #get a word from Words.txt
    word = generateWord()
    # Hangman Class
    game = Hangman(word)

    print("Välkommen till Hangman spel!")
    print(f"Ordet består av {len(game.wordToGuess)} bokstäver, bokstäver: {game.display()}")

    while not game.gameIsOver():
        guess = input("Gissa en bokstäv:").lower()
        print(game.guess(guess))
        print(game.display())

    if game.gameIsOver():
        print(f"Tyvärr, du har inga försök kvar. Ordet var '{game.wordToGuess}'")
    if game.wordGuessed():
        print(f"Grattis! Du gissade order '{game.wordToGuess}'")



main()