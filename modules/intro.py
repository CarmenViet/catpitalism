import pygame
from modules.images import *

def show_intro_screen(screen, clock, settings):
    intro_screen_image = get_image(intro_screen_file_name, (settings["width"], settings["height"]))
    screen.blit(intro_screen_image, (0, 0))
    pygame.display.update()
    user_has_clicked = False
    while user_has_clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if (settings["width"]*0.2 < click[0] and click[0] < settings["width"]*0.74) and (settings["height"]*0.565 < click[1] and click[1] < settings["height"]*0.84):
                    user_has_clicked = True
            if event.type == pygame.QUIT:
                pygame.quit()
    clock.tick(60)