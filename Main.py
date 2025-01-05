"""Voici la boucle principale du jeu : elle ne contient pas de fonction et se contente de les appeler"""

from Fonctions_utiles import *
from fenetre_graphique import *

import pygame.locals



pygame.mixer.init()
son = pygame.mixer.Sound('Assets/fort-boyard_orchestre-symphonique-police.mp3')
son.play(loops=-1, maxtime=0, fade_ms=0)

pygame.init()
ecran = fenetre_graphique.ecran

Menu_neutre=pygame.image.load('Assets/document_0.jpg')
Menu_neutre=pygame.transform.scale(Menu_neutre, ecran.get_size())



pygame.display.flip()

screen_size = pygame.display.get_surface().get_size()
fenetre="Menu"

continuer=True

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()

    pygame.display.flip()

    if fenetre=="Menu":
        #ici on lance le menu, qui va renvoyer soit a la creation d'equipe soit au leaderboard
        fenetre=Menu()

    if fenetre=="Equipe":

        ecran.blit(Menu_neutre, (0, 0))
        afficher_texte(ecran, "Choisir le nombre de joueur par équipe :", 40, (220, 430))

        #on appelle ici la fonction pour creer les equipes
        equipes = composer_equipe()
        equipe1 = equipes[0]
        equipe2 = equipes[1]
        clé_equipe1=0
        clé_equipe2=0
        fenetre="Play"

    if fenetre=="Play":
        #Le jeu commence ! On commence par choisir un candidat dans la premiere equipe pour jouer

        ecran.blit(Menu_neutre, (0, 0))
        afficher_texte(ecran, "Equipe 1, a toi de jouer", 50, ((100, 100), (200, 200)))
        candidat="^"
        while candidat=="^":
            candidat = choisir_joueur(equipe1)

        ecran.blit(Menu_neutre, (0, 0))
        message="A "+ str(candidat) + " de jouer"
        afficher_texte(ecran, message, 50, ((100, 100), (200, 200)))

        if menu_epreuves() == True:
            #cette simple condition permet d'appeler menu_epreuve qui appelera a son tour une epreuve et viendra retourner True ou False ici.
            ecran.blit(Menu_neutre, (0, 0))
            #on augmente le nombre de clés de l'equipe
            clé_equipe1+=1
            message="Vous avez gagné une clé ! Vous avez "+ str(clé_equipe1)+ " clés !"
            afficher_texte(ecran, message, 50, ((100, 100), (200, 200)))
            pygame.display.flip()
            #on attend pour rendre lisible le jeu
            pygame.time.wait(2500)

        else:
            ecran.blit(Menu_neutre, (0, 0))
            afficher_texte(ecran, "Dommage", 50, ((100, 100), (200, 200)))
            pygame.display.flip()
            pygame.time.wait(2500)


        if clé_equipe1==3:
            #si l'equipe a 3 clés, on lance l'epeuve finale
            ecran.blit(Menu_neutre, (0, 0))

            if epreuve_finale():
                ecran.blit(Menu_neutre, (0, 0))
                afficher_texte(ecran, "Victoire de l'equipe 1 !", 70, ((100, 100), (200, 200)))
                score_incrementation("equipe1")
            else :
                ecran.blit(Menu_neutre, (0, 0))
                afficher_texte(ecran, "Dommage", 70, ((100, 100), (200, 200)))
            pygame.time.wait(2500)
            fenetre="Menu"

        #et rebelotte avec l'equipe 2, meme principe
        if fenetre == "Play": #ici on re verifie si le joueur 1 n'as pas gagné car sinon ca finirait la boucle
            ecran.blit(Menu_neutre, (0, 0))
            afficher_texte(ecran, "Equipe 2, a toi de jouer", 50, ((100, 100), (200, 200)))
            candidat = "^"
            while candidat == "^":
                candidat = choisir_joueur(equipe2)

            ecran.blit(Menu_neutre, (0, 0))
            message = "A " + str(candidat) + " de jouer"
            afficher_texte(ecran, message, 50, ((100, 100), (200, 200)))

            if menu_epreuves() == True:
                ecran.blit(Menu_neutre, (0, 0))
                clé_equipe2 += 1
                message = "Vous avez gagné une clé ! Vous avez " + str(clé_equipe2) + " clés !"
                afficher_texte(ecran, message, 50, ((100, 100), (200, 200)))
                pygame.display.flip()
                pygame.time.wait(2500)

            else:
                ecran.blit(Menu_neutre, (0, 0))
                afficher_texte(ecran, "Dommage", 50, ((100, 100), (200, 200)))
                pygame.display.flip()
                pygame.time.wait(2500)

            if clé_equipe2==3:

                ecran.blit(Menu_neutre, (0, 0))

                if epreuve_finale():
                    ecran.blit(Menu_neutre, (0, 0))
                    afficher_texte(ecran, "Victoire de l'equipe 2 !", 70, ((100, 100), (200, 200)))
                    score_incrementation("equipe2")
                else:
                    ecran.blit(Menu_neutre, (0, 0))
                    afficher_texte(ecran, "Dommage", 70, ((100, 100), (200, 200)))
                pygame.time.wait(2500)
                fenetre="Menu"

            #quand l'equipe 2 a joué, la boucle recommence si aucune equipe n'as 3 clés