import pygame

pygame.init()
ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

boyard=pygame.image.load('Assets/img.png')
boyard=pygame.transform.scale(boyard, ecran.get_size())

fenetre="Menu"

ecran.blit(boyard, (0, 0))
pygame.display.flip()

def creer_bouton(x, y, taille_x, taille_y, ecran):
    Rect=pygame.Rect(x, y, taille_x, taille_y)
    pygame.draw.rect(ecran, pygame.Color('black'), Rect)
    return Rect

def cliqe_bouton(bouton):
    mouse_pos = pygame.mouse.get_pos()
    mouse_rect_size = 8
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], mouse_rect_size, mouse_rect_size)
    return pygame.Rect.colliderect(mouse_rect, bouton)


while True:

    play_bouton=creer_bouton(0, 0, 800, 800, ecran)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:

                if fenetre == "Menu":
                    print(cliqe_bouton(play_bouton))


    pygame.display.flip()