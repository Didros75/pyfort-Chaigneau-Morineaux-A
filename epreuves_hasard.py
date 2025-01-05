"""contient l'epeuve du bonneteau et des dés. Les epreuves retournent True si elles sont reussies et False sinon"""
import random
import time

import fenetre_graphique
from fenetre_graphique import *

ecran=fenetre_graphique.ecran
bonneteau_menu=pygame.image.load("Assets/Bonneteau.jpg")
dé_menu=pygame.image.load("Assets/Dé.jpg")
bonneteau_menu = pygame.transform.scale(bonneteau_menu, ecran.get_size())
dé_menu = pygame.transform.scale(dé_menu, ecran.get_size())

def jeu_lance_des():
    "le joueur tire 2 dés, et si un des deux fais 6 il gagne, sinon c'est au maitre de le faire. Au bout de 3 essais chacun, si personne n'as eu de 6, c'est match nul et aucune clé n'est accordée"
    ecran.blit(dé_menu, (0, 0))
    pygame.display.flip()
    nb_essai=3
    des=[1,2,3,4,5,6]
    while nb_essai>0:
        ecran.blit(dé_menu, (0, 0))
        message=str(nb_essai) + "essais"
        afficher_texte(ecran, message, 40, (400, 500))
        choix_multiple(["Lancer"])
        de_joueur = (random.choice(des), random.choice(des))
        afficher_texte(ecran, str(de_joueur[0]), 60, (ecran.get_width() / 2-100, ecran.get_height() /2 -110))
        afficher_texte(ecran, str(de_joueur[1]), 60, (ecran.get_width() / 2+50, ecran.get_height() /2 -110))
        time.sleep(2)
        if de_joueur[0]==6 or de_joueur[1]==6:
            return True
        ecran.blit(dé_menu, (0, 0))
        message="c'est au tour du maître du jeu"
        afficher_texte(ecran, message, 40, (220, 160))
        de_maitre = (random.choice(des), random.choice(des))
        afficher_texte(ecran, str(de_maitre[0]), 60, (ecran.get_width() / 2 - 100, ecran.get_height() / 2 -110))
        afficher_texte(ecran, str(de_maitre[1]), 60, (ecran.get_width() / 2+ 50, ecran.get_height() / 2 -110))
        if de_maitre[0]==6 or de_maitre[1]==6:
            afficher_texte(ecran, "Le maitre du jeu a remporté la partie", 40, (200, 100))
            time.sleep(2)
            return False
        afficher_texte(ecran, "Aucun 6 n'a été obtenu, on continue", 40, (220, 450))
        time.sleep(2)
        nb_essai -= 1
    return False

def bonneteau():
    "un des 3 bonneteau est choisi au hasard, le joueur a une chance sur 3 de trouver le bon. S'il echoue, il a une deuxieme chance"
    ecran.blit(bonneteau_menu,(0,0))
    pygame.display.flip()
    liste=[1,2,3]
    nb_tentatives=2
    afficher_texte(ecran, "Choisissez un Bonneteau", 30, (200, 50))

    for i in range(2):
        texte='il vous reste ' + str(nb_tentatives)+ ' tentatives'
        afficher_texte(ecran, texte, 30, (200, 90))

        lettre=random.choice(liste)
        Bonneteau_choisi=choix_multiple(["A", "B", "C"])
        if Bonneteau_choisi==lettre:
            return True
        else:
            afficher_texte(ecran, "dommage, essaye encore", 30, (200, 130))
            ecran.blit(bonneteau_menu,(0,0))
        nb_tentatives-=1

    return False
