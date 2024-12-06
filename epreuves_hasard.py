import random


def jeu_lance_des():
    nb_essai=3
    des=[1,2,3,4,5,6]
    while nb_essai>0:
        message="le nombre d'essais restant est "+str(nb_essai)
        print(message)
        print("lancez les dés en pressant la touche entrée")
        input()
        de_joueur = (random.choice(des), random.choice(des))
        print(de_joueur)
        if de_joueur[0]==6 or de_joueur[1]==6:
            print("vous avez gagnez une clé")
            return True
        message="c'est au tour du maître du jeu"
        print(message)
        de_maitre = (random.choice(des), random.choice(des))
        print(de_maitre)
        if de_joueur[0]==6 or de_joueur[1]==6:
            print("Le maître du jeu a remporté la partie")
            return False
        print("Aucun 6 n'est obtenu, on passe au prochain essai")
        nb_essai -= 1
    print("Aucun joueur n'a obtenu 6 après trois essais, c'est match nul")
    return False

def bonneteau():
    liste=["A","B","C"]
    nb_tentatives=2
    print("Vous devez deviner sous quel Bonneteau ce trouve la clé et pour cela vous avez deux essais")
    print("A","B","C")
    for i in range(2):
        print("il vous reste ", nb_tentatives, " tentatives")
        lettre=random.choice(liste)
        Bonneteau_choisi=input("choisissez un Bonneteau A, B ou C")
        if Bonneteau_choisi==lettre:
            print("Bravo la clé est sous le Bonneteau")
            return True
        else:
            print("Vous n'avez pas réussi cette tentative")
        nb_tentatives-=1
    print("Vous avez perdu")
    return False
