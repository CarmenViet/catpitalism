import pygame
import json
from modules.images import *

json_file = open('settings.json')
data = json.load(json_file)
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)
money_texty = my_font.render(('money amount: '), False, (0, 0, 0))
head = my_font.render(('click on my head for coins'), False, (0, 0, 0))

def settings_popup(screen, clock):
    switch = True
    while switch == True:
        screen.blit(intro_screen, (0, 0))
        screen.blit(two, (250, 100))
        screen.blit(three, (250, 300))
        screen.blit(one, (250, 500))
        screen.blit(leave, (850, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                print(click) 
                if 251 < click[0] and click[0] < 800 and 100 < click[1] and click[1] < 230:
                    screen = pygame.display.set_mode((1000, 900))
                if 251 < click[0] and click[0] < 800 and 300 < click[1] and click[1] < 430:
                    screen = pygame.display.set_mode((1700, 600))
                if 251 < click[0] and click[0] < 800 and 500 < click[1] and click[1] < 630:
                    screen = pygame.display.set_mode((1200, 700))
                if 950 > click[0] and click[0] > 850 and 400 > click[1] and click[1] > 300:
                    switch = False
        pygame.display.update()
        clock.tick(60)
        
def win(screen, clock):
    screen.blit(win_screen, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

def shop(screen, clock, money):
    entered = True
    while entered == True:
        screen.blit(shop_screen, (0, 0))
        screen.blit(money_texty, (525, 0))
        money_text = my_font.render(str(money), False, (0, 0, 0))
        screen.blit(money_text, (665, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                print(click)
                if 1177 > click[0] and click[0] > 833 and 678 > click[1] and click[1] > 522:
                    entered = False
                if 785 > click[0] and click[0] > 544 and 678 > click[1] and click[1] > 522:
                    print("flamingo")
                    if money >= 100:
                        win()
                        print("end")
                if 367 > click[0] and click[0] > 24 and 678 > click[1] and click[1] > 522:
                    if money >= 5:
                        money -= 5
                        #give them a grow juice
                    #figure out the mechanics of placing down the juice


            pygame.display.update()
            clock.tick(60)

def show_game(screen, clock):
    settings_screen = False
    game = True
    money = 0
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
                if 1014 > click[0] and click[0] > 890 and 385 > click[1] and click[1] > 250:
                    shop(screen, clock, money)
                    screen.blit(money_text, (690, 0))

                if 328 > click[0] and click[0] > 284 and 251 > click[1] and click[1] > 209 and money < 10:
                    money += 1

        screen.blit(main, (0, 0))
        screen.blit(settings, (0, 0))
        screen.blit(money_texty, (550, 0))
        money_text = my_font.render(str(money), False, (0, 0, 0))
        screen.blit(money_text, (690, 0))
        screen.blit(head, (230, 170))



        pygame.display.update()
        clock.tick(60)
