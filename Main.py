import time

from Fonctions_utiles import *
from fenetre_graphique import *
import pygame
from pygame.locals import *
from pygame import *
import pygame.locals


print(leader_board())

pygame.mixer.init()
son = pygame.mixer.Sound('Assets/fort-boyard_orchestre-symphonique-police.mp3')
son.play(loops=-1, maxtime=0, fade_ms=0)

pygame.init()
ecran = fenetre_graphique.ecran
boyard = pygame.image.load('Assets/Menu.jpg')
boyard = pygame.transform.scale(boyard, ecran.get_size())
Menu_equipe = pygame.image.load('Assets/Menu_equipe.jpg')
Menu_equipe = pygame.transform.scale(Menu_equipe, ecran.get_size())
Menu_nb_equipe = pygame.image.load('Assets/nb_equipe.jpg')
Menu_nb_equipe = pygame.transform.scale(Menu_nb_equipe, ecran.get_size())
ecran.blit(boyard, (0, 0))
pygame.display.flip()

screen_size = pygame.display.get_surface().get_size()
print(screen_size)

fenetre="Menu"

clé_equipe1 = 0
clé_equipe2 = 0

continuer=True

while continuer:

    play_bouton = creer_bouton(int(8*screen_size[0]/10), int(screen_size[1] / 4), 200, 100, ecran, "")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()

    pygame.display.flip()

    if fenetre=="Menu":
        ecran.blit(boyard, (0, 0))
        choix=0

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clique_bouton(play_bouton):
                    fenetre = "nbEquipes"

    if fenetre == "nbEquipes":
        ecran.blit(Menu_nb_equipe, (0, 0))
        equipes = composer_equipe()
        equipe1 = equipes[0]
        equipe2 = equipes[1]
        fenetre="Play"

    if fenetre=="Play":
        ecran.blit(boyard, (0, 0))
        afficher_texte(ecran, "Equipe 1, a toi de jouer", 24, ((100, 200), (200, 200)))
        candidat="^"
        while candidat=="^":
            candidat = choisir_joueur(equipe1)

        ecran.blit(boyard, (0, 0))
        message="A "+ str(candidat) + " de jouer"
        afficher_texte(ecran, message, 24, ((100, 250), (200, 200)))

        if menu_epreuves() == True:
            clé_equipe1+=1
            print(clé_equipe1)
            message="Vous avez gagné une clé ! Vous avez "+ str(clé_equipe1)+ " clés !"
            afficher_texte(ecran, message, 24, ((300, 200), (200, 200)))

        else:
            afficher_texte(ecran, "Dommage", 24, ((300, 200), (200, 200)))
            print("dommage")


        if clé_equipe1==3:
            epreuve_finale("equipe1", equipe1)
            break

        ecran.blit(boyard, (0, 0))
        afficher_texte(ecran, "Equipe 2, a toi de jouer", 24, ((100, 200), (200, 200)))
        candidat = "^"
        while candidat == "^":
            candidat = choisir_joueur(equipe2)

        ecran.blit(boyard, (0, 0))
        message = "A " + str(candidat) + " de jouer"
        afficher_texte(ecran, message, 24, ((100, 250), (200, 200)))

        if menu_epreuves():
            clé_equipe2 += 1
            message = "Vous avez gagné une clé ! Vous avez " + str(clé_equipe2) + " clés !"
            afficher_texte(ecran, message, 24, ((300, 200), (200, 200)))

        else:
            afficher_texte(ecran, "Dommage", 24, ((300, 200), (200, 200)))

        if clé_equipe2==3:
            epreuve_finale("equipe2", equipe2)
            break


