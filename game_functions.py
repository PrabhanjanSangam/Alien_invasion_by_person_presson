import sys

import pygame

def check_events(ship):
    """Respond to keypressed and mouse events."""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
      elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              ship.moving_right = True
          elif event.key == pygame.K_LEFT:
              ship.moving_left = True
      elif event.type == pygame.KEYUP:
          if event.key == pygame.K_RIGHT:
              ship.moving_right = False
          elif event.key == pygame.K_LEFT:
              ship.moving_left = False

        # Move ship to the right by its speed factor.
           # ship.rect.centerx += 1  #ship.speed_factor

def update_screen(ai_settings,screen,ship):
   """Update image on the screen and flip to new screen."""
    #Redraw the screen
   screen.fill(ai_settings.bg_color)
   ship.blitme()

   # the most recently drawn screen visible
   pygame.display.flip()
