import pygame
import json
from modules.images import *

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 20)
head = my_font.render(('click on my head for coins'), False, (0, 0, 0))
inventory = {
    "money": 0,
    "juices": 0,
    "max": 0
}
level_one = [0]
level_two = [0]

def settings_popup(screen, clock, settings):
    switch = True
    while switch == True:
        back = get_image(back_file_name, (settings["width"], settings["height"]))
        screen.blit(back, (0, 0))
        two = get_image(two_file_name, (549, 130))
        screen.blit(two, (250, 100))
        three = get_image(three_file_name, (549, 130))
        screen.blit(three, (250, 250))
        one = get_image(one_file_name, (549, 130))
        screen.blit(one, (250, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                screen_size_has_changed = False
                if settings["width"]*0.665 > click[0] and click[0] > settings["width"]*0.208 and settings["height"]*0.33 > click[1] and click[1] > settings["height"]*0.142:
                    settings["width"] = 1000
                    settings["height"] = 900
                    screen_size_has_changed = True
                if settings["width"]*0.665 > click[0] and click[0] > settings["width"]*0.208 and settings["height"]*0.54 > click[1] and click[1] > settings["height"]*0.277:
                    settings["width"] = 1700
                    settings["height"] = 600
                    screen_size_has_changed = True
                if settings["width"]*0.665 > click[0] and click[0] > settings["width"]*0.208 and settings["height"]*0.756 > click[1] and click[1] > settings["height"]*0.572:
                    settings["width"] = 1200
                    settings["height"] = 700
                    screen_size_has_changed = True
                if screen_size_has_changed == True:
                    screen = pygame.display.set_mode((settings["width"], settings["height"]))
                    settings_string = json.dumps(settings)
                    with open("settings.json", "w") as settings_file:
                        settings_file.write(settings_string)
                    return
        pygame.display.update()
        clock.tick(60)
        
def win(screen, clock, settings):
    while True:
        win_screen = get_image(win_screen_file_name, (settings["width"], settings["height"]))
        screen.blit(win_screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
        clock.tick(60)

def shop(screen, clock, settings, inventory, level_two):
    entered = True
    while entered == True:
        shop_screen = get_image(shop_screen_file_name, (settings["width"], settings["height"]))
        screen.blit(shop_screen, (0, 0))
        money_text = my_font.render("money: " + str(inventory["money"]), False, (0, 0, 0))
        screen.blit(money_text, (settings["width"]*0.47, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if settings["width"]*.98 > click[0] and click[0] > settings["width"]*.6945 and settings["height"]*.9645 > click[1] and click[1] > settings["height"]*.748:
                    entered = False
                if settings["width"]*.654 > click[0] and click[0] > settings["width"]*.346 and settings["height"]*.9645 > click[1] and click[1] > settings["height"]*.748:
                    if inventory["money"] >= 100:
                        win(screen, clock, settings)
                if settings["width"]*.307 > click[0] and click[0] > settings["width"]*.0205 and settings["height"]*.9645 > click[1] and click[1] > settings["height"]*.748:
                    if inventory["money"] >= 5 and inventory["max"] < 3:
                        inventory["money"] -= 5
                        if inventory["juices"] < 3:
                            inventory["juices"] += 1
                            level_one.insert(0, 1)
                        elif inventory["juices"] >= 3:
                            inventory["max"] += 1
                            level_two.insert(0, 1)
        pygame.display.update()
        clock.tick(60)
    money_text = my_font.render(str(inventory["money"]), False, (0, 0, 0))
    pygame.display.update()

def show_game(screen, clock, settings):
    settings_screen = False
    game = True
    plots = 3
    level_zero = True
    start_time = 0
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                if 60 > click[0] and click[0] > 0 and 60 > click[1] and click[1] > 0:
                    settings_screen = True
                    if settings_screen == True:
                        settings_popup(screen, clock, settings)
                
                #entering shop 
                if settings["width"]*0.845 > click[0] and click[0] > settings["width"]*0.745 and settings["height"]*0.545 > click[1] and click[1] > settings["height"]*0.365:
                    shop(screen, clock, settings, inventory, level_two)

                #clicking on head 
                if settings["width"]*0.27 > click[0] and click[0] > settings["width"]*0.235 and settings["height"]*0.35 > click[1] and click[1] > settings["height"]*0.292 and inventory["money"] < 10:
                    inventory["money"] += 1

        #blit main screen
        main_image = get_image(main_file_name, (settings["width"], settings["height"]))
        settings_image = get_image(settings_image_file_name, None)
        screen.blit(main_image, (0, 0))
        screen.blit(settings_image, (0, 0))
        screen.blit(head, (settings["width"]*0.3, settings["height"]*0.3))
        money_text = my_font.render("money: " + str(inventory["money"]), False, (0, 0, 0))
        screen.blit(money_text, (settings["width"]*0.47, 0))

        current_time = pygame.time.get_ticks()
        if current_time >= start_time + 1000:
            start_time = current_time
            if level_one[0] == 1:
                for i in range(inventory["juices"]):
                    inventory["money"] += 1
            if level_two[0] == 1:
                for i in range(inventory["max"]):
                    inventory["money"] += 2
                    
    #plots and upgrades 
        #empty 
        x = settings["width"]*0.083
        y = settings["height"]*0.572
        empty_block_image = get_image(empty_block_file_name, (150, 250))
        if level_zero == True:
            for k in range(plots):
                screen.blit(empty_block_image, (x, y))
                x += 160

        #level one
        y = settings["height"]*0.572
        level_up_block_image = get_image(level_up_file_name, (150, 250))
        if level_one[0] == 1:
            x = 100
            for k in range(inventory["juices"]):
                screen.blit(level_up_block_image, (x, y))
                x += 160

        #max
        x = settings["width"]*0.083
        y = settings["height"]*0.572
        max_block_image = get_image(max_file_name, (150, 250))
        if level_two[0] == 1:
            for k in range(inventory["max"]):
                screen.blit(max_block_image, (x, y))
                x+=160

        pygame.display.update()
        clock.tick(60)