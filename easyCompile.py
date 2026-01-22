# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk

def easyCompile(window=None, file=None, language="en", title="Easy compile Py"):
    """Open an window for compile Python with GUI.
    Argument :
    * window : the Tkinter window
    * file : the file of scrip python
    * title : the title of windows. Defaut is "Easy compile Py".
    """

    if window is None:
        raise Exception("No window was given.")
    elif file is None:
        raise Exception("No file was given.")
    
    window_easy_compile = tk.Toplevel(window)
    window_easy_compile.title(title)

    main_frame = tk.Frame(window_easy_compile)
    main_frame.place(x=0, y=0)

    
