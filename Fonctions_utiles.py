""" Dans ce module, nous allons mettre les fonctions utiles au deroulement de notre programme"""
import fenetre_graphique
from fenetre_graphique import *
from epreuves_mathematiques import *
from epreuves_hasard import *
import json

boyard_fond=pygame.image.load('Assets/img.png')
boyard_fond = pygame.transform.scale(boyard_fond, ecran.get_size())
Menu_equipe = pygame.image.load('Assets/Menu_equipe.jpg')
Menu_equipe = pygame.transform.scale(Menu_equipe, ecran.get_size())
Menu_nb_equipe = pygame.image.load('Assets/nb_equipe.jpg')
Menu_nb_equipe = pygame.transform.scale(Menu_nb_equipe, ecran.get_size())
ecran = fenetre_graphique.ecran

def introduction():
    print("Bienvenue sur Fort Boyard Simulator ! \n Constituez deux equipes de 1 a 3 joueurs et affrontez vous dans une serie de mini jeux dans le but de gagner des clés et d'acceder a la salle du tresor !")

def composer_equipe():
    ecran.blit(Menu_nb_equipe, (0, 0))
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)

    liste_player=[]

    nbJoueurs=0
    while nbJoueurs == 0:
        nbJoueurs=choix_multiple(["1 joueur", "2 joueurs", "3 joueurs"])
    ecran.blit(Menu_equipe, (0, 0))

    for i in range(nbJoueurs*2):
        if i<nbJoueurs:
            afficher_texte(ecran, "Equipe1", 24, ((200, 100), (300, 70)))
        else:
            ecran.blit(Menu_equipe, (0, 0))
            afficher_texte(ecran, "Equipe2", 24, ((200, 100), (300, 70)))


        afficher_texte(ecran, "Prenom", 24, ((100, 200), (300, 70)))
        prenom = entrer_texte(ecran, ((200, 200), (300, 50)), 24)
        afficher_texte(ecran, "Nom", 24, ((100, 300), (300, 70)))
        nom = entrer_texte(ecran, ((200, 300), (300, 50)), 24)

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
    liste_mini_jeux_hasard = ["dés","Bonneteau"]
    categorie=""
    jeu=""
    message="Choisis une catégorie parmis " + str(liste_catgories) + " : "

    while categorie == "":
        afficher_texte(ecran, message, 24, ((200, 550), (300, 70)))
        categorie=liste_catgories[choix_multiple(liste_catgories)-1]

    ecran.blit(boyard_fond, (0, 0))

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

def choisir_joueur(equipe):
    candidat="^"
    afficher_texte(ecran, "Choisir le joueur parmis " + str(equipe), 30, ((400, 400),(300, 300)))
    while candidat == "^":

        if len(equipe)==1:
            candidat=choix_multiple([equipe[0]])
        elif len(equipe)==2:
            candidat=choix_multiple([equipe[0], equipe[1]])
        else:
            candidat = choix_multiple([equipe[0], equipe[1], equipe[2]])
    return equipe[candidat-1]


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

