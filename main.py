# Copyright (C) 2023  MF366

import random
import nltk
from tkinter import messagebox as mb
import customtkinter as ctk
import os
import time
import json
from PIL import Image

settings = {}

win = ctk.CTk()
win.title("Hangman Remix")
win._set_appearance_mode("dark")
win.resizable(False, False)

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
assets_dir = os.path.join(script_dir, "assets")
sprites_dir = os.path.join(assets_dir, "sprites")
data_dir = os.path.join(script_dir, "data")

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

"""
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
"""

'''
def phase_1(previous_menu, home_menu, *widgets):
'''

def load_settings(check_only: bool = False) -> dict:
    """
    load_settings loads the settings of your game

    Args:
        check_only (bool, optional): Actually loads the settings if False. Defaults to False.

    Returns:
        dict: the settings!
    """
    global settings
    
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
        
    settings_file = os.path.join(data_dir, "settings.json")
    
    if not os.path.exists(settings_file):
        with open(settings_file, "w", encoding="utf-8") as f:
            json.dump({
                "nickname": "VeryCoolHangmanPlayer"
            }, f)
            f.close()
    
    if not check_only:    
        with open(settings_file, "r", encoding="utf-8") as f:
            settings = json.load(f)
            f.close()
            
        return settings

def save_settings():
    """
    save_settings saves the settings to the JSON file
    """
    load_settings(check_only=True)
    
    settings_file = os.path.join(data_dir, "settings.json")
    
    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(settings, f)
        f.close()

def apply_changes(previous, *widgets, **kwargs) -> None:
    """
    apply_changes is a bridge between save_settings and the settings menu

    It also connects other menus related to the settings menu.

    Args:
        previous (function): the previous menu opened
    """
    global settings
    
    if kwargs["nickname"] != settings["nickname"]:
        settings["nickname"] = kwargs["nickname"]
    
    save_settings()
    
    previous(*widgets)
    
    return

def settings_menu(previous, *widgets):
    global settings
    
    for widget in widgets:
        widget.destroy()
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    
    label_2 = ctk.CTkLabel(win, text="Nickname: ", font=body)
    label_3 = ctk.CTkLabel(win, text="SETTINGS", font=h1)
    
    a = ctk.StringVar(win, value=settings["nickname"])
    
    entry_1 = ctk.CTkEntry(win, fg_color="white", text_color="black", placeholder_text_color="grey", placeholder_text="Insert your new nickname here.", textvariable=a, font=body)
        
    butt_1 = ctk.CTkButton(win, text="Apply", font=h3, fg_color="green", text_color="black", hover_color="dark green", command=lambda:
        apply_changes(previous, label_0,
                    label_1,
                    label_3,
                    entry_1,
                    butt_1,
                    label_2, 
                    nickname=a.get(), itself=settings_menu))
    
    label_0.pack()
    label_3.pack()
    label_2.pack()
    entry_1.pack()
    label_1.pack()
    butt_1.pack()

def classic_mode(previous, *widgets):
    for widget in widgets:
        widget.destroy()
        
    return


def phase_1(previous, *widgets):
    for widget in widgets:
        widget.destroy()
        
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    
    label_2 = ctk.CTkLabel(win, text="SELECT A GAMEMODE", font=h1)
    
    label_3 = ctk.CTkLabel(win, text="")
    
    butt_1 = ctk.CTkButton(win, text="Classic", font=h3, hover_color="yellow", fg_color="orange", text_color="black", command=lambda:
        classic_mode(phase_1, label_0, label_1, label_2, label_3, butt_2, butt_1))
    butt_2 = ctk.CTkButton(win, text="Hardcore", font=h3, hover_color="red", fg_color="pink", text_color="black")
    
    label_1.pack()
    label_2.pack()
    label_0.pack()
    butt_1.pack()
    butt_2.pack()
    label_3.pack()

def initial_phase(*widgets):
    time.sleep(1.25)
        
    for widget in widgets:
        widget.destroy()
    
    win.geometry(f"{light_logo.width+100}x{light_logo.height+200}")
    
    # Get the screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # Get the height of the taskbar (if it's visible)
    taskbar_height = screen_height - win.winfo_reqheight()

    # Calculate the x and y coordinates to center the window above the taskbar
    x = (screen_width - win.winfo_width()) // 2
    y = (taskbar_height - win.winfo_height()) // 2

    # Set the window's size and position
    win.geometry(f"{light_logo.width+100}x{light_logo.height+200}+{x}+{y}")
    
    logo = ctk.CTkImage(light_logo, dark_logo, (light_logo.width, light_logo.height))
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    label_2 = ctk.CTkLabel(win, text="")
        
    logo_packable = ctk.CTkLabel(win, image=logo, width=light_logo.width, height=dark_logo.height, text=" ")
    
    label_0.pack()
    logo_packable.pack()
        
    label_3 = ctk.CTkLabel(win, text="Copyright (C) 2023  MF366", font=bold)
    
    butt_1 = ctk.CTkButton(win, text="-> PLAY", font=h2, fg_color="orange", text_color="black", hover_color="yellow", command=lambda:
        phase_1(initial_phase, label_0, label_1, butt_1, butt_2, butt_3, label_2, label_3, logo_packable))
    butt_2 = ctk.CTkButton(win, text="Credits", font=h3, fg_color="dark blue", text_color="white", hover_color="purple")
    butt_3 = ctk.CTkButton(win, text="Settings", font=h3, fg_color="green", text_color="black", hover_color="cyan", command=lambda:
        settings_menu(initial_phase, label_0, label_1, butt_1, butt_2, butt_3, label_2, label_3, logo_packable))
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

settings = load_settings()
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