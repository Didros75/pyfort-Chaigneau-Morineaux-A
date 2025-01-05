"contient l'epreuve du jeu de nim, renvoie True si elle est reussite"
import random

import pygame
from fenetre_graphique import *
import time
import fenetre_graphique
ecran = fenetre_graphique.ecran


def afficher_batonnets(n):
    "va chercher la fonction d'affichage des n batonnets"
    afficher_batons_graphique(ecran, n)

def joueur_retrait():
    "demande au joueur de choisir 1 2 ou 3 batonnets a enlever"
    choix=-1
    while choix == -1:
        choix=choix_multiple(["1 bâton", "2 bâtons", "3 bâtons"])

    return choix

def maitre_retrait(n):
    "Le maitre regarde combien de batons il reste et essaye toujours d'en enlever de facon a ce qu'il en reste un multiple de 4 plus 1. Il retourne le nombre de batonnets restant apres son opperation. S'il commence, il gagne toujours"
    index=n
    while index%4!=1 and index>=n-2 or index==n:
        index=index-1

    return n-index

def jeu_nim():
    "choisis de maniere aléatoire qui commence, appelle joueur_retrait et maitre_retrait alternativement, et renvoie True si c'est le maitre qui prend le dernier baton, False sinon"
    batonnets=20
    tour_joueur=random.choice([True, False])
    while batonnets>0:
        afficher_batonnets(batonnets)
        if tour_joueur:
            batonnets-=joueur_retrait()
            tour_joueur=False
        else:
            time.sleep(1)
            choix_maitre=maitre_retrait(batonnets)
            batonnets-=choix_maitre
            tour_joueur=True
    return tour_joueur

