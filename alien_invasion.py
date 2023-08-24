import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  #Initialize game and create a screen object.
  pygame.init()
  ai_settings=Settings()
  # screen = pygame.display.set_mode((1200,800))

  screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  #Set the background color.
  #bg_color = (230,230,230)

  #Make a ship.
  ship = Ship(ai_settings, screen)

  #set backgound colour.
  #bg_color=(230, 230, 230)

  #Start the main loop for the game.
  while True:
      gf.check_events(ship)	
      ship.update()
      gf.update_screen(ai_settings,screen,ship)         


     #Watch for the keyboard and mouse events.
   # for event in pygame.event.get():
#	    if event.type == pygame.QUIT:
#		    sys.exit()
       
    # Redraw the screen during each pass trhough the loop
    #  screen.fill(ai_settings.bg_color)
     # ship.blitme()
  
   #Redraw the screen during each pass through the loop.
   #
         # Make the most recently drawn screen visible.
     # pygame.display.flip()

run_game()
