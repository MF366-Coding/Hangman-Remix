# Copyright (C) 2023  MF366

import random
import nltk
import customtkinter as ctk
import os
import time
from PIL import Image

win = ctk.CTk()
win.title("Hangman Remix")
win._set_appearance_mode("dark")
win.resizable(False, False)

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
assets_dir = os.path.join(script_dir, "assets")
sprites_dir = os.path.join(assets_dir, "sprites")

light_logo = Image.open(os.path.join(sprites_dir, "LIGHT_LOGO.png"))
dark_logo = Image.open(os.path.join(sprites_dir, "DARK_LOGO.png"))

h1 = ctk.CTkFont("JetBrains Mono", 21, "bold")
h2 = ctk.CTkFont("JetBrains Mono", 18, "bold")
h3 = ctk.CTkFont("JetBrains Mono", 16, "bold")
h4 = ctk.CTkFont("JetBrains Mono", 14, "bold", "italic")

body = ctk.CTkFont("JetBrains Mono", 15)
italic = ctk.CTkFont("JetBrains Mono", 15, slant="italic")
bold = ctk.CTkFont("JetBrains Mono", 15, "bold")
bold_italic = ctk.CTkFont("JetBrains Mono", 15, "bold", "italic")

small_body = ctk.CTkFont("JetBrains Mono", 13)
small_italic = ctk.CTkFont("JetBrains Mono", 13, slant="italic")
small_bold = ctk.CTkFont("JetBrains Mono", 13, "bold")
small_bold_italic = ctk.CTkFont("JetBrains Mono", 13, "bold", "italic")

def change_appearance():
    '''
    # button: ctk.CTkButton = None
    if button != None:
        current_colors = [button._fg_color,
                        button._text_color,
                        button._text,
                        button._hover_color]
        
        preset1 = ["black", "white", "Dark Mode", "grey"]
        preset2 = ["white", "black", "Light Mode", "grey"]
        
        if current_colors[2] == "Light Mode":
            preset = preset1
            
        else:
            preset = preset2
        
        button.configure(text=preset[2], fg_color=preset[0], text_color=preset[1], hover_color=preset[3])
    '''
    
    current_mode = win._get_appearance_mode()
    
    if current_mode.strip().lower() == "dark":
        win._set_appearance_mode("light")
        time.sleep(1.5)
        return
    
    win._set_appearance_mode("dark")    
    time.sleep(1.5)

'''
def phase_1(previous_menu: function, home_menu: function, *widgets):
'''

def settings_menu(previous, *widgets):
    for widget in widgets:
        widget.destroy()
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    
    label_3 = ctk.CTkLabel(win, text="SETTINGS", font=h1)
    
    butt_1 = ctk.CTkButton(win, text="Apply", font=h3, fg_color="green", text_color="black", hover_color="dark green", command=lambda:
        previous(label_0, label_1, label_3, butt_1))
    
    label_0.pack()
    label_3.pack()
    label_1.pack()
    butt_1.pack()
    
def initial_phase(*widgets):
    for widget in widgets:
        widget.destroy()
    
    win.geometry(f"{light_logo.width+100}x{light_logo.height+200}")
    
    logo = ctk.CTkImage(light_logo, dark_logo, (light_logo.width, light_logo.height))
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    label_2 = ctk.CTkLabel(win, text="")
        
    logo_packable = ctk.CTkLabel(win, image=logo, width=light_logo.width, height=dark_logo.height, text=" ")
    
    label_0.pack()
    logo_packable.pack()
        
    label_3 = ctk.CTkLabel(win, text="Copyright (C) 2023  MF366", font=bold)
    
    butt_1 = ctk.CTkButton(win, text="-> PLAY", font=h2, fg_color="orange", text_color="black", hover_color="yellow")
    butt_2 = ctk.CTkButton(win, text="Credits", font=h3, fg_color="dark blue", text_color="white", hover_color="purple")
    butt_3 = ctk.CTkButton(win, text="Settings", font=h3, fg_color="green", text_color="black", hover_color="cyan", command=lambda:
        settings_menu(initial_phase, logo_packable, label_0, label_1, label_2, label_3, butt_1, butt_2, butt_3))
    '''
    butt_4 = ctk.CTkButton(win, text="Light Mode", font=h3, fg_color="white", text_color="black", hover_color="grey", command=lambda:
        change_appearance(butt_4))
    '''
    
    label_3.pack()
    label_1.pack()
    butt_1.pack()
    butt_2.pack()
    butt_3.pack()
    '''
    butt_4.pack()
    '''
    label_2.pack()

initial_phase()

'''
# chatGPT break in here!

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