# Hangman Game

Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence, and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses. Originally a paper-and-pencil game, there are now electronic versions.


Projekt 1: Hangman

Skapa en version av det klassiska spelet Hangman.

·         Datorn väljer ett slumpmässigt ord från en fördefinierad lista av ord.

·         Spelet visar hur många bokstäver ordet består av, men inte vilka bokstäver som är rätt.

·         Spelaren ska gissa en bokstav i taget, och datorn ger feedback om bokstaven finns i ordet eller inte.

·         Spelet fortsätter tills spelaren har gissat hela ordet eller har gjort tillräckligt många felaktiga gissningar.

## hangmanSpel.py

**Python version**: 3.11.9

### Hangman Class

The `Hangman` class contains the following attributes and methods:

#### Attributes:
1. **wordToGuess**: A random word chosen from the `Words.txt` file.
2. **maxAttempt**: The maximum number of attempts in the game (6 attempts).
3. **attemptLeft**: The remaining attempts left in the game.
4. **guessedLetters**: The guessed letters so far.
5. **guessedWord**: An array (list) of `_` with the same length as the `wordToGuess`, representing the unguessed word.

#### Methods:
1. **guess**: Checks if the `wordToGuess` contains the guessed letter.
2. **display**: Prints the current state of the `guessedWord`.
3. **gameIsOver**: Checks if the game is over by determining if the word has been guessed or if the `attemptLeft` is 0.
4. **wordGuessed**: Checks if the entire word has been correctly guessed.

### Functions:
1. **generateWord**: Returns a random word from a list of words.
2. **loadWordsFromFile**: Reads the `Words.txt` file and loads the words into a list.

## How to Run:

1. Open a terminal.
2. Change the directory to the `Hangman` folder:
  ```bash
   cd ./Hangman
  ```
3. in the terminal run the command 
   ```bash
    python3 HnagmanSpel.py
  ```