import pygame
import json
from modules.intro import show_intro_screen
from game import show_game

#initialize game
pygame.init()

#initializing variables
json_file = open('settings.json')
settings = json.load(json_file)
screen = pygame.display.set_mode((settings['width'], settings['height']))
clock = pygame.time.Clock()

#game functions
show_intro_screen(screen, clock, settings)
show_game(screen, clock, settings)
pygame.quit()

