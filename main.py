# Copyright (C) 2023  MF366

import random
from tkinter import messagebox as mb
import customtkinter as ctk
import os
import time
import string
import json
from requests import get
from PIL import Image
import sys

# [!!] VERY BUGGY CODE: DON'T RUN IT!! 

settings = {}

script_path = os.path.abspath(__file__)
script_dir = os.path.abspath(os.path.dirname(script_path))
assets_dir = os.path.join(script_dir, "assets")
sprites_dir = os.path.join(assets_dir, "sprites")
data_dir = os.path.join(script_dir, "data")

lowercase_alphabet = list(string.ascii_lowercase)

english_words = None

try:
    response = get("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt", timeout=5.0)
    
    with open(os.path.join(data_dir, "english_dict.txt"), "w", encoding="utf-8") as dict_eng:
        dict_eng.write(response.text)
        dict_eng.close()
        
        
except Exception:
    mb.showerror("Hangman Remix - Connection Error", "Error found while trying to download the english alpha words from english_words GitHub repository.\nYou must have internet connection!")
    
    if not os.path.exists(os.path.join(data_dir, "english_dict.txt")):
        sys.exit()
    
finally:
    with open(os.path.join(data_dir, "english_dict.txt"), "r", encoding="utf-8") as dict_eng:
        english_words = dict_eng.read().split("\n")
        dict_eng.close()


win = ctk.CTk()
win.title("Hangman Remix")
win._set_appearance_mode("dark")
win.resizable(False, False)

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


not_guessed_letters = lowercase_alphabet.copy()
guesses_left = 6


def remove_guesses(widget: ctk.CTkLabel) -> bool:
    global guesses_left
    
    guesses_left -= 1
    
    if guesses_left <= 0:
        widget.configure(text=f"{settings['nickname']} has no guesses left!")
        return False
    
    widget.configure(text=f"{settings['nickname']} has {guesses_left} guesses left!")
    
    return True

def reset_guess():
    global not_guessed_letters, guesses_left
    
    not_guessed_letters = lowercase_alphabet.copy()
    guesses_left = 6


def guess(word: str, letter: str, widget, xwidget: ctk.CTkLabel, *widgets):
    global guesses_left
    
    _letter = letter.lower()
    _word = word
    
    # [?] How the hell will I do this?
    # [*] Aight, here goes nothing!
    
    # /-/ [!?] I'm still stuck here lol
            
    if _letter not in not_guessed_letters:
        mb.showwarning("Hangman Remix", "You already guessed that letter!")
    
    elif _letter in word:
        not_guessed_letters.remove(_letter)
        
        for let in not_guessed_letters:
            _word = _word.replace(let, "_")
            
        widget.configure(text=_word)
        
        mb.showinfo("Hangman Remix", "Guessed it!")
        
    elif _letter not in word:
        not_guessed_letters.remove(_letter)
        
        mb.showerror("Hangman Remix", "Wrong guess!")
        
        value = remove_guesses(xwidget)
        
        if not value:
            mb.showerror("Hangman Remix", f"DEFEAT! You lost!\nThe word was: {word}")
            phase_1(initial_phase, *widgets)
        
        
def classic_mode(previous, *widgets):
    for widget in widgets:
        widget.destroy()
    
    reset_guess()
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    
    random_word = "a"
    
    while len(random_word) <= 1:
        random_word = random.choice(english_words).lower()
    
    label_2 = ctk.CTkLabel(win, text="HANGMAN - CLASSIC MODE", font=h1)
    label_3 = ctk.CTkLabel(win, text='_' * len(random_word), font=h3)
    label_6 = ctk.CTkLabel(win, text=f"{settings['nickname']} has {guesses_left} guesses left!", font=h4)
    label_8 = ctk.CTkLabel(win, text="Press a key to guess its letter.", font=body)
    
    butt_1 = ctk.CTkButton(win, text="Report a swear word!", font=h4, hover_color="yellow", fg_color="white", text_color="red", command=lambda:
        classic_mode(label_0, label_1, label_2, label_3, butt_1, butt_2, butt_3, label_4, label_5, label_6, label_7, label_8, label_9))
    
    butt_2 = ctk.CTkButton(win, text="Restart", font=h4, hover_color="pink", fg_color="orange", text_color="black", command=lambda:
        classic_mode(label_0, label_1, label_2, label_3, butt_1, butt_2, butt_3, label_4, label_5, label_6, label_7, label_8, label_9))
    
    butt_3 = ctk.CTkButton(win, text="<- Go back", font=h3, hover_color="purple", fg_color="blue", text_color="white", command=lambda:
        previous(label_0, label_1, label_2, label_3, butt_1, butt_2, butt_3, label_4, label_5, label_6, label_7, label_8, label_9))
    
    label_4 = ctk.CTkLabel(win, text="")
    label_5 = ctk.CTkLabel(win, text="")
    label_7 = ctk.CTkLabel(win, text="")
    label_9 = ctk.CTkLabel(win, text="")
    
    for i in lowercase_alphabet:
        win.bind("<KeyPress-{}>".format(i), lambda event, i=i: guess(random_word, i, label_3, label_6, label_0, label_1, label_2, label_3, label_4, label_5, label_6, label_7, label_8, label_9, butt_1, butt_2))

    
    label_0.pack()
    label_2.pack()
    label_1.pack()
    label_4.pack()
    label_3.pack()
    label_5.pack()
    label_6.pack()
    label_7.pack()
    label_8.pack()
    butt_1.pack()
    butt_2.pack()
    butt_3.pack()
    label_9.pack()
    

def phase_1(previous, *widgets):
    for widget in widgets:
        widget.destroy()
        
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    
    label_2 = ctk.CTkLabel(win, text="SELECT A GAMEMODE", font=h1)
    
    label_3 = ctk.CTkLabel(win, text="")
    label_4 = ctk.CTkLabel(win, text="")
    
    butt_1 = ctk.CTkButton(win, text="Classic", font=h3, hover_color="yellow", fg_color="orange", text_color="black", command=lambda:
        classic_mode(phase_1, label_0, label_1, label_2, label_3, butt_2, butt_1, butt_3))
    butt_2 = ctk.CTkButton(win, text="Hardcore", font=h3, hover_color="red", fg_color="pink", text_color="black", command=lambda:
        mb.showerror("Hangman Remix", "Hardcore mode coming soon!"))
    butt_3 = ctk.CTkButton(win, text="<- Go back", font=h3, hover_color="purple", fg_color="blue", text_color="white", command=lambda:
        previous(label_0, label_1, label_2, label_3, butt_2, butt_1, butt_3))
    
    
    label_1.pack()
    label_2.pack()
    label_0.pack()
    butt_1.pack()
    butt_2.pack()
    label_3.pack()
    butt_3.pack()
    label_4.pack()


def on_quit(): 
    x = mb.askyesnocancel("Hangman Remix", "The english dictionary takes up some space.\nWould you like to delete it before exiting?\n(It will be downloaded again the next time you open the game.)")
    
    if not x:
        sys.exit()
        
    elif x:
        os.remove(os.path.join(data_dir, "english_dict.txt"))
        sys.exit()
        
    else:
        pass

def initial_phase(*widgets):
    time.sleep(1.25)
        
    for widget in widgets:
        widget.destroy()
    
    win.geometry(f"{light_logo.width+100}x{light_logo.height+400}")
    
    # Get the screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # Get the height of the taskbar (if it's visible)
    taskbar_height = screen_height - win.winfo_reqheight()

    # Calculate the x and y coordinates to center the window above the taskbar
    x = (screen_width - win.winfo_width()) // 2
    y = (taskbar_height - win.winfo_height()) // 2

    # Set the window's size and position
    win.geometry(f"{light_logo.width+100}x{light_logo.height+400}+{x}+{y}")
    
    logo = ctk.CTkImage(light_logo, dark_logo, (light_logo.width, light_logo.height))
    
    label_0 = ctk.CTkLabel(win, text="")
    label_1 = ctk.CTkLabel(win, text="")
    label_2 = ctk.CTkLabel(win, text="")
        
    logo_packable = ctk.CTkLabel(win, image=logo, width=light_logo.width, height=dark_logo.height, text=" ")
    
    label_0.pack()
    logo_packable.pack()
        
    label_3 = ctk.CTkLabel(win, text="Copyright (C) 2023  MF366", font=bold)
    
    butt_1 = ctk.CTkButton(win, text="-> PLAY", font=h2, fg_color="orange", text_color="black", hover_color="yellow", command=lambda:
        phase_1(initial_phase, label_0, label_1, butt_1, butt_3, label_2, label_3, butt_4, logo_packable))
    butt_3 = ctk.CTkButton(win, text="Settings", font=h3, fg_color="green", text_color="black", hover_color="cyan", command=lambda:
        settings_menu(initial_phase, label_0, label_1, butt_1, butt_3, label_2, butt_4, label_3, logo_packable))
    butt_4 = ctk.CTkButton(win, text="Quit", font=h4, fg_color="red", text_color="black", hover_color="pink", command=on_quit)
    
    label_3.pack()
    label_1.pack()
    butt_1.pack()
    butt_3.pack()
    butt_4.pack()
    label_2.pack()

settings = load_settings()
initial_phase()
    

win.protocol("WM_DELETE_WINDOW", on_quit)

win.mainloop()