# Copyright (C) 2023  MF366

import random
import nltk
import customtkinter as ctk
import os
from PIL import Image

win = ctk.CTk(fg_color="#292929")

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
assets_dir = os.path.join(script_dir, "assets")
sprites_dir = os.path.join(assets_dir, "sprites")

light_logo = Image.open(os.path.join(sprites_dir, "LIGHT_LOGO.png"))
dark_logo = Image.open(os.path.join(sprites_dir, "DARK_LOGO.png"))

logo = ctk.CTkImage(light_logo, dark_logo, (light_logo.width, light_logo.height))
logo_packable = ctk.CTkLabel(win, image=logo, width=light_logo.width, height=dark_logo.height, text=" ")
logo_packable.grid(column=1, row=1)

# this is just an idea bro

'''
# Download the NLTK words corpus if you haven't already
nltk.download('words')

# Get the list of English words from NLTK
english_words = nltk.corpus.words.words()

# Select a random word from the list
random_word = random.choice(english_words)

# List of words for the game
word_list = ["python", "hangman", "programming", "game", "code"]

# Choose a random word from the list
random_word = random.choice(word_list)

# Initialize variables
word_display = ["_"] * len(random_word)
incorrect_guesses = 0
max_attempts = 6  # You can adjust the number of allowed incorrect guesses

# Main game loop
while True:
    # Display the current state of the word
    print(" ".join(word_display))

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the guess is in the word
    if guess in random_word:
        # Update the word display with the correctly guessed letter
        for i in range(len(random_word)):
            if random_word[i] == guess:
                word_display[i] = guess
    else:
        print("Incorrect guess.")
        incorrect_guesses += 1

    # Check if the player has won or lost
    if "".join(word_display) == random_word:
        print("Congratulations! You guessed the word:", random_word)
        break
    elif incorrect_guesses >= max_attempts:
        print("Sorry, you've run out of attempts. The word was:", random_word)
        break
'''
win.mainloop()