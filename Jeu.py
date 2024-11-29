from Fonctions_utiles import *
from fenetre_graphique import *
import pygame
from pygame.locals import *
from pygame import *
import pygame.locals

pygame.init()
ecran = fenetre_graphique.ecran
boyard = pygame.image.load('Assets/img.png')
boyard = pygame.transform.scale(boyard, ecran.get_size())
ecran.blit(boyard, (0, 0))
pygame.display.flip()

screen_size = pygame.display.get_surface().get_size()

fenetre="Menu"

clé_equipe1 = 0
clé_equipe2 = 0

continuer=True

while continuer:

    play_bouton = creer_bouton(int(screen_size[0] / 2 - 50), int(screen_size[1] / 2 - 50), 100, 100, ecran)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:

                if fenetre == "Menu":
                    if clique_bouton(play_bouton):
                        fenetre="nbEquipes"

    pygame.display.flip()

    if fenetre=="Menu":
        ecran.blit(boyard, (0, 0))

    if fenetre == "nbEquipes":

        ecran.fill(pygame.Color('Black'))
        pygame.display.flip()
        fenetre="play"

    if fenetre=="Play":
        equipes=composer_equipe()
        equipe1 = equipes[0]
        equipe2 = equipes[1]
        afficher_texte(ecran, "Equipe1, a toi de jouer", 24, ((200, 200), (200, 200)))
        candidat = choisir_joueur(equipe1)
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


