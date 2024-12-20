import random
import pygame
import fenetre_graphique
from fenetre_graphique import *
ecran=fenetre_graphique.ecran
bonneteau_menu=pygame.image.load("Assets/Bonneteau.jpg")
dé_menu=pygame.image.load("Assets/Dé.jpg")
bonneteau_menu = pygame.transform.scale(bonneteau_menu, ecran.get_size())
dé_menu = pygame.transform.scale(dé_menu, ecran.get_size())

def jeu_lance_des():
    ecran.blit(dé_menu, (0, 0))
    pygame.display.flip()
    nb_essai=3
    des=[1,2,3,4,5,6]
    while nb_essai>0:
        message=str(nb_essai) + "essais"
        afficher_texte(ecran, message, 40, (400, 500))
        choix_multiple(["Lancer"])
        de_joueur = (random.choice(des), random.choice(des))
        afficher_texte(ecran, de_joueur, 60, (300, 500))
        if de_joueur[0]==6 or de_joueur[1]==6:
            print("vous avez gagnez une clé")
            return True
        message="c'est au tour du maître du jeu"
        print(message)
        de_maitre = (random.choice(des), random.choice(des))
        print(de_maitre)
        if de_joueur[0]==6 or de_joueur[1]==6:
            print("Le maître du jeu a remporté la partie")
            return False
        print("Aucun 6 n'est obtenu, on passe au prochain essai")
        nb_essai -= 1
    print("Aucun joueur n'a obtenu 6 après trois essais, c'est match nul")
    return False

def bonneteau():
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
    print("Vous avez perdu")
    return False
