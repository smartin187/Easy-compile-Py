# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk
from tkinter import ttk
import sys

os_name = sys.platform

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

    compile_notebok = ttk.Notebook(main_frame)
    compile_notebok.pack()

    # Window :
    frame_compile_Window = tk.Frame(compile_notebok)
    compile_notebok.add(frame_compile_Window, text="Window", state="normal" if os_name == "win32" else "disabled")
    
    # Linux :
    frame_compile_Linux = tk.Frame(compile_notebok)
    compile_notebok.add(frame_compile_Linux, text="Linux", state="normal" if os_name == "linux" else "disabled")
    

    window_easy_compile.grab_set()
    window_easy_compile.wait_window()

    
