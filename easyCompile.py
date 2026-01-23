# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk
from tkinter import ttk

import sys

os_name = sys.platform

class Trad:
    """The traduction for easyCompile.
    Example : {"fr":"aa", "en":"aa"}
    """

    t001 = {
        "fr":"Choisiser le type de compilation pour Window :",
        "en":"Select the type of compiling for Window:"
    }

    t002 = {
        "fr":"Type de compilation",
        "en":"Compiling type"
    }

    t003 = {
        "fr":"Configuration",
        "en":"Configure"
    }

    t004 = {
        "fr":"Aucun paramètre...",
        "en":"No configure..."
    }

    t005 = {
        "fr":"Compiler",
        "en":"Compile"
    }


def easyCompile(window=None, file=None, language="en", title="Easy compile Py"):
    """Open an window for compile Python with GUI.
    Argument :
    * window : the Tkinter window
    * file : the file of scrip python
    * title : the title of windows. Defaut is "Easy compile Py".
    """
    def configure_frame_windows(frame):
        """Make the frame of the compile for window."""
        frame_type_compiling = tk.LabelFrame(frame, text=Trad.t002[language])

        text_info_compiling = tk.Label(frame_type_compiling, text=Trad.t001[language])
        text_info_compiling.pack()

        text_compile = tk.StringVar()
        text_compile.set("Windows application | *.exe")

        list_compiling = ttk.Combobox(frame_type_compiling, values=["Windows application | *.exe"], state="readonly", textvariable=text_compile, width=25)     # meilleur texte + mettre par défaut le texte
        list_compiling.pack()

        frame_type_compiling.pack()

        frame_config_compile = tk.LabelFrame(frame, text=Trad.t003[language])

        texte_config = tk.Label(frame_config_compile, text=Trad.t004[language])
        texte_config.pack()

        frame_config_compile.pack()

        frame_compile = tk.LabelFrame(frame, text=Trad.t005[language])

        button_compile = tk.Button(frame_compile, text=Trad.t005[language], font=("Arial", 25))
        button_compile.pack()

        frame_compile.pack()


    if window is None:
        raise Exception("No window was given.")
    elif file is None:
        raise Exception("No file was given.")
        
    window_easy_compile = tk.Toplevel(window)
    window_easy_compile.title(title)

    main_frame = tk.Frame(window_easy_compile)
    main_frame.place(x=0, y=0)

    compile_notebok = ttk.Notebook(main_frame)
    compile_notebok.pack()

    # Window :
    frame_compile_Window = tk.Frame(compile_notebok)
    compile_notebok.add(frame_compile_Window, text="Window", state="normal" if os_name == "win32" else "disabled")

    configure_frame_windows(frame_compile_Window)
    
    # Linux :
    frame_compile_Linux = tk.Frame(compile_notebok)
    compile_notebok.add(frame_compile_Linux, text="Linux", state="normal" if os_name == "linux" else "disabled")
    
    window_easy_compile.geometry("300x300")

    window_easy_compile.grab_set()
    window_easy_compile.wait_window()

    
