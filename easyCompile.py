# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import traceback

import sys
import platform
import subprocess

import webbrowser

import shutil

import os

import pathlib

os_name = sys.platform

def easyCompile(window:object=None, file:str=None, language:str="en", title:str="Easy compile Py"):
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
            "fr":"Choisissez le type de compilation pour Windows :",
            "en":"Select the type of compilation for Windows:"
        }

        t002 = {
            "fr":"Type de compilation",
            "en":"Compiling type"
        }

        t003 = {
            "fr":"Configuration",
            "en":"Configuration"
        }

        t004 = {
            "fr":"Aucun paramètre...",
            "en":"No configuration..."
        }

        t005 = {
            "fr":"Compiler",
            "en":"Compile"
        }

        t006 = {
            "fr":"Compilation en cours,\nVeuillez patienter...",
            "en":"Compilation in progress,\nPlease wait..."
        }

        t007 = {
            "fr":"Ne fermez pas cette fenêtre.",
            "en":"Do not close this window."
        }

        t008 = {
            "fr":"Erreur de compilation",
            "en":"Compilation error"
        }

        t009 = {
            "fr":"Désolé, une erreur est arrivée lors de la compilation...",
            "en":"Sorry, an error occurred during compilation..."
        }

        t010 = {
            "fr":"Détail",
            "en":"Detail"
        }

        t011 = {
            "fr":"Dépendance manquante",
            "en":"Missing dependency"
        }

        t012 = {
            "fr":"Easy Compile a besoin de PyInstaller pour compiler.\nPyInstaller n'est pas installé sur votre ordinateur.",
            "en":"Easy Compile needs PyInstaller to compile.\nPyInstaller is not installed on your computer."
        }

        t013 = {
            "fr":"Installation automatique",
            "en":"Automatic installation"
        }

        t014 = {
            "fr":"L'installation de PyInstaller a été réalisée avec succès.\nVous devez redémarrer Easy Compile pour appliquer l'installation...",
            "en":"The installation of PyInstaller was successful.\nYou must restart Easy Compile to apply the installation..."
        }

        t015 = {
            "fr":"OK",
            "en":"OK"
        }

        t016 = {
            "fr":"Erreur d'installation",
            "en":"Installation error"
        }

        t017 = {
            "fr":"Impossible d'installer PyInstaller automatiquement. Vous pouvez essayer la commande dans un terminal :\npip install pyinstaller\n\nVérifiez aussi que pip est bien installé.\n\nEasy Compile va être fermé...",
            "en":"Unable to automatically install PyInstaller. You can try the command in a terminal:\npip install pyinstaller\n\nAlso check that pip is installed.\n\nEasy Compile will be closed..."
        }

        t018 = {
            "fr":"Télécharger Python",
            "en":"Download Python"
        }

        t019 = {
            "fr":"Fermer",
            "en":"Close"
        }

        t020 = {
            "fr":"Installation manuelle",
            "en":"Manual install"
        }

        t021 = {
            "fr":"Suivez les étapes suivantes pour installer manuellement PyInstaller :",
            "en":"Follow the next steps to manually install PyInstaller:"
        }

        t022 = {
            "fr":"(Étape à suivre si pip n'est pas installé)\nTéléchargez pip, et vérifiez que pip s'installe correctement.",
            "en":"(Step to follow if pip is not installed)\nDownload pip, and make sure pip is installed correctly."
        }

        t023 = {
            "fr":"Dans un terminal, écrivez la commande :\npip install pyinstaller",
            "en":"In a terminal, write the command:\npip install pyinstaller"
        }

        t024 = {
            "fr":"Redémarrez Easy Compile...",
            "en":"Restart Easy Compile..."
        }

        t025 = {
            "fr":"Compilation terminée",
            "en":"Build complete"
        }

        t026 = {
            "fr":"La compilation est terminée.",
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
            "fr":"Enregistrer l'exécutable",
            "en":"Save the executable"
        }

        t030 = {
            "fr":"Informations sur la compilation",
            "en":"Compilation information"
        }

        t031 = {
            "fr": "Vous venez de créer un exécutable Linux.\nN'oubliez pas que pour l'exécuter, le fichier doit être marqué comme 'exécutable'. Pour cela, vous pouvez aller dans les propriétés du fichier, ou exécuter la commande :\nchmod +x nom_du_binaire",
            "en": "You have just created a Linux executable.\nDon't forget that to run it, the file must be marked as 'executable'. To do this, you can go to the file properties or run the command:\nchmod +x binary_name"
        }

        t032 = {
            "fr":"Vertion du package :",
            "en":"Package vertion:"
        }

        t033 = {
            "fr":"Icon de l'éxécutable",
            "en":"Executable icon"
        }

        t034 = {
            "fr":"Paramètre du package Debian",
            "en":"Config of Debian package"
        }

        t035 = {
            "fr":"Configuration du binaire Linux",
            "en":"Binary Linux config"
        }

        t036 = {
            "fr":"Section du package (type d'application) :",
            "en":"Package section (type of application):"
        }

        t037 = {
            "fr":"Architecture :",
            "en":"Architecture:"
        }

        t038 = {
            "fr":"Votre nom :",
            "en":"Your name:"
        }

        t039 = {
            "fr":"Votre adresse email :",
            "en":"Your email adresse:"
        }

        t040 = {
            "fr":"Description :",
            "en":"Description:"
        }

        t041 = {
            "fr":"Nom du package :",
            "en":"Package name:"
        }

        t042 = {
            "fr":"Nom de l'éxécutable\n(nom dans le path) :",
            "en":"Executable name\n(name one path):"
        }
    
    def get_debian_architecture():
        """Return the architecture"""
        machine = platform.machine()
        
        arch_map = {
            'x86_64': 'amd64',
            'aarch64': 'arm64',
            'armv7l': 'armhf',
            'i686': 'i386',
            'i386': 'i386',
        }
        
        return arch_map.get(machine, machine)


    UPTATE_GUIT = 100

    file_info = {
        "control":"""Package: {}
Version: {}
Section: {}
Priority: optional
Architecture: {}
Depends: python3
Maintainer: {} <{}>
Description: {}
"""
    }
    
    def save_compile(extention_compile_save=".exe"):
        """Save the compile (copy the executable)"""

        """# get the executable file :
        
        parent_dir = os.path.dirname(source_file)
        
        executable_file = os.path.join(parent_dir, "dist", file_name + extention_compile_save)
        """
        source_file = os.path.abspath(file)
        file_name = os.path.splitext(os.path.basename(source_file))[0]
        
        new_executable_file = filedialog.asksaveasfilename(
                                                            title=Trad.t029[language],
                                                            filetypes=[(text_type_of_compile["exe" if extention_compile_save==".exe" else "bin"], "*" + extention_compile_save)],
                                                        )
        
        if isinstance(new_executable_file, tuple):
            new_executable_file = new_executable_file[0] if new_executable_file else ""

        if new_executable_file != "":
            shutil.move("./dist/" + file_name + extention_compile_save, new_executable_file)

            if os_name == "linux" and extention_compile_save == "":     # binary Linux
                messagebox.showinfo(
                    title=Trad.t030[language],
                    message=Trad.t031[language]
                )



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
                    subprocess.run(
                            ["pyinstaller", str(file), "--onefile"],
                            #shell=True,
                            text=True,
                        )
                    
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
    
    def configure_frame_Linux(frame):
        """Make the frame of the compile for Linux."""
        def compile_Linux():
            """Lauche the compile for Linux"""
            compile_type = list_compiling.get()

            disabeled_window(window_easy_compile, "disabled")

            frame_message = compile_message()

            compile_ok = False
            deb_ok = False

            window_easy_compile.update()

            try:
                print("file : ", str(file))
                subprocess.run(
                        ["pyinstaller", str(file), "--onefile"],
                        text=True,
                    )
                
                if compile_type == text_type_of_compile["deb"]:     # make a *.deb
                    # delet and make the folder :

                    try: shutil.rmtree("./dist/easycompiledeb")
                    except: pass

                    
                    os.makedirs("./dist/easycompiledeb", exist_ok=True)

                    os.makedirs("./dist/easycompiledeb/usr/bin", exist_ok=True)

                    os.makedirs("./dist/easycompiledeb/DEBIAN", exist_ok=True)

                    # --------

                    source_file = os.path.abspath(file)
                    parent_dir = os.path.dirname(source_file)
                    file_name = os.path.splitext(os.path.basename(source_file))[0]

                    executable_file = os.path.join(parent_dir, "dist", file_name)

                    shutil.move("./dist/" + file_name, "./dist/easycompiledeb/usr/bin/" + entry_name_one_path.get())

                    controle_file = file_info["control"].format(entry_title.get(), entry_vertion.get(), combobox_section.get(), entry_architecture.get(), entry_name.get(), entry_email.get(), entry_description.get())


                    pathlib.Path("./dist/easycompiledeb/DEBIAN/control").write_text(controle_file)

                    deb_build_dir = os.path.abspath("./dist")

                    subprocess.run(
                        ["dpkg-deb", "--build", "easycompiledeb"],
                        cwd=deb_build_dir
                    )

                    shutil.move("./dist/easycompiledeb.deb", "./dist/" + file_name + ".deb")

                    deb_ok = True




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

                button_save = tk.Button(frame_button_compile, text=Trad.t027[language], command=lambda: save_compile(".deb" if deb_ok else "")).grid(column=0, row=0)

                button_cancel = tk.Button(frame_button_compile, text=Trad.t028[language], command=window_easy_compile.destroy).grid(column=1, row=0)


                frame_button_compile.pack()

                window_end_compile.grab_set()
                window_end_compile.wait_window()

            try:
                frame_message.destroy()
            
                disabeled_window(window_easy_compile, "normal")
            except:
                pass

        # -------------------- setting of compile :

        entry_vertion = None
        combobox_section = None
        entry_architecture = None
        entry_name = None
        entry_email = None
        entry_description = None
        entry_title = None
        entry_name_one_path = None
        # ---------


        frame_type_compiling = tk.LabelFrame(frame, text=Trad.t002[language])

        text_info_compiling = tk.Label(frame_type_compiling, text=Trad.t001[language])
        text_info_compiling.pack()

        list_compiling = ttk.Combobox(frame_type_compiling, values=[text_type_of_compile["bin"], text_type_of_compile["deb"]], state="readonly", width=25)
        list_compiling.current(0)
        list_compiling.pack()

        frame_type_compiling.pack()

        frame_config_compile = tk.LabelFrame(frame, text=Trad.t003[language])

        frame_setting_bin = tk.LabelFrame(frame_config_compile, text=Trad.t035[language])
        # frame setting bin if not used now...
        #text_incon = tk.Label(frame_setting_bin, text=Trad.t033[language]).pack()

        frame_setting_bin.grid(column=0, row=0)

        
        frame_config_type = "bin"

        frame_setting_deb_1 = tk.Frame(frame_config_compile)
        frame_setting_deb_1.grid(column=0, row=1)

        def make_frame_setting_deb():
            """Returne the frame setting deb"""

            frame_setting_deb = tk.LabelFrame(frame_setting_deb_1, text=Trad.t034[language])
            frame_setting_deb.grid(column=0, row=0)
            return frame_setting_deb

        frame_setting_deb = make_frame_setting_deb()

        def set_frame_config():
            nonlocal frame_config_type, frame_setting_deb, entry_vertion, combobox_section, entry_architecture, entry_name, entry_email, entry_description, entry_title, entry_name_one_path
            WITH_ENTRY = 15
            # setting for normal compil :
            
            if list_compiling.get() == text_type_of_compile["deb"] and frame_config_type=="bin":
                frame_config_type = "deb"
                # make the config for deb :
                frame_setting_deb.destroy()
                frame_setting_deb = make_frame_setting_deb()

                colum_0 = tk.Frame(frame_setting_deb)
                colum_0.grid(row=0, column=0)

                colum_1 = tk.Frame(frame_setting_deb)
                colum_1.grid(column=1, row=0)

                text_package = tk.Label(colum_0, text=Trad.t032[language]).grid(column=0, row=0)
                entry_vertion = tk.Entry(colum_0, width=WITH_ENTRY)
                entry_vertion.grid(column=1, row=0)
                entry_vertion.insert(0, "1.0")

                text_section = tk.Label(colum_0, text=Trad.t036[language]).grid(column=0, row=1)
                combobox_section = ttk.Combobox(colum_0, values=["admin", "devel", "doc", "editors", "games", "graphics", "libs", "libdevel", "misc", "net", "python", "shells", "sound", "text", "utils", "web"], state="readonly", width=WITH_ENTRY)
                combobox_section.grid(column=1, row=1)
                combobox_section.current(14)

                text_name = tk.Label(colum_0, text=Trad.t038[language]).grid(column=0, row=2)
                entry_name = tk.Entry(colum_0, width=WITH_ENTRY)
                entry_name.grid(column=1, row=2)
                entry_name.insert(0, "User")

                text_email = tk.Label(colum_0, text=Trad.t039[language]).grid(column=0, row=3)
                entry_email = tk.Entry(colum_0, width=WITH_ENTRY)
                entry_email.grid(column=1, row=3)
                entry_email.insert(0, "email@email.com")

                text_architecture = tk.Label(colum_1, text=Trad.t037[language]).grid(column=0, row=0)
                entry_architecture = tk.Entry(colum_1, width=WITH_ENTRY)
                entry_architecture.insert(0, get_debian_architecture())
                entry_architecture["state"]="disabled"
                entry_architecture.grid(column=1, row=0)

                text_title = tk.Label(colum_1, text=Trad.t041[language]).grid(column=0, row=1)
                entry_title = tk.Entry(colum_1, width=WITH_ENTRY)
                entry_title.insert(0, "titleofpackage")
                entry_title.grid(column=1, row=1)

                text_path = tk.Label(colum_1, text=Trad.t042[language]).grid(column=0, row=2)
                entry_name_one_path = tk.Entry(colum_1, width=WITH_ENTRY)
                entry_name_one_path.grid(column=1, row=2)
                entry_name_one_path.insert(0, "myapp")
                

                text_description = tk.Label(colum_1, text=Trad.t040[language]).grid(column=0, row=3)

                entry_description = tk.Entry(colum_1, width=WITH_ENTRY)
                entry_description.grid(column=1, row=3)
                entry_description.insert(0, "Description of package")

                def control_config():
                    """if the debian config is bad, the compilation is disabled."""
                    def vertion_ok(vertion:str):
                        """Return True if the vertion is good, False else"""
                        for char in vertion:
                            if not(char=="." or char=="0" or char=="1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9"):
                                return False
                        
                        return True
                    
                    RED = "#FF0000"
                    NORMAL = "#FFFFFF"
                    try:
                        bad_config = False
                        
                        version = entry_vertion.get()
                        if version == "" or not(vertion_ok(version)):
                            entry_vertion.configure(bg=RED)
                            bad_config = True
                        else: 
                            entry_vertion.configure(bg=NORMAL)

                        name = entry_name.get()
                        if name == "":
                            entry_name.configure(bg=RED)
                            bad_config = True
                        else: 
                            entry_name.configure(bg=NORMAL)
                        
                        email = entry_email.get()
                        if email == "" :
                            entry_email.configure(bg=RED)
                            bad_config = True
                        else: 
                            entry_email.configure(bg=NORMAL)
                        
                        description = entry_description.get()
                        if description == "":
                            entry_description.configure(bg=RED)
                            bad_config = True
                        else: 
                            entry_description.configure(bg=NORMAL)

                        if bad_config: button_compile["state"] = "disabled"
                        else: button_compile["state"] = "normal"


                        frame_setting_deb.after(UPTATE_GUIT, control_config)

                    except: pass
                
                control_config()


            elif list_compiling.get() == text_type_of_compile["bin"] :
                frame_setting_deb.destroy()
                frame_config_type = "bin"


            try: window_easy_compile.after(UPTATE_GUIT, set_frame_config)
            except: pass
        
        set_frame_config()


        frame_config_compile.pack()

        frame_compile = tk.LabelFrame(frame, text=Trad.t005[language])

        button_compile = tk.Button(frame_compile, text=Trad.t005[language], command=compile_Linux, font=("Arial", 25))
        button_compile.pack()

        frame_compile.pack()

    text_type_of_compile = {
                                            # Window :
        "exe":"Windows Executable | *.exe",
                                            # Linux :
        "bin":"Linux Binary Executable | *",
        "deb": "Debian Package | *.deb",
        "appimage": "AppImage Executable | *.AppImage"
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

    configure_frame_Linux(frame_compile_Linux)
    
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
                        ["python", "-m", "pip", "install", "pyinstaller"],
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

    
