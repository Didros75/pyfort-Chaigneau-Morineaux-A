"""dans ce module, on appelle l'epeuve finale"""
import json
import random
import time

import fenetre_graphique
import pygame

from fenetre_graphique import afficher_texte, entrer_texte

ecran = fenetre_graphique.ecran
Menu_enigme = pygame.image.load('Assets/Enigmes.jpg')
Menu_enigme = pygame.transform.scale(Menu_enigme, ecran.get_size())


def salle_De_Tresor():
    "on recupere d'abord la liste de dictionnaire, on les trie par année, on en choisi une au hasard, puis on choisi une emission au hasard, on affiche d'abord 3 indices, puis un nouveau a chaque erreur, et on regarde si la reponse attendue est dans la reponse de l'utilisateur"
    with open('indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)
        jeu_tv_annee=jeu_tv['Fort Boyard']
    liste_annee = []
    for i in jeu_tv_annee.keys():
        liste_annee.append(i)
    annee=random.choice(liste_annee)
    annee_emission=jeu_tv_annee[annee]
    liste_emission = []
    for i in annee_emission.keys():
        liste_emission.append(i)
    emission=random.choice(liste_emission)
    liste_indices=annee_emission[emission]['Indices']
    mot_code=annee_emission[emission]['MOT-CODE'].lower()
    ecran.blit(Menu_enigme, (0, 0))
    afficher_texte(ecran, "Trouver le bon mot grâce aux indices : ", 40, (100, 100))
    afficher_texte(ecran, liste_indices[0], 30, (100, 160))
    afficher_texte(ecran, liste_indices[1], 30, (100, 200))
    afficher_texte(ecran, liste_indices[3], 30, (100, 240))
    cpt=3
    reponse_correcte=False
    while cpt>0:
        reponse_joueur=entrer_texte(ecran, ((120, 520),(300, 50)), 30).lower()
        if mot_code in reponse_joueur:
            #les reponses sont en un seul mot, donc si le joueur repond La Pluie au lieu de simplement Pluie, il aura bon
            return True
        else:
            cpt-=1
            message="Il vous reste " + str(cpt) + " essais"
            afficher_texte(ecran, message, 20, (120, 580 + ((3 - cpt) * 20)))
            if cpt>0:
                if cpt==2:
                    afficher_texte(ecran, liste_indices[4], 30, (100, 280))
                else:
                    afficher_texte(ecran, liste_indices[5], 30, (100, 320))
            else:
                message="Le mot etait " + mot_code
                afficher_texte(ecran,message, 30, (120, 650))
                time.sleep(2)


    return False