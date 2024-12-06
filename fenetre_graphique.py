import pygame



ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
boyard2=pygame.image.load('Assets/img.png')
boyard2 = pygame.transform.scale(boyard2, ecran.get_size())
bouton_petit=pygame.image.load('Assets/bouton_petit.png')

fenetre="Menu"

def afficher_texte(ecran, texte, taille, position):
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    message = font.render(texte, True, "White")
    ecran.blit(message, position)
    pygame.display.update()


def choix_multiple(textes):

    screen_size = pygame.display.get_surface().get_size()
    largeur_ecran = screen_size[0]
    hauteur_ecran = screen_size[1]


    n = len(textes)
    espacement = largeur_ecran // (n + 1)
    y_position = int(4 * hauteur_ecran / 6)


    boutons = []
    for i, texte in enumerate(textes):
        x_position = espacement * (i + 1) - 100
        bouton = creer_bouton(x_position, y_position, 200, 100, ecran, texte)
        boutons.append(bouton)

    pygame.display.flip()

    while True:
        for i, bouton in enumerate(boutons):
            if clique_bouton(bouton):
                return i + 1


def entrer_texte(ecran, rect, taille):
    pygame.init()
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    user_input_value = ""
    user_input_rect = pygame.Rect(rect)
    background_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    print(user_input_value)
                    return user_input_value
                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    user_input_value += event.unicode


            pygame.draw.rect(ecran, background_color, user_input_rect)


            user_input = font.render(user_input_value, True, "White")
            ecran.blit(user_input, user_input_rect)


            pygame.display.update()


def creer_bouton(x, y, taille_x, taille_y, ecran, texte, taille_police=30, couleur_bouton="black",couleur_texte="white"):

    Rect = pygame.Rect(x, y, taille_x, taille_y)


    if texte:
        font = pygame.font.SysFont('Comic Sans MS,Arial', taille_police)
        texte_rendu = font.render(texte, True, couleur_texte)


        texte_rect = texte_rendu.get_rect(center=Rect.center)
        ecran.blit(texte_rendu, texte_rect)

    return Rect

def clique_bouton(bouton):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton.collidepoint(event.pos):
                return True

