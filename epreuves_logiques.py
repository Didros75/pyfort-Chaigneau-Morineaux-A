import pygame

import random

def afficher_batonnets(n):
    for i in range(n):
        print("|")

def joueur_retrait(n):
    choix=-1
    while choix == -1:
        choix=int(input("Choisi un nombre de batonnets a enlever"))

    return choix

def maitre_retrait(n):
    index=n
    while index%4!=1:
        index=index-1
    return n-index

def jeu_nim():
    batonnets=20
    tour_joueur=False
    while batonnets>0:
        afficher_batonnets(batonnets)
        if tour_joueur:
            print("Au joueur de jouer :")
            batonnets-=joueur_retrait(batonnets)
            tour_joueur=False
        else:
            choix_maitre=maitre_retrait(batonnets)
            print("Le maitre du jeu enleve", str(choix_maitre), "batonnets")
            batonnets-=choix_maitre
            tour_joueur=True
    return tour_joueur

print(jeu_nim())