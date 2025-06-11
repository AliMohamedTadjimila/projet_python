import win32gui # récupérer la fenêtre active windows
import win32process
import psutil # récupérer des informations sur les processus en cours d'exécution et les ressources système
import getpass # récupéré le nom d'user windows
import time
from datetime import datetime

def get_active_window_info():
    window =win32gui.GetForegroundWindow() # récupérer la fenêtre qui est actuellement au premier plan
    user = getpass.getuser() # obtenir le nom d'user actuel
    if window == 0:
        return None # pas de fenêtre active 

    title = win32gui.GetWindowText(window)  # récupérer le nom de cette fenêtre


    # récupérer le nom de l'aplication associee
    #gerer les scenario des erreurs
    try:
        pid = win32process.GetWindowThreadProcessId(window)[1] # rcupere l'identifiant du processus associe a la fenetre active
        process = psutil.Process(pid) # on cree un objet processus
        app_name =process.name() # recupere le nom du fichier excutable de l'app
    except Exception as e: # si y a erreur du PID[1] met inconnu
        app_name = "Inconnu"


    # on prend la date et heure 
    timestamp =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       # on retourne un dictionnaire contenant titre,nom,date et heure
    return{
        "Titre": title,
        "nom_app": app_name,
        "date_heure": timestamp,
        "Utilisateur" : user,
    }

    

start_time = time.time() # enreigistrer le temps actuel
last_title =None #memoriser le dernier fenetre active
compteur = 1
current_window_start = time.time() # permet de mesurer le momemnt ou une fentre devient active
with open("Liste_fenetres.txt", "w", encoding="utf-8") as fichier:
    pass
    while True:
    
      if time.time() -start_time > 30:
        print("fin du suivi (30 secondes).") #arreter apres 30 secondes
        break

      info = get_active_window_info()

      if info and info.get("Titre") != last_title: # verifier si le titre est valide et different
        now =time.time() # retourne l'heure actuelle en secondes
        if last_title is not None: # si ce n'est pas la premiere fenetre, calcule la duree
           duree =int(now - current_window_start)
           print(f"Duree d'utilisation de la fenetre precedente '{last_title}': {duree} seconde!")
           fichier.write(f"Duree: {duree} secondes!\n")
           fichier.flush()
        current_window_start = now
        ligne = (f"[{info['date_heure']}] | Fenetre active: {info['Titre']} | Utilisateur : {info['Utilisateur']} |App : {info['nom_app']}\n")
        # afficher dans la console
        print(ligne.strip())
        # ecrire dans le fichier
        fichier.write(ligne)
        # sauvegarder immediat
        fichier.flush()
        compteur += 1
        last_title = info["Titre"]
    time.sleep(1)