from Fonctions_utiles import *

introduction()

def jeu():



    equipes = composer_equipe()
    equipe1 = equipes[0]
    equipe2 = equipes[1]

    clé_equipe1 = 0
    clé_equipe2 = 0

    while True:
        print("Equipe 1, a toi de jouer")
        candidat=choisir_joueur(equipe1)
        print("A", candidat, "de jouer")
        if menu_epreuves():
            clé_equipe1+=1
            print("Vous avez gagné une clé ! Vous avez", clé_equipe1, "clés !")
        else:
            print("Dommage")

        if clé_equipe1==3:
            epreuve_finale("equipe1", equipe1)
            break

        print("Equipe 2, a toi de jouer")
        candidat=choisir_joueur(equipe2)
        print("A", candidat, "de jouer")
        if menu_epreuves():
            clé_equipe2 += 1
            print("Vous avez gagné une clé ! Vous avez", clé_equipe2, "clés !")
        else:
            print("Dommage")

        if clé_equipe2==3:
            epreuve_finale("equipe2", equipe2)
            break


jeu()
print(leader_board())