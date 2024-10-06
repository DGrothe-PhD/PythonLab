# Memory Game

Projekt 1: Memory

Skapa en version av spelet Memory.
·         Datorn väljer ett antal slumpmässiga siffror eller bokstäver (beroende på svårighetsgrad) och visar dem i en viss ordning.
·         Sedan visar datorn samma siffror eller bokstäver igen, men denna gång blandat.
·         Spelaren ska gissa i vilken ordning siffrorna eller bokstäverna visades första gången.
·         Spelet fortsätter tills spelaren har gissat rätt ordning.

## MemorySpel.py

**Python version**: 3.11.9

### MemoryGame Class

The `MemoryGame` class contains the following attributes and methods:

#### Attributes:
1. **difficulty**: the difficulty level easy or hard.
2. **sequence**: random sequence.
3. **shuffled_sequence**: a copy of sequence.

#### Methods:
1. **generate_sequence**: Generate a sequence base on difficulty level.
2. **display_sequence**: Display the sequence.
3. **clear_screen**: clear the terminal after display the sequence.
4. **get_player_guess**: ask user to insert his own guessed sequence.
4. **check_guess**: Checks if user input is matched the sequence.
4. **play**: to play the game.

## How to Run:

1. Open a terminal.
2. Change the directory to the `Memory` folder:
  ```bash
   cd ./Memory
  ```
3. in the terminal run the command 
   ```bash
    python3 MemorySpel.py
  ```