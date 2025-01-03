import random
import fenetre_graphique
from fenetre_graphique import *
import pygame
ecran = fenetre_graphique.ecran
position_reponses=((120, 480),(300, 50))
Menu_maths=pygame.image.load('Assets/Maths_willy.jpg')
Menu_maths = pygame.transform.scale(Menu_maths, ecran.get_size())

def jeu_factorielle():
    """Pour le jeu factorielle, on prend un nombre aléatoire et on calcule la factorielle par recursivité, puis on demande au joeueur d'entrer une valeur, et on renvoie True si il a bon, False sinon"""
    ecran.blit(Menu_maths,(0,0))
    pygame.display.flip()
    n = random.randint(1, 10)
    facto = factorielle(n)
    message="Factoriel de " + str(n) + " ? "
    afficher_texte(ecran, "Question :", 40, ((150, 200), (200, 200)))
    afficher_texte(ecran, message, 24, ((150, 300),(200, 200)))
    return str(facto) == entrer_texte(ecran, position_reponses, 24)

def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)



def roulette_mathematique():
    """Pour le jeu de la roulette mathematique, on selectionne 5 nombres aléatoires, puis on operation et on retourne True ou False si la reponse du joueur est bonne ou pas"""
    ecran.blit(Menu_maths, (0, 0))
    pygame.display.flip()
    liste=[]
    operations=["+", "-", "*"]
    for i in range(5):
        liste.append(random.randint(1, 20))
    operation_choisie=random.choice(operations)
    afficher_texte(ecran, "Question :", 40, ((150, 200), (200, 200)))
    if operation_choisie == "+":
        add=0
        for i in liste:
            add+=i
        message=str(liste)
        message=message[1:-1]
        afficher_texte(ecran, message, 30, ((150, 270), (200, 200)))
        afficher_texte(ecran, "Calculez le résultat en combinant ces nombres avec une addition ", 30, ((150, 320), (200, 200)))
        return str(add)==entrer_texte(ecran, position_reponses, 24)
    elif operation_choisie == "-":
        diff=liste[0]
        for i in range(1, len(liste)):
            diff-=liste[i]
        message = str(liste)
        message = message[1:-1]
        afficher_texte(ecran, message, 30, ((150, 270), (200, 200)))
        afficher_texte(ecran, "Calculez le résultat en combinant ces nombres avec une soustraction ", 30,
                       ((150, 320), (200, 200)))
        return str(diff) == entrer_texte(ecran, position_reponses, 24)
    elif operation_choisie == "*":
        mult = liste[0]
        for i in range(1, len(liste)):
            mult *= liste[i]
        message = str(liste)
        message = message[1:-1]
        afficher_texte(ecran, message, 30, ((150, 270), (200, 200)))
        afficher_texte(ecran, "Calculez le résultat en combinant ces nombres avec une multiplication ", 30,
                       ((150, 300), (220, 200)))
        return str(mult) == entrer_texte(ecran, position_reponses, 24)



def  resoudre_equation_lineaire():
    """Pour le jeu de l'equation, on prend un nombre a et b entre -10 et 10, on resoud l'equation puis on l'arrondi et on renvoie True ou False en fonction de l'entrée du joueur"""

    nombres_possibles = list(range(-10, 11))
    nombres_possibles.remove(0)
    a=random.choice(nombres_possibles)
    b=random.choice(nombres_possibles)
    return a, b, -b/a

def arrondir(nombre):
    if nombre.is_integer():
        return round(nombre)
    else:
        return round(nombre, 1)

def epreuve_math_equation():
    ecran.blit(Menu_maths, (0, 0))
    pygame.display.flip()
    list=resoudre_equation_lineaire()
    resultat=arrondir(list[2])
    print(resultat)
    afficher_texte(ecran, "Question :", 40, ((150, 200), (200, 200)))
    message="Resolvez l'equation "+ str(list[0]) +"x + "+ str(list[1]) + " (arrondi a la première decimale) : "
    afficher_texte(ecran, message, 24, ((150, 300), (200, 200)))
    return str(resultat) == entrer_texte(ecran, position_reponses, 24)
