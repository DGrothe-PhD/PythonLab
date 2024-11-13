import tkinter as tk
import random
from PIL import Image, ImageTk  # Use PIL to handle PNG images

# List of words

word_list = [
    "python", "room", "programming", "developer", "challenge",
    "opportunity", "database", "inspiration", "knowledge", "application",
    "growth", "mindset", "debugging", "exception", "documentation",
    "learning", "improvement", "dictionary", "translation", "requirement",
    "building", "geometry", "button", "correct", "compiler", "desktop",
    "window", "creativity", "feedback", "message", "enhancement"
]

def load_room_image(attempts_left):
    """Load the room image based on the number of attempts left."""
    image_paths = [
        "./images/room0.png",  # 0 attempts left
        "./images/room1.png",
        "./images/room2.png",
        "./images/room3.png",
        "./images/room4.png",
        "./images/room5.png",
        "./images/room6.png"   # Full health, 6 attempts left
    ]
    image_path = image_paths[attempts_left]  # Choose correct image
    return Image.open(image_path)

class RoomGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Room Game")
        self.geometry("850x600")
        self.config(bg="#f5f5f5")

        self.word = random.choice(word_list)
        self.guessed_word = ['_'] * len(self.word)
        self.attempts = 6
        self.guessed_letters = []

        # Room frame for image
        self.room_frame = tk.Frame(self, bg="#f5f5f5")
        self.room_frame.pack(pady=10)

        # Load initial room image
        self.room_image = ImageTk.PhotoImage(load_room_image(self.attempts))
        self.room_label = tk.Label(self.room_frame, image=self.room_image, bg="#f5f5f5")
        self.room_label.pack()

        # Guessed word label with styling
        self.word_label = tk.Label(self, text=" ".join(self.guessed_word),
                                   font=("Courier", 24), bg="#f5f5f5", fg="#007acc")
        self.word_label.pack(pady=20)

        # Message label for displaying feedback
        self.message_label = tk.Label(self, text="", font=("Courier", 16), bg="#f5f5f5", fg="#ff3333")
        self.message_label.pack(pady=10)

        # Frame for the letter buttons
        self.letters_frame = tk.Frame(self, bg="#f5f5f5")
        self.letters_frame.pack(pady=10)

        # Restart button
        self.restart_button = tk.Button(self, text="Restart Game",
         font=("Courier", 14), bg="#ffcc00", fg="#333333", command=self.restart_game)
        self.restart_button.pack(pady=10)

        self.create_letter_buttons()

    def create_letter_buttons(self):
        # Create buttons for each letter A-Z
        for i in range(26):
            letter = chr(65 + i)
            button = tk.Button(self.letters_frame, text=letter,
                               width=4, height=2, font=("Courier", 14), bg="#007acc", fg="white",
                               command=lambda l=letter: self.guess_letter(l.lower()))
            button.grid(row=i // 13, column=i % 13, padx=5, pady=5)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            self.message_label.config(text=f"You already guessed '{letter}'.", fg="#ff3333")
            return

        self.guessed_letters.append(letter)

        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.guessed_word[i] = letter
            self.word_label.config(text=" ".join(self.guessed_word))
            self.message_label.config(text=f"Good guess!", fg="#33cc33")

            if "_" not in self.guessed_word:
                self.message_label.config(text="Congratulations! You won!", fg="#33cc33")
                self.disable_buttons()
        else:
            self.attempts -= 1
            # Update room image on wrong guess
            self.room_image = ImageTk.PhotoImage(load_room_image(self.attempts))
            self.room_label.config(image=self.room_image)
            self.message_label.config(text=f"Wrong guess! {self.attempts} attempts left.", fg="#ff3333")

            if self.attempts == 0:
                self.message_label.config(text=f"Game over! The word was '{self.word}'.", fg="#ff3333")
                self.disable_buttons()

        # Change button style for correct/incorrect guess
        for button in self.letters_frame.winfo_children():
            if button['text'].lower() == letter:
                if letter in self.word:
                    button.config(bg="#33cc33", state="disabled")
                else:
                    button.config(bg="#ff3333", state="disabled")

    def disable_buttons(self):
        # Disable all letter buttons when the game ends
        for button in self.letters_frame.winfo_children():
            button.config(state="disabled")

    def restart_game(self):
        # Reset the game state
        self.word = random.choice(word_list)
        self.guessed_word = ['_'] * len(self.word)
        self.attempts = 6
        self.guessed_letters = []

        # Reset labels and message
        self.room_image = ImageTk.PhotoImage(load_room_image(self.attempts))
        self.room_label.config(image=self.room_image)
        self.word_label.config(text=" ".join(self.guessed_word))
        self.message_label.config(text="")

        # Re-enable all letter buttons and reset their color
        for button in self.letters_frame.winfo_children():
            button.config(state="normal", bg="#007acc")

# Start the game
if __name__ == "__main__":
    app = RoomGame()
    app.mainloop()
