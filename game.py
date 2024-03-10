import pygame
import json
from modules.images import *

json_file = open('settings.json')
data = json.load(json_file)

def settings_popup(screen, clock):
    while True:
        screen.blit(intro_screen, (90, 0))
        screen.blit(box, (250, 100))
        screen.blit(box, (250, 300))
        screen.blit(box, (250, 500))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                print(click) 
                if 251 < click[0] and click[0] < 800 and 100 < click[1] and click[1] < 230:
                    screen = pygame.display.set_mode((20, 24))
                if 251 < click[0] and click[0] < 800 and 300 < click[1] and click[1] < 430:
                    print("blueberry")
                if 251 < click[0] and click[0] < 800 and 500 < click[1] and click[1] < 630:
                    print("godzilla")
        pygame.display.update()
        clock.tick(60)

def show_game(screen, clock):
    settings_screen = False
    print("blue")
    game = True
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                print(click)
                if 60 > click[0] and click[0] > 0 and 60 > click[1] and click[1] > 0:
                    settings_screen = True
                    if settings_screen == True:
                        screen.blit(intro_screen, (420, 0))
                        settings_popup(screen, clock)

     
        screen.blit(intro_screen, (50, 0))
        screen.blit(settings, (0, 0))

        pygame.display.update()
        clock.tick(60)
