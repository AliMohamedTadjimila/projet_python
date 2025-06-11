import tkinter as tk #creer l'interface graphique
import os # interagir avec le systeme d'exploitation et manipuler les fichiers et dossiers
from tkinter import messagebox #importer une boite de dialogue

fichier_log = "Liste_fenetres.txt"

#creer la fenetre principale de l'app
fenetre = tk.Tk()
fenetre.title("Visualiseur de logs")
fenetre.geometry("700x500") # definit la taille de la fenetre

#verifier si le fichier log existe
if os.path.exists(fichier_log):
    #ouvrir le fichier en mode lecture avec encodage utf-8
    with open(fichier_log, "r", encoding="utf-8") as f:
        contenu = f.read()
else:
    contenu = "le fichier liste_fenetres.txt n'existe pas."

# Création d'une zone de texte avec retour à la ligne automatique
zone_texte = tk.Text(fenetre, wrap = "word")
# Insertion du texte au début de la zone de texte
zone_texte.insert("1.0" , contenu)
# Désactivation de l'édition (lecture seule)
zone_texte.config(state="disabled")
# Affichage de la zone de texte, remplissant tout l'espace disponible
zone_texte.pack(expand=True, fill="both")

# fonction du server
def envoyer_logs():


     messagebox.showinfo("Envoyer les logs", "les logs ont ete envoyee au serveur distant!!") 

#creer la fenetre pour envoyer les logs au serveur 

btn_envoyer = tk.Button(fenetre, text="Envoyer les logs", command=envoyer_logs)
btn_envoyer.pack(side=tk.LEFT, padx=20, pady=10)
#creer un bouton pour fermer la fenetre

btn_fermer = tk.Button(fenetre, text="Fermer",command=fenetre.destroy)
btn_fermer.pack(pady=10)

fenetre.mainloop()