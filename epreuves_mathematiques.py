import random
import fenetre_graphique
from fenetre_graphique import *
ecran = fenetre_graphique.ecran
position_reponses=((200, 300),(300, 50))

def jeu_factorielle():
    """Pour le jeu factorielle, on prend un nombre aléatoire et on calcule la factorielle par recursivité, puis on demande au joeueur d'entrer une valeur, et on renvoie True si il a bon, False sinon"""

    n = random.randint(1, 10)
    facto = factorielle(n)
    message="Factoriel de " + str(n) + " ? "
    afficher_texte(ecran, message, 24, ((200, 200),(200, 200)))
    return facto == entrer_texte(ecran, position_reponses, 24)

def factorielle(n):
    if n == 1:
        return 1
    else:
        return n * factorielle(n - 1)



def roulette_mathematique():
    """Pour le jeu de la roulette mathematique, on selectionne 5 nombres aléatoires, puis on operation et on retourne True ou False si la reponse du joueur est bonne ou pas"""

    liste=[]
    operations=["+", "-", "*"]
    for i in range(5):
        liste.append(random.randint(1, 20))
    operation_choisie=random.choice(operations)
    if operation_choisie == "+":
        message=str(liste)+"\nCalculez le résultat en combinant ces nombres avec une addition "
        afficher_texte(ecran, message, 24, ((200, 200), (200, 200)))
        return sum(liste)==entrer_texte(ecran, ((300, 200),(200, 200)), 24)
    elif operation_choisie == "-":
        diff=liste[0]
        for i in range(1, len(liste)):
            diff-=liste[i]
        message = str(liste) + "\nCalculez le résultat en combinant ces nombres avec une soustaction "
        afficher_texte(ecran, message, 24, ((200, 200), (200, 200)))
        return diff == entrer_texte(ecran, position_reponses, 24)
    elif operation_choisie == "*":
        mult = liste[0]
        for i in range(1, len(liste)):
            mult *= liste[i]
        message = str(liste) + "\nCalculez le résultat en combinant ces nombres avec une multiplication "
        afficher_texte(ecran, message, 24, ((200, 200), (200, 200)))
        return mult == entrer_texte(ecran, position_reponses, 24)



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
    list=resoudre_equation_lineaire()
    resultat=arrondir(list[2])
    print(resultat)
    message="Resolvez l'equation "+ str(list[0]) +"x + "+ str(list[1]) + " (arrondi a la première decimale) : "
    afficher_texte(ecran, message, 24, ((200, 200), (200, 200)))
    return str(resultat) == entrer_texte(ecran, position_reponses, 24)
