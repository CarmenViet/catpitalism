import pygame
import os

intro_screen_file_name = 'catpitalism_intro.png'
settings_image_file_name = 'settings.png'
main_file_name = 'main.png'
one_file_name = 'option_one.png'
two_file_name = 'option_two.png'
three_file_name = 'option_three.png'
shop_screen_file_name = 'shop.png'
win_screen_file_name = 'win_screen.png'
empty_block_file_name = 'empty.png'
level_up_file_name = 'one.png'
max_file_name = 'max.png'
back_file_name = 'back.png'

def get_image(file_name: str, size: tuple):
    image = pygame.image.load(os.path.join('assets', file_name))
    if size != None:
        image = pygame.transform.scale(image, size)
    return image

# get_image(intro_screen_file_name, (settings["width"], settings["height"]))
# get_image(settings_image_file_name, None)
# get_image(empty_block_file_name/level_up_file_name/max_file_name, (150, 120))