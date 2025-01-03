""" Dans ce module, nous allons mettre les fonctions utiles au deroulement de notre programme"""
import pygame.time

import fenetre_graphique
from fenetre_graphique import *
from epreuves_mathematiques import *
from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
import json

boyard_fond=pygame.image.load('Assets/img.png')
boyard_fond = pygame.transform.scale(boyard_fond, ecran.get_size())
Menu_equipe = pygame.image.load('Assets/Menu_equipe.jpg')
Menu_equipe = pygame.transform.scale(Menu_equipe, ecran.get_size())
Menu_nb_equipe = pygame.image.load('Assets/nb_equipe.jpg')
Menu_nb_equipe = pygame.transform.scale(Menu_nb_equipe, ecran.get_size())
Menu_neutre2=pygame.image.load('Assets/document_0.jpg')
Menu_neutre2=pygame.transform.scale(Menu_neutre2, ecran.get_size())
ecran = fenetre_graphique.ecran

def introduction():
    print("Bienvenue sur Fort Boyard Simulator ! \n Constituez deux equipes de 1 a 3 joueurs et affrontez vous dans une serie de mini jeux dans le but de gagner des clés et d'accéder a la salle du tresor !")

def composer_equipe():
    ecran.blit(Menu_nb_equipe, (0, 0))
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)

    liste_player=[]

    nbJoueurs=0
    while nbJoueurs == 0:
        nbJoueurs=choix_multiple(["1 joueur", "2 joueurs", "3 joueurs"])
    ecran.blit(Menu_neutre2, (0, 0))
    e1=[]
    e2=[]
    #l'interface graphique ne dépend pas de la résolution de l'écran donc peux être décalée sur certain ordi
    for i in range(nbJoueurs*2):
        if i<nbJoueurs:
            afficher_texte(ecran, "Equipe 1", 50, (80, 100))

            afficher_texte(ecran, "Prenom :", 30, (80, 210))
            afficher_texte(ecran, "Nom :", 30, (120, 300))
            pygame.draw.rect(ecran, "black", ((200, 210), (300, 50)))
            pygame.draw.rect(ecran, "black", ((200, 300), (300, 50)))
            prenom = entrer_texte(ecran, ((200, 210), (300, 50)), 24)
            nom = entrer_texte(ecran, ((200, 300), (300, 50)), 24)
            e1.append(prenom)
            for i in range(len(e1)):
                afficher_texte(ecran, e1[i], 40, (200, 400+i*40))
        else:
            afficher_texte(ecran, "Equipe 2", 50, (640, 100))

            afficher_texte(ecran, "Prenom :", 30, (640, 210))
            afficher_texte(ecran, "Nom :", 30, (680, 300))
            pygame.draw.rect(ecran, "black", ((760, 210), (300, 50)))
            pygame.draw.rect(ecran, "black", ((760, 300), (300, 50)))
            prenom = entrer_texte(ecran, ((760, 210), (300, 50)), 24)
            nom = entrer_texte(ecran, ((760, 300), (300, 50)), 24)
            e2.append(prenom)

            for i in range(len(e2)):
                afficher_texte(ecran, e2[i], 40, (760, 400 + i * 40))
        pygame.time.wait(1000)

        present = False
        for personne in donnees:
            if personne["Nom"] == nom and personne["Prenom"] == prenom:
                present=True
        if not present:
            donnees.append({"Nom": nom, "Prenom": prenom, "Score":0})

        if prenom not in liste_player:
            liste_player.append(prenom)
        else:
            prenom_nom=prenom + " " + nom
            liste_player.append(prenom_nom)
    with open('players_sauvegarde.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f, indent=4)

    equipe1=liste_player[:int(len(liste_player)/2)]
    equipe2=liste_player[int(len(liste_player)/2):]

    return equipe1, equipe2

def menu_epreuves():
    liste_catgories = ["Maths", "Hasard", "Logique", "Enigme"]
    liste_mini_jeux_maths = ["factorielle", "roulette_mathematique", "equation"]
    liste_mini_jeux_hasard = ["Bonneteau"]
    categorie=""
    jeu=""
    message="Choisis une catégorie"

    while categorie == "":
        afficher_texte(ecran, message, 50, ((100, 200), (300, 70)))
        categorie=liste_catgories[choix_multiple(liste_catgories)-1]

    ecran.blit(Menu_neutre2, (0, 0))

    if categorie=="Maths":
        jeu=random.choice(liste_mini_jeux_maths)
    if jeu=="factorielle":
        return jeu_factorielle()
    elif jeu=="roulette_mathematique":
        return roulette_mathematique()
    elif jeu=="equation":
        return epreuve_math_equation()

    if categorie=="Hasard":
        jeu=random.choice(liste_mini_jeux_hasard)
    if jeu=="dés":
        return jeu_lance_des()
    elif jeu=="Bonneteau":
        return bonneteau()

    if categorie=="Logique":
        return jeu_nim()

    if categorie=="Enigme":
        return enigme_pere_fouras()

def choisir_joueur(equipe):
    candidat="^"
    afficher_texte(ecran, "Choisir le joueur", 50, ((100, 200),(300, 300)))
    while candidat == "^":

        if len(equipe)==1:
            candidat=choix_multiple([equipe[0]])
        elif len(equipe)==2:
            candidat=choix_multiple([equipe[0], equipe[1]])
        else:
            candidat = choix_multiple([equipe[0], equipe[1], equipe[2]])
    return equipe[candidat-1]


def epreuve_finale(equipe_numero, equipe):
    if salle_De_Tresor():
        score_incrementation(equipe)
        return True
    return False


def score_incrementation(equipe):
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    for personne in donnees:
        for player in equipe:
            if personne["Prenom"] == player:
                personne["Score"]=personne["Score"]+1
    with open('players_sauvegarde.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f)


def leader_board():
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        leader_board_liste=[]
        while donnees!=[]:
            best_player=""
            best_score=-1
            best_index=0
            index=0
            for personne in donnees:
                try:
                    if personne["Score"] > best_score:
                        best_player=personne["Prenom"]
                        best_score=personne["Score"]
                        best_index=index
                except:
                    pass
                index+=1

            leader_board_liste.append(best_player)
            donnees.pop(best_index)
    return leader_board_liste





def supprimer_sauvegarde():
    with open('players_sauvegarde.json', 'w', encoding='utf-8') as f:
        json.dump([], f)

