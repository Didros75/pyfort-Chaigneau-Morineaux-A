import json
import random
import fenetre_graphique
import pygame

from fenetre_graphique import afficher_texte, entrer_texte

ecran = fenetre_graphique.ecran
Menu_enigme = pygame.image.load('Assets/Enigmes.jpg')
Menu_enigme = pygame.transform.scale(Menu_enigme, ecran.get_size())


def charger_enigmes():
    with open('enigmesPF.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)
        return donnees

def enigme_pere_fouras():
    ecran.blit(Menu_enigme, (0, 0))
    pygame.display.flip()
    donnees=charger_enigmes()
    nb_essais=3
    liste=[]
    for i in donnees:
        liste.append(i["question"])
    enigme=random.choice(liste)
    for i in donnees:
        if i["question"] == enigme:
            reponse=i["reponse"].lower()
    enigme_coupée = enigme.split("\n")
    j=0
    for i in enigme_coupée:
        afficher_texte(ecran, i, 30, (120, 230+j*50))
        j+=1
    while nb_essais>0:
        utilisateur_rep=entrer_texte(ecran, ((120, 595),(300, 50)), 30).lower()
        if utilisateur_rep in reponse:
            print("vous avez gagner une clé")
            return True
        else:
            nb_essais-=1
            if nb_essais>0:
                print("La réponse est incorrecte, il vous reste", nb_essais)
            else:
                print("Vous avez échoué à l'énigme la solution était: ", reponse)
                return False