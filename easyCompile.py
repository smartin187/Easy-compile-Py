# -*- coding: utf-8 -*-

"""
This module have the fonction "easyCompile", for easy compile Python.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from urllib import request

import sys
import platform
import subprocess
from PIL import Image
import webbrowser
import traceback
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

        t043 = {
            "fr":"Appimage",
            "en":"Appimage"
        }

        t044 = {
            "fr":"Section de l'appimage :",
            "en":"Appimage section:"
        }

        t045 = {
            "fr":"Appimagetool indisponible",
            "en":"Appimagetool unavailable"
        }

        t046 = {
            "fr":"Pour générer des appimage, Easy Compile Py doit avoir Appimagetool.\nVous devez le télécharger, le mettre dans le même dossier que Easy Compile Py, et le renommer en 'appimagetool.appimage'.",
            "en":"To generate appimage, Easy Compile Py needs Appimagetool.\nYou must download it, put it in the same folder as Easy Compile Py, and rename it to 'appimagetool.appimage'."
        }

        t047 = {
            "fr":"Shouaiter vous installer Appimagetool ?",
            "en":"Do you want to install Appimagetool?"
        }

        t048 = {
            "fr":"Installer Appimagetool",
            "en":"Install Appimagetool"
        }

        t049 = {
            "fr":"Shouaiter vous installer Appimagetool automatiquement ?\nSi l'instalation automatique échoue, veiller faire l'installation manuelle...",
            "en":"Do you want to install Appimagetool automatically?\nIf the automatic installation fails, please do the manual installation..."
        }

        t050 = {
            "fr":"Avec l'instalation manuelle, vous aurait un guide pour l'instalation...",
            "en":"With the manual installation, you will have a guide for the installation..."
        }

        t051 = {
            "fr":"Instalation manuelle",
            "en":"Manual install"
        }

        t052 = {
            "fr":"Etape ",
            "en":"Step "
        }

        t053 = {
            "fr":"Télécharger AppimageTool depuis GitHub (au format appimage).\nPenser à téléchager la bonne architecture processeur.",
            "en":"Download AppimageTool from GitHub (in appimage format).\nMake sure to download the correct processor architecture."
        }

        t054 = {
            "fr":"Téléchargement sur GitHub",
            "en":"Download on GitHub"
        }

        t055 = {
            "fr":"Vérifier que AppimageTool soit bien éxécutable.\nVous pouvez faire la commande :\nchmod +x appimagetool.appimage",
            "en":"Make sure that AppimageTool is executable.\nYou can do the command:\nchmod +x appimagetool.appimage"
        }

        t056 = {
            "fr":"Copier AppimageTool dans le même dossier que EasyCompilePy.\nPuis renomer le extactement 'appimagetool.appimage'.",
            "en":"Copy AppimageTool in the same folder as EasyCompilePy.\nThen rename it exactly 'appimagetool.appimage'."
        }

        t057 = {
            "fr":"Fermer",
            "en":"Close"
        }

        t058 = {
            "fr":"Redémarer EasyCompilePy",
            "en":"Restart EasyCompilePy"
        }

        t059 = {
            "fr":"Désolé, une erreur est survenu lors de l'instalation d'AppimageTool.\nVous pouvez esseyer d'installer manuellement, en suivant le guide.",
            "en":"Sorry, an error occurred during the installation of AppimageTool.\nYou can try to install manually, following the guide."
        }

        t060 = {
            "fr":"Détail : ",
            "en":"Detail: "
        }

        t061 = {
            "fr":"Erreur d'instalation",
            "en":"Instaltion error"
        }

        t062 = {
            "fr":"Icon de l'AppImage :",
            "en":"AppImage icon:"
        }

        t063 = {
            "fr":"Définire l'icon",
            "en":"Set icon"
        }

        t064 = {
            "fr":"Importer un icon",
            "en":"Import an icon"
        }

        t065 = {
            "fr":"Choisiser un icon en PNG.",
            "en":"Choos an PNG icon."
        }

        t066 = {
            "fr":"Veiller ne pas déplacer/renomer l'image séléctionner...",
            "en":"Please do not move/rename the selected image..."
        }

        t067 = {
            "fr":"Compilation avec Wine",
            "en":"Compilation with Wine"
        }

        t068 = {
            "fr":"Vous ête sous Linux. Easy Compile Py permet de compiller vers Window en utilisant Wine.",
            "en":"You are on Linux. Easy Compile Py allows you to compile for Windows using Wine."
        }

        t069 = {
            "fr":"Wine est une application libre pour exécuté des programme Windows sur Linux.\nLa compilation fonctionne dans la majorité des cas, mais il peut y avoir des erreurs...\nTester toujour l'éxécutable Windows...\nLa compilation peut durée longtemps (même pour de petit script).",
            "en":"Wine is a free application to run Windows programs on Linux.\nThe compilation works in most cases, but there may be errors...\nAlways test the Windows executable...\nThe compilation can take a long time (even for small scripts)."
        }

        t070 = {
            "fr":"Wine n'est pas installer",
            "en":"Wine is not install"
        }

        t071 = {
            "fr":"Wine n'est pas installer ou a rencontrer une erreur.",
            "en":"Wine is not installed or has encountered an error."
        }

        t072 = {
            "fr":"Voulez vous installer Wine ?",
            "en":"Do you want to install Wine?"
        }

        t073 = {
            "fr":"Installation de Wine",
            "en":"Wine installation"
        }

        t074 = {
            "fr":"Shouaiter vous installer Wine automatiquement ?",
            "en":"Do you want to install Wine automatically?"
        }

        t075 = {
            "fr":"Erreur d'instalation",
            "en":"Install error"
        }

        t076 = {
            "fr":"Désolé, une erreur est arrivé lors de l'installation de Wine.\nVeuiller faire l'installation automatiquement.\nSi votre distribution Linux n'est pas un dérivé de Debian, faite l'instalation manuelle...",
            "en":"Sorry, an error occurred during the installation of Wine.\nPlease do the automatic installation.\nIf your Linux distribution is not a Debian derivative, do the manual installation..."
        }

        t077 = {
            "fr":"L'instalation de Wine est terminer.\nRedémarer Easy Compile Py pour l'utiliser...",
            "en":"The installation of Wine is complete.\nRestart Easy Compile Py to use it..."
        }

        t078 = {
            "fr":"Guide d'instalation de Wine",
            "en":"Wine installation guide"
        }

        t079 = {
            "fr":"Suiver le guide pour installer Wine :",
            "en":"Follow the guide to install Wine:"
        }

        t080 = {
            "fr":"Ecriver dans votre terminale la commande :\napt install wine\n\nSi vous n'êtes pas sur Debian ou un dérivé, vous devez adapté la commande...\n\nAttention : si vous avez un processeur ARM, il est recommander d'installer Box86...",
            "en":"Write in your terminal the command:\napt install wine\n\nIf you are not on Debian or a derivative, you must adapt the command...\n\nWarning: if you have an ARM processor, it is recommended to install Box86..."
        }

        t081 = {
            "fr":"Ecriver dans votre terminale la commande :\nwinecfg\nUne fênetre s'ouvre pour paramétrer Wine.\nIl pourra vous être demander d'installer Mono, accepter l'installation...\nNoter que la première vois que vous faite cette commande, cela peut prendre du temps...",
            "en":"Write in your terminal the command:\nwinecfg\nA window opens to configure Wine.\nYou may be asked to install Mono, accept the installation...\nNote that the first time you run this command, it may take some time..."
        }

        t082 = {
            "fr":"Redémarer Easy Compile Py.",
            "en":"Restart Easy Compile Py."
        }

        t083 = {
            "fr":"Etape : {}",
            "en":"Step: {}"
        }

        t084 = {
            "fr":"Quitter",
            "en":"Close"
        }

        t085 = {
            "fr":"Erreur WSL",
            "en":"WSL error"
        }

        t086 = {
            "fr":"WSL n'est pas installer...",
            "en":"WSL is not install..."
        }

        t087 = {
            "fr":"Veuiller installer WSL puis redémarer Easy Compile Py...",
            "en":"Please install WSL then restart Easy Compile Py..."
        }

        t088 = {
            "fr":"Pyinstaller dans WSL n'est pas installer.",
            "en":"Pyinstaller in WSL is not install."
        }

        t089 = {
            "fr":"Voulez vous installer Pyinstaller ?",
            "en":"Do you want to install Pyinstaller ?"
        }

        t090 = {
            "fr":"Installation de Pyinstaller",
            "en":"Pyinstaller setup"
        }

        t091 = {
            "fr":"Shouaiter vous installer Pyinstaller automatiquement ?",
            "en":"Do you want to install Pyinstaller automatically ?"
        }

        t092 = {
            "fr":"Si vous shouaiter installer Pyinstaller manuellement, vous aurez un guide pour le faire...",
            "en":"If you want to install Pyinstaller manually, you will have a guide to do it..."
        }

        t093 = {
            "fr":"Erreur d'installation",
            "en":"Instal error"
        }

        t094 = {
            "fr":"Une erreur est arrivé lors de l'installation de Pyinstaller. Faites l'installation manuelle...",
            "en":"An error occurred when the installation of Pyinstaller. Do the manual installation..."
        }

        t095 = {
            "fr":"Détail : ",
            "en":"Detail: "
        }

        t096 = {
            "fr":"Installation manuelle",
            "en":"Manual installation"
        }

        t097 = {
            "fr":"Ouvrer WSL et taper la commande :\npip install pyinstaller\n\nRedémarer Easy Compile Py.",
            "en":"Open WSL and write the command:\npip install pyinstaller\n\nRestart Easy Compile Py."
        }

        t098 = {
            "fr":"Fermer",
            "en":"Close"
        }

        t099 = {
            "fr":"Effectuer toutes ces action dans WSL :",
            "en":"Perform all these action in WSL:"
        }

        t100 = {
            "fr":"Copier AppimageTool dans votre dossier personnel :\n/home/votrenom/  ou  ~/\n\nEt renomer le fichier en exactement 'appimagetool.appimage'.",
            "en":"Copy AppimageTool in your home folder:\n/home/yourname/  or  ~/\n\nAnd rename the file exactly 'appimagetool.appimage'."
        }

    def get_debian_architecture():
        """Return the architecture"""
        machine = platform.machine()
        
        arch_map = {
            'x86_64': 'amd64',
            'AMD64': 'amd64',
            'aarch64': 'arm64',
            'armv7l': 'armhf',
            'i686': 'i386',
            'i386': 'i386',
        }
        
        return arch_map.get(machine, machine)

    def get_appimage_architecture():
        """Return the architecture name used in appimagetool download URLs."""
        machine = platform.machine()

        arch_map = {
            'x86_64': 'x86_64',
            'AMD64': 'x86_64',
            'amd64': 'x86_64',
            'x64': 'x86_64',

            'aarch64': 'aarch64',
            'arm64': 'aarch64',
            'ARM64': 'aarch64',

            'armv7l': 'armhf',
            'armhf': 'armhf',

            'i686': 'i686',
            'i386': 'i686',
        }

        return arch_map.get(machine, machine)

    def grab_set_and_wait_window(window):
        """Set wait_window() and grab_set() for the Tk/Toplevel."""
        window.grab_set()
        window.wait_window()

    CHAR_LIST = {
        "az":["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"],
        "09":["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    }


    UPTATE_GUIT = 100

    APPIMAGETOOL_URL = "https://github.com/AppImage/appimagetool/releases/download/1.9.1/appimagetool-{}.AppImage"


    file_info = {
        "control":"""Package: {}
Version: {}
Section: {}
Priority: optional
Architecture: {}
Depends: python3
Maintainer: {} <{}>
Description: {}
""",
        "desktop":"""[Desktop Entry]
Name=appname
Exec={}
Icon={}
Type=Application
Categories={};""",
    "AppRun":'''#!/bin/bash

exec "$APPDIR/usr/bin/{}" "$@"'''
    }
    
    def save_compile(extention_compile_save=".exe"):
        """Save the compile (copy the executable)"""
        source_file = os.path.abspath(file)
        file_name = os.path.splitext(os.path.basename(source_file))[0]
        
        new_executable_file = filedialog.asksaveasfilename(
                                                            title=Trad.t029[language],
                                                            filetypes=[(text_type_of_compile["exe" if extention_compile_save==".exe" else "bin" if extention_compile_save=="" else "deb" if extention_compile_save==".deb" else "appimage"], "*" + extention_compile_save)],
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

        grab_set_and_wait_window(window_e)
    
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

            if os_name == "win32":

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
                                check=True,
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

                        grab_set_and_wait_window(window_end_compile)

                    try:
                        frame_message.destroy()
                    
                        disabeled_window(window_easy_compile, "normal")
                    except:
                        pass


            elif os_name == "linux":
                if compile_type == text_type_of_compile["exe"]:
                    messagebox.showinfo(title=Trad.t067[language], message=Trad.t068[language], detail=Trad.t069[language])
                    try:
                        result = subprocess.run(["wine", "--version"], capture_output=True, text=True)
                    except:
                        class result_error:
                            returncode = 1
                        result = result_error()

                    if result.returncode != 0:
                        install_wine = messagebox.askyesno(title=Trad.t070[language], message=Trad.t071[language], detail=Trad.t072[language])

                        if install_wine:
                            automatique_install = messagebox.askyesno(title=Trad.t073[language], message=Trad.t074[language])

                            if automatique_install:
                                try:
                                    subprocess.run(
                                        ["sudo", "apt", "install", "wine"],
                                        capture_output=True,
                                        text=True,
                                        check=True,
                                    )
                                    subprocess.run(
                                        ["winecfg"],
                                        capture_output=True,
                                        text=True,
                                        check=True,
                                    )
                                    
                                except Exception as e:
                                    messagebox.showerror(title=Trad.t075[language], message=Trad.t076[language], detail=str(e))
                                    window_easy_compile.destroy()
                                    return
                                else:
                                    messagebox.showinfo(title=Trad.t073[language], message=Trad.t077[language])
                                    window_easy_compile.destroy()
                                    return
                            else:
                                window_manual_install_wine = tk.Toplevel()
                                window_manual_install_wine.title(Trad.t078[language])

                                text_info = tk.Label(window_manual_install_wine, text=Trad.t079[language]).pack()

                                step = [
                                    Trad.t080[language],
                                    Trad.t081[language],
                                    Trad.t082[language]
                                ]

                                

                                for i in range(1, 4):
                                    frame_tmp = tk.LabelFrame(window_manual_install_wine, text=Trad.t083[language].format(str(i)))
                                    text_tmp = tk.Label(frame_tmp, text=step[i-1]).pack()
                                    frame_tmp.pack()

                                button_close_guide = tk.Button(window_manual_install_wine, text=Trad.t084[language], command=window_manual_install_wine.destroy).pack()

                                grab_set_and_wait_window(window_manual_install_wine)

                                window_easy_compile.destroy()
                                return


                        else:
                            window_easy_compile.destroy()
                            return

                    
                        


                    disabeled_window(window_easy_compile, "disabled")

                    frame_message = compile_message()

                    compile_ok = False

                    window_easy_compile.update()

                    try:
                        subprocess.run(
                                ["wine", "pyinstaller", str(file), "--onefile"],
                                text=True,
                                check=True,
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

                        grab_set_and_wait_window(window_end_compile)

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

            if os_name == "linux":

                frame_message = compile_message()

                compile_ok = False
                deb_ok = False
                appimage_ok = False

                window_easy_compile.update()

                try:
                    subprocess.run(
                            ["pyinstaller", str(file), "--onefile"],
                            text=True,
                            check=True,
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
                            cwd=deb_build_dir,
                            check=True,
                        )

                        shutil.move("./dist/easycompiledeb.deb", "./dist/" + file_name + ".deb")

                        deb_ok = True

                    elif compile_type == text_type_of_compile["appimage"]:       # make a appimage
                        
                        if not pathlib.Path("appimagetool.appimage").is_file():
                            install_appimagetool = messagebox.askyesno(title=Trad.t045[language], message=Trad.t046[language], detail=Trad.t047[language], icon="warning")

                            if install_appimagetool:
                                automatic_install = messagebox.askyesno(title=Trad.t048[language], message=Trad.t049[language], detail=Trad.t050[language])

                                if automatic_install:
                                    try:
                                        request.urlretrieve(APPIMAGETOOL_URL.format(get_appimage_architecture()), "./appimagetool.appimage")
                                        subprocess.run(["chmod", "+x", "./appimagetool.appimage"], check=True)
                                        
                                    except Exception as e:
                                        messagebox.showerror(title=Trad.t061[language], message=Trad.t059[language], detail=Trad.t060[language] + str(e))
                                        window_easy_compile.destroy()
                                        return

                                else:
                                    window_manual_install_appimage = tk.Toplevel(window_easy_compile)
                                    window_manual_install_appimage.title(Trad.t051[language])

                                    step = [
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "1"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "2"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "3"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "4")
                                    ]

                                    text = [
                                        tk.Label(step[0], text=Trad.t053[language]),
                                        tk.Label(step[1], text=Trad.t055[language]),
                                        tk.Label(step[2], text=Trad.t056[language]),
                                        tk.Label(step[3], text=Trad.t058[language])
                                    ]

                                    for frame in step:
                                        frame.pack()
                                    for label in text:
                                        label.pack()
                                    
                                    button_step_0 = tk.Button(step[0], text=Trad.t054[language], command=lambda: webbrowser.open("https://github.com/AppImage/appimagetool/releases")).pack()

                                    button_close = tk.Button(window_manual_install_appimage, text=Trad.t057[language], command=window_manual_install_appimage.destroy).pack(pady=10)
                                    
                                    grab_set_and_wait_window(window_manual_install_appimage)

                                    window_easy_compile.destroy()
                                    return
                                    
                            else:
                                window_easy_compile.destroy()
                                return
                        
                        
                        try: shutil.rmtree("./dist/easycompile.AppDir")
                        except: pass

                        os.makedirs("./dist/easycompile.AppDir/usr/bin")

                        file_name = os.path.splitext(os.path.basename(os.path.abspath(file)))[0]

                        shutil.move("./dist/" + file_name, "./dist/easycompile.AppDir/usr/bin")

                        # desktop and apprun :
                        pathlib.Path("./dist/easycompile.AppDir/easycompile.desktop").write_text(file_info["desktop"].format(file_name, "appicon", combobox_section_appimage.get()))

                        pathlib.Path("./dist/easycompile.AppDir/AppRun").write_text(file_info["AppRun"].format(file_name))
                        subprocess.run(["chmod", "+x", "./dist/easycompile.AppDir/AppRun"], check=True)

                        path_icon = string_var_path_icon_appimage.get()
                        if path_icon == "[No icon]":
                            # make the icon :
                            icon = Image.new("RGB", (256,256), color="white")
                            icon.save("./dist/easycompile.AppDir/appicon.png", "png")
                        else:
                            shutil.move(path_icon, "./dist/easycompile.AppDir/appicon.png")

                        subprocess.run(["./appimagetool.appimage", "./dist/easycompile.AppDir"], check=True)

                        shutil.move(f"./appname-{get_appimage_architecture()}.AppImage", f"./dist/{file_name}.AppImage")

                        appimage_ok = True

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

                    button_save = tk.Button(frame_button_compile, text=Trad.t027[language], command=lambda: save_compile(".deb" if deb_ok else ".AppImage" if appimage_ok else "")).grid(column=0, row=0)

                    button_cancel = tk.Button(frame_button_compile, text=Trad.t028[language], command=window_easy_compile.destroy).grid(column=1, row=0)


                    frame_button_compile.pack()

                    grab_set_and_wait_window(window_end_compile)

                try:
                    frame_message.destroy()
                
                    disabeled_window(window_easy_compile, "normal")
                except:
                    pass




            else:       # window
                frame_message = compile_message()

                compile_ok = False
                deb_ok = False
                appimage_ok = False

                window_easy_compile.update()

                try:
                    result = subprocess.run(["wsl", "--status"], capture_output=True, text=True)

                    if result.returncode!=0:
                        messagebox.showerror(Trad.t085[language], Trad.t086[language], detail=Trad.t087[language])
                        window_easy_compile.destroy()
                        return
                    
                    result = subprocess.run(["wsl", "bash", "-lc", "pyinstaller -v"], capture_output=True, text=True)

                    if result.returncode!=0:
                        install_pyinstaller = messagebox.askquestion(Trad.t085[language], Trad.t088[language], detail=Trad.t089[language], icon="error")
                        
                        if install_pyinstaller:
                            automatic_install_pyinstaller = messagebox.askyesno(Trad.t090[language], Trad.t091[language], detail=Trad.t092[language])


                            if automatic_install_pyinstaller:
                                try:
                                    result = subprocess.run(["wsl", "pip", "install", "pyinstaller"], capture_output=True, text=True)

                                    if result.returncode != 0:
                                        raise Exception("Error with pip.")


                                except Exception as e:
                                    messagebox.showerror(Trad.t093[language], Trad.t094[language], detail=Trad.t095[language] + str(e))
                                    window_easy_compile.destroy()
                                    return

                            else:
                                window_install_pyinstaller = tk.Toplevel(window_easy_compile)
                                window_install_pyinstaller.title(Trad.t096[language])

                                texte_guide = tk.Label(window_install_pyinstaller, text=Trad.t097[language]).pack()

                                button_close_guide = tk.Button(window_install_pyinstaller, text=Trad.t098[language], command=window_install_pyinstaller.destroy).pack(pady=10)

                                grab_set_and_wait_window(window_install_pyinstaller)
                                window_easy_compile.destroy()
                                return


                        else:
                            window_easy_compile.destroy()
                            return
                    
                    def path_for_wsl():
                        """Make the path for use file on WSL"""
                        path = file[2:len(file)]

                        path = file[2:].replace("\\", "/")
                        
                        
                        return "/mnt/" + file[0].lower() + path
                    
                    subprocess.run(["wsl", "bash", "-lc", f"pyinstaller '{path_for_wsl()}' --onefile"], text=True, check=True)

                    if compile_type == text_type_of_compile["bin"]:
                        compile_ok = True
                    
                    elif compile_type == text_type_of_compile["deb"]:     # make a *.deb
                        # delet and make the folder :
                        
                        try: shutil.rmtree("dist\\easycompiledeb")
                        except: pass

                        
                        os.makedirs("dist\\easycompiledeb", exist_ok=True)

                        os.makedirs("dist\\easycompiledeb\\usr\\bin", exist_ok=True)

                        os.makedirs("dist\\easycompiledeb\\DEBIAN", exist_ok=True)

                        # --------

                        source_file = os.path.abspath(file)
                        parent_dir = os.path.dirname(source_file)
                        file_name = os.path.splitext(os.path.basename(source_file))[0]

                        
                        shutil.move("dist\\" + file_name, "dist\\easycompiledeb\\usr\\bin\\" + entry_name_one_path.get())

                        controle_file = file_info["control"].format(entry_title.get(), entry_vertion.get(), combobox_section.get(), entry_architecture.get(), entry_name.get(), entry_email.get(), entry_description.get())


                        pathlib.Path("dist\\easycompiledeb\\DEBIAN\\control").write_text(controle_file)

                        deb_build_dir = os.path.abspath("\\dist")

                                                
                        def path_for_deb():
                            """Return the path for copi the *.deb from WSL to Windows."""
                            path = os.path.abspath("dist")


                            path_linux = path[0].lower() + path[2:len(path)]

                            path_linux = path_linux.replace("\\", "/")

                            return "/mnt/" + path_linux
                        
                        def path_for_dpkg():
                            return path_for_deb() + "/easycompiledeb"


                        subprocess.run(["wsl", "bash", "-lc", f"cp -r {path_for_dpkg()} ~/"], check=True)
                                                
                        
                        subprocess.run(
                            ["wsl", "bash", "-lc", f"dpkg-deb --build ~/easycompiledeb"],
                            check=True,
                        )

                        subprocess.run(["wsl", "bash", "-lc", f"cp -r ~/easycompiledeb.deb {path_for_deb()}"], check=True)
                       
                        shutil.move("dist\\easycompiledeb.deb", "dist\\" + file_name + ".deb")

                        deb_ok = True
                        compile_ok = True
                    
                    elif compile_type == text_type_of_compile["appimage"]:       # make a appimage

                        result = subprocess.run(["wsl", "bash", "-lc", "test -f ~/appimagetool.appimage"])
                        
                        if result.returncode != 0:
                            install_appimagetool = messagebox.askyesno(title=Trad.t045[language], message=Trad.t046[language], detail=Trad.t047[language], icon="warning")

                            if install_appimagetool:
                                automatic_install = messagebox.askyesno(title=Trad.t048[language], message=Trad.t049[language], detail=Trad.t050[language])

                                if automatic_install:
                                    try:
                                        url = APPIMAGETOOL_URL.format(get_appimage_architecture())
                                        result = subprocess.run(
                                            ["wsl", "bash", "-lc", f"wget -O ~/appimagetool.appimage '{url}'"],
                                            capture_output=True,
                                            text=True,
                                        )

                                        if result.returncode != 0:
                                            raise Exception(result.stderr or result.stdout or "wget failed")

                                        result_chmod = subprocess.run(
                                            ["wsl", "bash", "-lc", "chmod +x ~/appimagetool.appimage"],
                                            capture_output=True,
                                            text=True,
                                        )

                                        if result_chmod.returncode != 0:
                                            raise Exception(result_chmod.stderr or result_chmod.stdout or "chmod failed")
                                        
                                    except Exception as e:
                                        messagebox.showerror(title=Trad.t061[language], message=Trad.t059[language], detail=Trad.t060[language] + str(e))
                                        window_easy_compile.destroy()
                                        return

                                else:
                                    window_manual_install_appimage = tk.Toplevel(window_easy_compile)
                                    window_manual_install_appimage.title(Trad.t051[language])

                                    text_info_wsl = tk.Label(window_manual_install_appimage, text=Trad.t099[language]).pack()

                                    step = [
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "1"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "2"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "3"),
                                        tk.LabelFrame(window_manual_install_appimage, text=Trad.t052[language] + "4")
                                    ]

                                    text = [
                                        tk.Label(step[0], text=Trad.t053[language]),
                                        tk.Label(step[1], text=Trad.t055[language]),
                                        tk.Label(step[2], text=Trad.t100[language]),
                                        tk.Label(step[3], text=Trad.t058[language])
                                    ]

                                    for frame in step:
                                        frame.pack()
                                    for label in text:
                                        label.pack()
                                    
                                    button_step_0 = tk.Button(step[0], text=Trad.t054[language], command=lambda: webbrowser.open("https://github.com/AppImage/appimagetool/releases")).pack()

                                    button_close = tk.Button(window_manual_install_appimage, text=Trad.t057[language], command=window_manual_install_appimage.destroy).pack(pady=10)
                                    
                                    grab_set_and_wait_window(window_manual_install_appimage)

                                    window_easy_compile.destroy()
                                    return
                                    
                            else:
                                window_easy_compile.destroy()
                                return
                        
                        try: shutil.rmtree("dist\\easycompile.AppDir")
                        except: pass

                        os.makedirs("dist\\easycompile.AppDir\\usr\\bin")

                        file_name = os.path.splitext(os.path.basename(os.path.abspath(file)))[0]

                        shutil.move("dist\\" + file_name, "dist\\easycompile.AppDir\\usr\\bin")

                        # desktop and apprun :
                        pathlib.Path("dist\\easycompile.AppDir\\easycompile.desktop").write_text(file_info["desktop"].format(file_name, "appicon", combobox_section_appimage.get()), newline="\n")

                        pathlib.Path("dist\\easycompile.AppDir\\AppRun").write_text(file_info["AppRun"].format(file_name), newline="\n")

                        path_icon = string_var_path_icon_appimage.get()
                        if path_icon == "[No icon]":
                            # make the icon :
                            icon = Image.new("RGB", (256,256), color="white")
                            icon.save("dist\\easycompile.AppDir\\appicon.png", "png")
                        else:
                            shutil.move(path_icon, "dist\\easycompile.AppDir\\appicon.png")

                        
                        def path_for_appimage():
                            """Return the path for copi the easycompile.AppDir directory from WSL to Windows."""
                            return path_for_linux() + "/easycompile.AppDir"

                        def path_for_linux():
                            path = os.path.abspath("dist")

                            path_linux = path[0].lower() + path[2:len(path)]

                            path_linux = path_linux.replace("\\", "/")

                            return "/mnt/" + path_linux

                        subprocess.run(["wsl", "bash", "-lc", f"cp -r {path_for_appimage()} ~/"], check=True)

                        subprocess.run(["wsl", "bash", "-lc", "chmod +x ~/easycompile.AppDir/AppRun"], check=True)
                        subprocess.run(["wsl", "bash", "-lc", f"chmod +x ~/easycompile.AppDir/usr/bin/{os.path.splitext(os.path.basename(file))[0]}"], check=True)
                     

                        subprocess.run(["wsl", "bash", "-lc", "cd ~ && ~/appimagetool.appimage ~/easycompile.AppDir"], check=True)

                        subprocess.run(["wsl", "bash", "-lc", f"cp -r ~/appname-{get_appimage_architecture()}.AppImage {path_for_linux()}"], check=True)

                        
                        shutil.move(f"dist\\appname-{get_appimage_architecture()}.AppImage", f"dist\\{file_name}.AppImage")

                        appimage_ok = True
                        compile_ok = True

                except Exception as e:
                    window_error(window_easy_compile, Trad.t008[language], Trad.t009[language], str(e))

                    print(traceback.format_exc())

                    window_easy_compile.update()
                    compile_ok = False
                
                if compile_ok :
                    window_end_compile = tk.Toplevel(window_easy_compile)
                    window_end_compile.title(Trad.t025[language])

                    text_info = tk.Label(window_end_compile, text=Trad.t026[language]).pack()

                    frame_button_compile = tk.Frame(window_end_compile)

                    button_save = tk.Button(frame_button_compile, text=Trad.t027[language], command=lambda: save_compile(".deb" if deb_ok else ".AppImage" if appimage_ok else "")).grid(column=0, row=0)

                    button_cancel = tk.Button(frame_button_compile, text=Trad.t028[language], command=window_easy_compile.destroy).grid(column=1, row=0)


                    frame_button_compile.pack()

                    grab_set_and_wait_window(window_end_compile)

                try:
                    frame_message.destroy()
                
                    disabeled_window(window_easy_compile, "normal")
                except:
                    pass
                
                


        # -------------------- setting of compile :
        # deb :
        entry_vertion = None
        combobox_section = None
        entry_architecture = None
        entry_name = None
        entry_email = None
        entry_description = None
        entry_title = None
        entry_name_one_path = None
        # appimage :
        combobox_section_appimage = None
        string_var_path_icon_appimage = None
        # ---------


        frame_type_compiling = tk.LabelFrame(frame, text=Trad.t002[language])

        text_info_compiling = tk.Label(frame_type_compiling, text=Trad.t001[language])
        text_info_compiling.pack()

        list_compiling = ttk.Combobox(frame_type_compiling, values=[text_type_of_compile["bin"], text_type_of_compile["deb"], text_type_of_compile["appimage"]], state="readonly", width=25)
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
        def make_frame_setting_appimage():
            """Return the frame setting appimage"""
            frame_setting_appimage = tk.LabelFrame(frame_setting_deb_1, text=Trad.t043[language])
            frame_setting_appimage.grid(column=0, row=0)
            return frame_setting_appimage

        frame_setting_deb = make_frame_setting_deb()
        frame_setting_appimage = None

        def set_frame_config():
            nonlocal frame_config_type, frame_setting_deb, entry_vertion, combobox_section, entry_architecture, entry_name, entry_email, entry_description, entry_title, entry_name_one_path, frame_setting_appimage, combobox_section_appimage, string_var_path_icon_appimage
            WITH_ENTRY = 15
            # setting for normal compil :
            
            if list_compiling.get() == text_type_of_compile["deb"] and (frame_config_type=="bin" or frame_config_type=="appimage"):
                if frame_config_type == "appimage":
                    frame_setting_appimage.destroy()
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
                            if (not(char in CHAR_LIST["09"])) and (char != "."):
                                return False
                        
                        return True
                    
                    def title_ok(title:str):
                        """Return True if the title is good, False else"""
                        for char in title:
                            if (char not in CHAR_LIST["09"]) and (char not in CHAR_LIST["az"]) and (char not in "-+."):
                                return False
                        
                        return True

                    def name_path_ok(name_path):
                        """Retunr True if the name is good, False else"""
                        for char in name_path:
                            if (char not in CHAR_LIST["09"]) and (char not in CHAR_LIST["az"]) and (char != "_"):
                                return False
                        return True


                    RED = "#FF0000"
                    NORMAL = "#FFFFFF"
                    try:
                        def field_error(entry):
                            """Set bg of entry to red and disabeled the buton for compile"""
                            nonlocal bad_config
                            entry.configure(bg=RED)
                            bad_config = True
                        
                        def field_normal(entry):
                            """Set bg of entry to normal"""
                            entry.configure(bg=NORMAL)

                        bad_config = False
                        
                        version = entry_vertion.get()
                        if version == "" or not(vertion_ok(version)):
                            field_error(entry_vertion)
                        else: 
                            field_normal(entry_vertion)

                        name = entry_name.get()
                        if name == "":
                            field_error(entry_name)
                        else:
                            field_normal(entry_name)
                        
                        email = entry_email.get()
                        if email == "" :
                            field_error(entry_email)
                        else: 
                            field_normal(entry_email)
                        
                        description = entry_description.get()
                        if description == "":
                            field_error(entry_description)
                        else: 
                            field_normal(entry_description)
                        
                        titel = entry_title.get()
                        if titel == "" or not(title_ok(titel)):
                            field_error(entry_title)
                        else:
                            field_normal(entry_title)
                        
                        path_name = entry_name_one_path.get()
                        if path_name == "" or not(name_path_ok(path_name)):
                            field_error(entry_name_one_path)
                        else:
                            field_normal(entry_name_one_path)

                        if bad_config: button_compile["state"] = "disabled"
                        else: button_compile["state"] = "normal"


                        frame_setting_deb.after(UPTATE_GUIT, control_config)

                    except: pass
                
                control_config()

            elif list_compiling.get() == text_type_of_compile["appimage"] and frame_config_type != "appimage":
                if frame_config_type == "deb":
                    frame_setting_deb.destroy()
                frame_config_type = "appimage"

                frame_setting_appimage = make_frame_setting_appimage()

                appimage_column_0 = tk.Frame(frame_setting_appimage)
                appimage_column_0.grid(column=0, row=0)

                appimage_column_1 = tk.Frame(frame_setting_appimage)
                appimage_column_1.grid(column=1, row=0)
                
                text_section_appimage = tk.Label(appimage_column_0, text=Trad.t044[language]).grid(column=0, row=0)
                combobox_section_appimage = ttk.Combobox(appimage_column_0, values=["Utility", "Development", "Graphics", "Office", "Internet", "Multimedia", "System", "Education", "Game"], state="readonly", width=WITH_ENTRY)
                combobox_section_appimage.current(0)
                combobox_section_appimage.grid(column=1, row=0)

                text_icon_appimage = tk.Label(appimage_column_0, text=Trad.t062[language]).grid(column=0, row=1)
                
                def set_icon():
                    """Open an icon in png for the appimage"""
                    messagebox.showinfo(title=Trad.t064[language], message=Trad.t065[language], detail=Trad.t066[language])

                    path = filedialog.askopenfilename(filetypes=[("Portable Netowrk Graphic","*.png")])

                    if isinstance(path, tuple):
                        path = path[0]
                    
                    if path != "":
                        string_var_path_icon_appimage.set(path)

                button_icon = tk.Button(appimage_column_0, text=Trad.t063[language], command=set_icon).grid(column=1, row=1)

                string_var_path_icon_appimage = tk.StringVar(appimage_column_0, value="[No icon]")
                text_path_icon_appimage = tk.Label(appimage_column_0, textvariable=string_var_path_icon_appimage, font=("Arial", 7), state="disabled").grid(column=0, row=2, columnspan=2)
                
                


            elif list_compiling.get() == text_type_of_compile["bin"] :
                if frame_config_type == "deb":
                    frame_setting_deb.destroy()
                elif frame_config_type == "appimage":
                    frame_setting_appimage.destroy()
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
    compile_notebok.add(frame_compile_Window, text="Window", state="normal" if os_name == "win32" else "normal")

    configure_frame_windows(frame_compile_Window)

    # Linux :
    frame_compile_Linux = tk.Frame(compile_notebok)
    compile_notebok.add(frame_compile_Linux, text="Linux", state="normal" if os_name == "linux" else "normal")

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

                grab_set_and_wait_window(window_error_install)

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

                    grab_set_and_wait_window(window_pyinstaller_install)
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

            grab_set_and_wait_window(window_manual_install)

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

        grab_set_and_wait_window(window_no_pyinstaller)

    try:
        grab_set_and_wait_window(window_easy_compile)
    except:
        pass

    
