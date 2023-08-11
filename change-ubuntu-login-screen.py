import os
import tkinter as tk
from tkinter import filedialog

def file_location(titre):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title=str(titre), filetypes=(("Fichiers JPG", "*.jpg"), ("Tous les fichiers", "*.*")))

    return str(file_path)


os.system("clear")
print("choisissez une option : ")
print("(1) Installer un arrière plan personnnalisé")
print("(2) Restaurer l'arrière plan")
print("(0) Quitter")
choix = int(input(">>> "))

if str(choix) == "1":
    os.system("sudo apt install libglib2.0-dev-bin")
    os.system("clear")
    input("Veuillez maintenant choisir l'arrière plan à utiliser, Appyuez sur entrer pour continuer ...")
    location = file_location("Arrière plan")
    os.system("clear")
    os.system("wget -qO - https://github.com/PRATAP-KUMAR/ubuntu-gdm-set-background/archive/main.tar.gz | tar zx --strip-components=1 ubuntu-gdm-set-background-main/ubuntu-gdm-set-background")
    os.system("sudo ./ubuntu-gdm-set-background --image "+location)

elif str(choix) == "2":
    os.system("clear")
    os.system("sudo ./ubuntu-gdm-set-background --reset")

else:
    exit()
