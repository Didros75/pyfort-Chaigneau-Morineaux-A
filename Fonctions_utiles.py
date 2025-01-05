""" Dans ce module, nous allons mettre les fonctions utiles au deroulement de notre programme"""
import pygame.time


from epreuves_mathematiques import *
from epreuves_hasard import *
from epreuves_logiques import *
from enigme_pere_fouras import *
from epreuve_finale import *
import json

#initialisation des fonds et reference a l'ecran present dans fenetre graphique
Menu_neutre2=pygame.image.load('Assets/document_0.jpg')
Menu_neutre2=pygame.transform.scale(Menu_neutre2, ecran.get_size())
ecran = fenetre_graphique.ecran

def introduction():
    "introduction, qui s'affiche dans le menu"
    afficher_texte(ecran, "Bienvenue sur PYFORT !", 50, (200, 100))
    afficher_texte(ecran, "Constituez deux equipes de 1 a 3 joueurs ", 40, (200, 230))
    afficher_texte(ecran, "et affrontez vous dans une serie de mini", 40,(200, 280))
    afficher_texte(ecran, "jeux dans le but de gagner des clés et", 40, (200, 330))
    afficher_texte(ecran, "d'accéder a la salle du tresor !", 40, (200, 380))

def Menu():
    "Menu qui se lance au debut du jeu et nous permet de choisir entre Jeu Leaderboard et Quitter"
    ecran.blit(Menu_neutre, (0, 0))
    introduction()
    choix = choix_multiple(["Jouer", "Leaderboard", "Quitter"])

    if choix == 1:
        return "Equipe"

    elif choix == 2:

        page = 0
        afficher_leaderboard(0)
        choix = choix_multiple(["Precedent", "Retour", "Suivant"])
        while choix != 2:
            if choix == 1:
                page -= 1
                page = afficher_leaderboard(page)
                choix = choix_multiple(["Precedent", "Retour", "Suivant"])
            elif choix == 3:
                page += 1
                page = afficher_leaderboard(page)
                choix = choix_multiple(["Precedent", "Retour", "Suivant"])
        if choix == 2:
            return "Menu"
    elif choix == 3:
        pygame.quit()

def composer_equipe():
    "sert à composer les equipes ; demande combien de joueurs par equipe puis demande nom et prenoms en verifiant s'ils sont deja dans la base de donée. Return 2 listes ; equipe 1 et 2"
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)

    liste_player=[]

    nbJoueurs=0
    while nbJoueurs == 0:
        nbJoueurs=choix_multiple(["1 joueur", "2 joueurs", "3 joueurs"])
    ecran.blit(Menu_neutre2, (0, 0))
    e1=[]
    e2=[]
    #l'interface graphique ne dépend pas de la résolution de l'écran donc peux être décalée sur certain ordinateurs
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
        #on cherche ici s'ils sont dans le Json
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
    "Fonction très importante : elle est appelée dans Main, demande de choisir une catégorie, et appelle un jeu au hasard dans cette catégorie. Il va alors tout simplement retourner le mini jeu, car ce dernier retourne deja True ou False en fonction de si le joueur a gagné ou perdu"
    liste_catgories = ["Maths", "Hasard", "Logique", "Enigme"]
    liste_mini_jeux_maths = ["factorielle", "roulette_mathematique", "equation"]
    liste_mini_jeux_hasard = ["Bonneteau", "dés"]
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
    "choisir le joueur d'une equipe entrée en paramètre et return le candidat choisi"
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


def epreuve_finale():
    "lance l'epreuve finale "
    return salle_De_Tresor()

def score_incrementation(equipe):
    "donne un point a chaque memebre de l'equipe qui a gagné"
    with open('players_sauvegarde.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    for personne in donnees:
        for player in equipe:
            if personne["Prenom"] == player:
                personne["Score"]=personne["Score"]+1
    with open('players_sauvegarde.json', 'w', encoding='utf-8') as f:
        json.dump(donnees, f)


def leader_board():
    "algorithme de tri permetant de renvoyer la liste triée des joueurs"
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
            name_score=(best_player, best_score)
            leader_board_liste.append(name_score)
            donnees.pop(best_index)
    return leader_board_liste

def afficher_leaderboard(page):
    "affiche la page du leaderboard"
    liste = leader_board()
    if page < 0:
        page = len(liste)//5
    elif page > len(liste)//5:
        page=0

    ecran.blit(Menu_neutre2, (0, 0))
    afficher_texte(ecran, "Joueurs :", 50, (300, 200))
    afficher_texte(ecran, "Score :", 50, (600, 200))
    max=5
    for i in range(5*page, len(liste)):
        if max>0:
            afficher_texte(ecran, liste[i][0], 30, (300, 240 + ((i-(5*page)+1)*30)))
            afficher_texte(ecran, str(liste[i][1]), 30, (600, 240 + ((i-(5*page) + 1) * 30)))
            max-=1
    return page

def supprimer_sauvegarde():
    "cette fonction n'est pas disponible en jeu, elle est la pour clear la sauvegarde en raison des nombreux tests effectués"
    with open('players_sauvegarde.json', 'w', encoding='utf-8') as f:
        json.dump([], f)

