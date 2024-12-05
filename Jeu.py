from Fonctions_utiles import *
from fenetre_graphique import *
import pygame
from pygame.locals import *
from pygame import *
import pygame.locals

print(test)
print(leader_board())

pygame.init()
ecran = fenetre_graphique.ecran
boyard = pygame.image.load('Assets/img.png')
boyard = pygame.transform.scale(boyard, ecran.get_size())
ecran.blit(boyard, (0, 0))
pygame.display.flip()

screen_size = pygame.display.get_surface().get_size()
print(screen_size)

fenetre="Menu"

clé_equipe1 = 0
clé_equipe2 = 0

continuer=True

while continuer:

    play_bouton = creer_bouton(int(8*screen_size[0]/10), int(screen_size[1] / 4), 200, 100, ecran, "play")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False
                pygame.quit()

    pygame.display.flip()

    if fenetre=="Menu":
        ecran.blit(boyard, (0, 0))
        if clique_bouton(play_bouton):
            fenetre = "nbEquipes"

    if fenetre == "nbEquipes":

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


