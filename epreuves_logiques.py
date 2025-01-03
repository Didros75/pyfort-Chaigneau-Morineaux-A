import random

import pygame
from fenetre_graphique import *
import time
import fenetre_graphique
ecran = fenetre_graphique.ecran


def afficher_batonnets(n):
    afficher_batons_graphique(ecran, n)

def joueur_retrait(n):
    choix=-1
    while choix == -1:
        choix=choix_multiple(["1 bâton", "2 bâtons", "3 bâtons"])

    return choix

def maitre_retrait(n):
    index=n
    while index%4!=1 and index>=n-2 or index==n:
        index=index-1

    return n-index

def jeu_nim():
    batonnets=20
    tour_joueur=random.choice([True, False])
    while batonnets>0:
        afficher_batonnets(batonnets)
        if tour_joueur:
            batonnets-=joueur_retrait(batonnets)
            tour_joueur=False
        else:
            time.sleep(1)
            choix_maitre=maitre_retrait(batonnets)
            batonnets-=choix_maitre
            tour_joueur=True
    return tour_joueur

