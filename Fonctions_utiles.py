""" Dans ce module, nous allons mettre les fonctions utiles au deroulement de notre programme"""
from pyexpat.errors import messages

from epreuves_mathematiques import *
import json

liste_mini_jeux=["factorielle", "roulette_mathematique", "equation"]

def introduction():
    print("Bienvenue sur Fort Boyard Simulator ! \n Constituez deux equipes de 1 a 3 joueurs et affrontez vous dans une serie de mini jeux dans le but de gagner des clés et d'acceder a la salle du tresor !")

def composer_equipe():
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)


    liste_player=[]
    nbJoueurs=-1
    while nbJoueurs <= 0 or nbJoueurs > 3:
        try:
            nbJoueurs=int(input("Nombre de joueurs par equipe (entre 1 et 3) : "))
        except:
            nbJoueurs=-1

    for i in range(nbJoueurs*2):
        if i<nbJoueurs:
            print("Equipe 1")
        else:
            print("Equipe 2")

        prenom = input("Prenom : ")
        nom = input("Nom : ")
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
        json.dump(donnees, f)

    equipe1=liste_player[:int(len(liste_player)/2)]
    equipe2=liste_player[int(len(liste_player)/2):]

    return equipe1, equipe2

def menu_epreuves():
    jeu=""
    message="Choisis un jeu parmis " + str(liste_mini_jeux) + " : "
    while jeu not in liste_mini_jeux:
        jeu=input(message)
    print("Jeu :", jeu)
    if jeu=="factorielle":
        return jeu_factorielle()
    elif jeu=="roulette_mathematique":
        return roulette_mathematique()
    elif jeu=="equation":
        return epreuve_math_equation()

def choisir_joueur(equipe):
    candidat=""
    while candidat not in equipe:
        message="choisissez un candidat parmi "+ str(equipe) + " : "
        candidat=input(message)
    return candidat


def epreuve_finale(equipe_numero, equipe):
    score_incrementation(equipe)
    print(equipe_numero, "a gagné !")

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

