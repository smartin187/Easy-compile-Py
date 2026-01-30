# -*- coding: utf-8 -*-

"""
Main module of easyCompile
"""
import ast
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

from easyCompile import easyCompile

# trad ------------------------------------------

trad_001 = {"fr":"Ouvrir un script", "en":"Open a script"}
trad_002 = {"fr":"Easy compile", "en":"Easy compile"}
trad_003 = {"fr":"Script Python", "en":"Python script"}
trad_004 = {"fr":"Easy Compile Py\n\nOuvrer un fichier Python (*.py) pour le compiller...", "en":"Easy Compile Py\n\nOpen a Python file (*.py) for compile it..."}
trad_005 = {"fr":"Paramètres", "en":"Setting"}
trad_006 = {"fr":"Choisiser la langue...", "en":"Selecte language..."}
trad_007 = {"fr":"Valider", "en":"Validate"}


# open the setting file
try:
    file_setting = open("Setting.txt", mode="r", encoding="UTF-8")

    dict_setting = ast.literal_eval(file_setting.read())
    language = dict_setting["language"]

except:
    Path("Setting.txt", encoding="UTF-8").write_text("{'language':'en'}")
    language="en"

main_window = tk.Tk()
main_window.title(trad_002[language])

def open():
    """Open a file and open the window for compile"""
    file = filedialog.askopenfilename(
                                    title=trad_001[language],
                                    filetypes=[(trad_003[language], "*.py")]
        )

    
    if file != "":

        main_window.withdraw()
        easyCompile(main_window, file, language)
        main_window.destroy()
    
text_info = tk.Label(main_window, text=trad_004[language], font=("Arial", 25)).pack()
button_open = tk.Button(main_window, text=trad_001[language], command=open, font=("Arial", 35)).pack(pady=20)

set_language = None

def validate_setting():
    """Write the setting one the file and destroy the setting frame."""
    Path("Setting.txt", encoding="UTF-8").write_text("{'language':'" + set_language.get() + "'}")
    frame_setting.destroy()

def setting():
    """Destroy the setting button and set the setting frame."""
    global set_language
    button_setting.destroy()

    frame_setting.configure(text=trad_005[language])

    text_setting = tk.Label(frame_setting, text=trad_006[language]).pack()

    set_language = ttk.Combobox(frame_setting, values=["en", "fr"], state="readonly")
    set_language.pack()
    set_language.current(0 if language=="en" else 1)


    button_validate = tk.Button(frame_setting, text=trad_007[language], command=validate_setting).pack()

frame_setting = tk.LabelFrame(main_window)
button_setting = tk.Button(frame_setting, text=trad_005[language], command=setting)
button_setting.pack()

frame_setting.pack()

main_window.mainloop()