import pygame

ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

fenetre="Menu"

def afficher_texte(ecran, texte, taille, rect):
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    ecran.blit(texte, rect)
    pygame.display.update()

def entrer_texte(ecran, rect, taille):
    font = pygame.font.SysFont('Comic Sans MS,Arial', taille)
    user_input_value = ""
    user_input = font.render(user_input_value, True, "White")
    user_input_rect = rect

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    print(user_input_value)
                    return user_input_value
                    break
                elif event.key == pygame.K_BACKSPACE:
                    user_input_value = user_input_value[:-1]
                else:
                    user_input_value += event.unicode
            ecran.fill((0,0,0))
            ecran.blit(user_input, user_input_rect)
            pygame.display.update()
            user_input = font.render(user_input_value, True, "White")
            user_input_rect = rect


def creer_bouton(x, y, taille_x, taille_y, ecran):
    Rect=pygame.Rect(x, y, taille_x, taille_y)
    pygame.draw.rect(ecran, pygame.Color('black'), Rect)
    return Rect

def clique_bouton(bouton):
    mouse_pos = pygame.mouse.get_pos()
    mouse_rect_size = 8
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_rect_size, mouse_rect_size)
    return pygame.Rect.colliderect(mouse_rect, bouton)


