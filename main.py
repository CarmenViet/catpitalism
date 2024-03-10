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
show_intro_screen(screen, clock)
show_game(screen, clock)
pygame.quit()





#at start of game since no factories you click manually on person to get money #
#you buy from shop to get upgrades and the final goal of game is to buy a cat ##
#stop hardcoding because you need to choose between game settings for size of screen #
#colorful grid ##
#make a settings file that stores the information for what screen size setting the player chooses (they can switch between the sizes at any time throughout the game) ###
#theres a settings file that is being read and then when the player makes a decision about the screen size, it writes that decision into the settings file to know thats what the size should be ###
#money variable #
#for color change, the grid color changes if you get an upgrade for that square ##
#click onto shop door to enter shop #
#shop has 4 items (factory grow juice (grows factory, ends at level 3 factory (bronze silver gold)) and cat (when you get the cat the game ends abruptly)) ##
#factories can just be ugly squares #
#when you buy from shop, you press on grow juice and it brings you back to the farm to select which grid to place it onto ###
#when you buy cat, the screen switches to the person with a cat on their lap and the game ends #
#grid should be a 3x3 or 2x2 ##
#have settings button on top left constantly ##
#settings button should be a square to make it easier to check if the player has clicked on settings or not #
#when game is over turn off the while loop by setting game to False
#do settings file through json
#import json library
#convert the json settings file into a dictionary that we can change