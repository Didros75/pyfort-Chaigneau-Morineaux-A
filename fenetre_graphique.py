"""Ici se trouvent toutes les fonctions utiles a l'affichage graphique ; on va retrouver l'equivalent du print du input et bien d'autre"""
import pygame



ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
bouton_petit=pygame.image.load('Assets/bouton_petit.png')
bouton_petit=pygame.transform.scale(bouton_petit, (200, 100))

Menu_neutre=pygame.image.load('Assets/document_0.jpg')
Menu_neutre=pygame.transform.scale(Menu_neutre, ecran.get_size())

fenetre="Menu"

def afficher_texte(ecran, texte, taille, position):
    "fonction simple, mais vitale : elle prend en paramètre un texte, une taille de texte et enfin la position sur l'ecran. On aurait pu rajouter la couleur et la police mais on a préféré garder quelque chose de simple. Le parametre ecran est simplement la pour designer la fenetre où afficher. "
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    message = font.render(texte, True, "White")
    ecran.blit(message, position)
    pygame.display.update()


def choix_multiple(textes):
    "Cette fonction est plus complexe ; elle prend en paramatre une liste de chaines de caracteres, et va ensuite creer un bouton pour chacun de ces textes. Enfin, elle va renvoyer le numero du bouton choisi. La fonction permet par exemple de choisir le joueur, ou la catégorie."
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                i = 0
                for bouton in boutons:
                    if clique_bouton(bouton):
                        return i + 1
                    i += 1

        pygame.display.update()


def entrer_texte(ecran, rect, taille):
    "cette fonction fait office d'input ; elle crée un rectangle noir dans lequel le joueur va pouvoir entrer et supprimer du texte. Quand ce dernier appuira sur entrée, la fonction va return le texte. Elle prend en parametre une zone de texte et la taille d'ecriture"
    pygame.init()
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    user_input_value = ""
    user_input_rect = pygame.Rect(rect)
    background_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input_value
                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    user_input_value += event.unicode


            pygame.draw.rect(ecran, background_color, user_input_rect)


            user_input = font.render(user_input_value, True, "White")
            ecran.blit(user_input, user_input_rect)


            pygame.display.update()


def afficher_batons_graphique(ecran, nb_batons):
    "cette fonction est utilisée uniquement dans l'affichage des batons du jeu de Nim. Elle separe l'exan en 20, et affiche le nombre de batons demandés en parametres"
    ecran.blit(Menu_neutre, (0, 0))
    screen_width = ecran.get_width()-50
    screen_height = ecran.get_height()
    for i in range(nb_batons):
        pygame.draw.line(ecran, "black", (50 + i * screen_width // 19, screen_height // 2 + 100),
                         (50 + i * screen_width // 19, screen_height // 2 - 100), 10)

        pygame.display.update()

def creer_bouton(x, y, largeur, hauteur, surface, texte):
    "permet comme son nom l'indique de creer un bouton. Le bouton a des coordonées x et y, une taille et un texte, tous donnés en paramètre, et va return un rect, c'est a dire un rectagle"
    rect = pygame.Rect(x, y, largeur, hauteur)
    surface.blit(bouton_petit, (x, y))
    font = pygame.font.Font(None, 36)
    texte_surface = font.render(texte, True, (255, 255, 255))  # Blanc
    texte_rect = texte_surface.get_rect(center=rect.center)
    surface.blit(texte_surface, texte_rect)
    return rect

def clique_bouton(bouton):
    "Renvoie true si on clique sur un bouton demandé en paramètre"
    mouse_pos = pygame.mouse.get_pos()
    return bouton.collidepoint(mouse_pos)
