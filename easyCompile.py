# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import sys

import subprocess

import webbrowser

import shutil

import os

os_name = sys.platform

def easyCompile(window=None, file=None, language="en", title="Easy compile Py"):
    """Open an window for compile Python with GUI.
    Argument :
    * window : the Tkinter window
    * file : the file of scrip python
    * title : the title of windows. Defaut is "Easy compile Py".
    """
    class Trad:
        """The traduction for easyCompile.
        Example : {"fr":"aa", "en":"aa"}
        """
        def t999(nuber):
            """Special trad"""
            nuber = str(nuber)
            return {
                    "fr":f"Étape {nuber}",
                    "en":f"Step {nuber}"
                }

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

        t006 = {
            "fr":"Compilation en cours,\nVeuiller patienter...",
            "en":"Compiling in progress,\nPlease wait..."
        }

        t007 = {
            "fr":"Ne fermer pas cette fênetre.",
            "en":"Do not close this window."
        }

        t008 = {
            "fr":"Erreur de compilation",
            "en":"Compilation error"
        }

        t009 = {
            "fr":"Désolé, une erreur est arrivé lors de la compilation...",
            "en":"Sorry, an error occurred during compilation..."
        }

        t010 = {
            "fr":"Détail",
            "en":"Detail"
        }

        t011 = {
            "fr":"Dépandance manquante",
            "en":"Missing depandance"
        }

        t012 = {
            "fr":"Easy Compile a besouin de Pyinstaller pour compiler.\nPyinstaller n'est pas installer sur votre ordinateur.",
            "en":"Easy Compile needs Pyinstaller to compile.\nPyinstaller is not installed on your computer."
        }

        t013 = {
            "fr":"Intalation automatique",
            "en":"Automatic installation"
        }

        t014 = {
            "fr":"L'instalation de pyinstaller a étais réaliser avec succé.\n Vous devez redémarer Easy Compile pour appliquer l'instalation...",
            "en":"The installation of pyinstaller was successful.\n You must restart Easy Compile to apply the installation..."
        }

        t015 = {
            "fr":"OK",
            "en":"OK"
        }

        t016 = {
            "fr":"Erreur d'instalation",
            "en":"Installation error"
        }

        t017 = {
            "fr":"Impossible d'instaler pyinstaller automatiquement. Vous pouvez esseyer la commande dans un terminal :\npip install pyinstaller\n\nVérifier aussi que pip est bien installer.\n\nEasy Compile va être fermer...",
            "en":"Unable to automatically install pyinstaller. You can try the command in a terminal:\npip install pyinstaller\n\nAlso check that pip is installed.\n\nEasy Compile will be closed..."
        }

        t018 = {
            "fr":"Téléchager Python",
            "en":"Download Python"
        }

        t019 = {
            "fr":"Fermer",
            "en":"Close"
        }

        t020 = {
            "fr":"Instalation manuelle",
            "en":"Manuel install"
        }

        t021 = {
            "fr":"Suiver les étapes suivante pour installer manuellement Pyinstaller :",
            "en":"Follow the next steps to manually install Pyinstaller:"
        }

        t022 = {
            "fr":"(Étape à suivre si pip n'est pas installer)\nTélécharger pip, et vérifier que pip s'installe correctement.",
            "en":"(Step to follow if pip is not installed)\nDownload pip, and make sure pip is installed correctly."
        }

        t023 = {
            "fr":"Dans un terminal, écriver la commande :\npip install pyinstaller",
            "en":"In a terminal, write the command:\npip install pyinstaller"
        }

        t024 = {
            "fr":"Redémarer Easy Compile...",
            "en":"Restart Easy Compile..."
        }

        t025 = {
            "fr":"Comliation terminer",
            "en":"Build complete"
        }

        t026 = {
            "fr":"La compilation est terminer.",
            "en":"The compilation is complete."
        }

        t027 = {
            "fr":"Enregistrer sous",
            "en":"Save as"
        }
        
        t028 = {
            "fr":"Annuler",
            "en":"Cancel"
        }

        t029 = {
            "fr":"Enregistrer l'éxécutable",
            "en":"Save the executable"
        }
    
    def save_compile():
        """Save the compile (copy the executable)"""
        # get the executable file :
        source_file = os.path.abspath(file)
        parent_dir = os.path.dirname(source_file)
        file_name = os.path.splitext(os.path.basename(source_file))[0]
        executable_file = os.path.join(parent_dir, "dist", file_name + ".exe")

        new_executable_file = filedialog.asksaveasfilename(
                                                            title=Trad.t029[language],
                                                            filetypes=[(text_type_of_compile["exe"], "*.exe")],
                                                            defaultextension="*.exe"
                                                        )
        
        if new_executable_file != "":
            shutil.move(executable_file, new_executable_file)

            window_easy_compile.destroy()

    def open_python_on_webbrowser():
        webbrowser.open("https://www.python.org/downloads/")
    
    def window_error(window, title, text, detail):
        """Open a window error."""
        window_e = tk.Toplevel(window)
        window_e.title(title)
        
        text_error = tk.Label(window_e, text=text).pack()

        frame_detail = tk.LabelFrame(window_e, text=Trad.t010[language])

        text_detail = tk.Label(frame_detail, text=detail).pack()

        frame_detail.pack()

        window_e.grab_set()
        window_e.wait_window()
    
    def compile_message():
        """Set a message one the window of easyCompile for anounce the compile.
        return the frame of message"""

        back_ground = "#FFFFFF"

        frame_message = tk.LabelFrame(window_easy_compile, bg=back_ground)

        text_info = tk.Label(frame_message, text=Trad.t006[language], bg=back_ground).pack()
        text_warning = tk.Label(frame_message, text=Trad.t007[language], bg=back_ground, fg="#FF0000", font=("Arial", 8, "bold")).pack()

        height=60
        width=200

        frame_message.place(
                            x=main_frame.winfo_width() // 2 - width // 2,
                            y=main_frame.winfo_height() // 2 - height // 2,
                            height=height,
                            width=width
                        )

        return frame_message

    def disabeled_window(window, state):
        """Disable all windget on the window"""
        for windget in window.winfo_children():
            try:
                if state=="normal" and isinstance(windget, ttk.Combobox):
                    windget["state"] = "readonly"
                else:
                    windget["state"] = state
            except:
                pass

            try:
                disabeled_window(windget, state)
            except:
                pass

    def configure_frame_windows(frame):
        """Make the frame of the compile for window."""
        def compile_windows():
            """Lauche the compile for windows"""
            compile_type = list_compiling.get()

            if compile_type == text_type_of_compile["exe"]:
                disabeled_window(window_easy_compile, "disabled")

                frame_message = compile_message()

                compile_ok = False

                window_easy_compile.update()

                try:
                    # old :
                    #subprocess.run(
                    #        ["pyinstaller", str(file)],
                    #        shell=True,
                    #        text=True,
                    #    )
                    PyInstaller.__main__.run([
                            str(file),
                            "--onefile",
                        ])
                    
                    window_easy_compile.update()
                    
                    compile_ok = True
                
                except Exception as e:
                    window_error(window_easy_compile, Trad.t008[language], Trad.t009[language], str(e))

                    window_easy_compile.update()
                    compile_ok = False
                
                if compile_ok :
                    window_end_compile = tk.Toplevel(window_easy_compile)
                    window_end_compile.title(Trad.t025[language])

                    text_info = tk.Label(window_end_compile, text=Trad.t026[language]).pack()

                    frame_button_compile = tk.Frame(window_end_compile)

                    button_save = tk.Button(frame_button_compile, text=Trad.t027[language], command=save_compile).grid(column=0, row=0)

                    button_cancel = tk.Button(frame_button_compile, text=Trad.t028[language], command=window_easy_compile.destroy).grid(column=1, row=0)


                    frame_button_compile.pack()

                    window_end_compile.grab_set()
                    window_end_compile.wait_window()

                try:
                    frame_message.destroy()
                
                    disabeled_window(window_easy_compile, "normal")
                except:
                    pass

        frame_type_compiling = tk.LabelFrame(frame, text=Trad.t002[language])

        text_info_compiling = tk.Label(frame_type_compiling, text=Trad.t001[language])
        text_info_compiling.pack()

        list_compiling = ttk.Combobox(frame_type_compiling, values=[text_type_of_compile["exe"]], state="readonly", width=25)
        list_compiling.current(0)
        list_compiling.pack()

        frame_type_compiling.pack()

        frame_config_compile = tk.LabelFrame(frame, text=Trad.t003[language])

        texte_config = tk.Label(frame_config_compile, text=Trad.t004[language])
        texte_config.pack()

        frame_config_compile.pack()

        frame_compile = tk.LabelFrame(frame, text=Trad.t005[language])

        button_compile = tk.Button(frame_compile, text=Trad.t005[language], command=compile_windows, font=("Arial", 25))
        button_compile.pack()

        frame_compile.pack()

    text_type_of_compile = {
        "exe":"Windows Executable | *.exe"
    }

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

    # controle de Pyinstaller :
    try:
        import PyInstaller.__main__
    except ImportError:
        def automatic_installe():
            """Try to install PyInstaller."""
            def error_install(détail):
                """Open an error window for an error of automatic install."""
                window_error_install = tk.Toplevel(window_no_pyinstaller)
                window_error_install.title(Trad.t016[language])

                text_error_install = tk.Label(window_error_install, text=Trad.t017[language]).pack()
                text_detail = tk.Label(window_error_install, text=Trad.t010[language] + détail).pack()

                frame_button_error = tk.Frame(window_error_install)

                #button_python = tk.Button(frame_button_error, text=Trad.t018[language], command=open_python_on_webbrowser).grid(column=0, row=0)
                button_close = tk.Button(frame_button_error, text=Trad.t019[language], command=window_easy_compile.destroy).grid(column=1, row=0)

                frame_button_error.pack()

                window_error_install.grab_set()
                window_error_install.wait_window()

            try:
                result = subprocess.run(
                        [sys.executable, "-m", "pip", "install", "pyinstaller"],        # remplacer executable par 'python' ?
                        capture_output=True,
                        text=True,
                        timeout=60
                    )
                if result.returncode == 0:
                    window_pyinstaller_install = tk.Toplevel(window_no_pyinstaller)

                    texte_info = tk.Label(window_pyinstaller_install, text=Trad.t014[language]).pack()

                    button_ok = tk.Button(window_pyinstaller_install, text=Trad.t015[language], command=window_easy_compile.destroy).pack()

                    window_pyinstaller_install.protocol("WM_DELETE_WINDOW", window_easy_compile.destroy)

                    window_pyinstaller_install.grab_set()
                    window_pyinstaller_install.wait_window()
                else:
                    error_install("returncode" + str(result.returncode))
            except Exception as e:
                error_install(str(e))

        def manual_install():
            """Open an window for an manual install."""
            window_no_pyinstaller.destroy()

            window_manual_install = tk.Toplevel(window_easy_compile)
            window_manual_install.title(Trad.t020[language])

            text_install_1 = tk.Label(window_manual_install, text=Trad.t021[language]).pack()

            frame_install_1 = tk.LabelFrame(window_manual_install, text=Trad.t999(1)[language])

            text_install_2 = tk.Label(frame_install_1, text=Trad.t022[language]).pack()

            #button_install_python = tk.Button(frame_install_1, text=Trad.t018[language], command=open_python_on_webbrowser).pack()

            frame_install_1.pack()

            frame_install_2 = tk.LabelFrame(window_manual_install, text=Trad.t999(2)[language])

            text_install_3 = tk.Label(frame_install_2, text=Trad.t023[language]).pack()

            frame_install_2.pack()

            frame_install_3 = tk.LabelFrame(window_manual_install, text=Trad.t999(3)[language])

            text_install_4 = tk.Label(frame_install_3, text=Trad.t024[language]).pack()

            frame_install_3.pack()

            button_close = tk.Button(window_manual_install, text=Trad.t019[language], command=window_manual_install.destroy).pack()

            window_manual_install.grab_set()
            window_manual_install.wait_window()

            window_easy_compile.destroy()


        window_no_pyinstaller = tk.Toplevel(window_easy_compile)
        window_no_pyinstaller.title(Trad.t011[language])

        text_no_pyinstaller = tk.Label(window_no_pyinstaller, text=Trad.t012[language]).pack()

        frame_button = tk.Frame(window_no_pyinstaller)

        button_automatic_installe = tk.Button(frame_button, text=Trad.t013[language], command=automatic_installe).grid(column=0, row=0)

        button_manual_intall = tk.Button(frame_button, text=Trad.t020[language], command=manual_install).grid(column=1, row=0)

        button_close = tk.Button(frame_button, text=Trad.t019[language], command=window_easy_compile.destroy).grid(column=2, row=0)

        frame_button.pack()

        window_no_pyinstaller.protocol("WM_DELETE_WINDOW", window_easy_compile.destroy)

        window_no_pyinstaller.grab_set()
        window_no_pyinstaller.wait_window()

    try:
        window_easy_compile.grab_set()
        window_easy_compile.wait_window()
    except:
        pass

    
