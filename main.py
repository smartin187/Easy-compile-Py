# -*- coding: utf-8 -*-

"""
Main module of easyCompile
"""

import tkinter as tk
from tkinter import filedialog

from easyCompile import easyCompile

# trad ------------------------------------------

trad_001 = {"fr":"Ouvrir un script", "en":"Open a script"}
trad_002 = {"fr":"Easy compile", "en":"Easy compile"}
trad_003 = {"fr":"Script Python", "en":"Python script"}

language="en"

main_window = tk.Tk()
main_window.title(trad_002[language])

def open():
    """Open a file and open the window for compile"""
    file = filedialog.askopenfile(
                                title=trad_001[language],
                                filetypes=[(trad_003[language], "*.py")]
        )
    
    if file != "":    
        main_window.withdraw()
        easyCompile(main_window, file, language)
        main_window.destroy()
    

button_open = tk.Button(main_window, text=trad_001[language], command=open, font=("Arial", 35)).pack()


main_window.mainloop()