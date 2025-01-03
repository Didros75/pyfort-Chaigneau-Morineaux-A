import json
import random
from time import sleep

import fenetre_graphique
import pygame

from fenetre_graphique import afficher_texte, entrer_texte

ecran = fenetre_graphique.ecran
Menu_enigme = pygame.image.load('Assets/Enigmes.jpg')
Menu_enigme = pygame.transform.scale(Menu_enigme, ecran.get_size())


def charger_enigmes():
    with open('enigmesPF.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees

def enigme_pere_fouras():
    ecran.blit(Menu_enigme, (0, 0))
    pygame.display.flip()
    donnees=charger_enigmes()
    nb_essais=3
    liste=[]
    for i in donnees:
        liste.append(i["question"])
    enigme=random.choice(liste)
    for i in donnees:
        if i["question"] == enigme:
            reponse=i["reponse"].lower()
    enigme_coupée = enigme.split("\n")
    j=0
    afficher_texte(ecran, "Enigme :", 50, (120, 160))
    for i in enigme_coupée:
        afficher_texte(ecran, i, 30, (120, 230+j*50))
        j+=1
    while nb_essais>0:
        utilisateur_rep=entrer_texte(ecran, ((120, 520),(300, 50)), 30).lower()
        if utilisateur_rep in reponse and len(utilisateur_rep)>=3:
            return True
        else:
            nb_essais-=1
            if nb_essais==2:
                message="La réponse est incorrecte, il vous reste 2 essais"
                afficher_texte(ecran, message, 30, (120, 610))
            elif nb_essais==1:
                message = "La réponse est incorrecte, il vous reste 1 essai"
                afficher_texte(ecran, message, 30, (120, 650))
            else:
                message="Vous avez échoué à l'énigme la solution était: " + str(reponse)
                afficher_texte(ecran, message, 40, (120, 680))
                sleep(4)
                return False