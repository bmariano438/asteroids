import pygame
from constants import *

def main():
  print("Starting asteroids!")
  print("Screen width:", SCREEN_WIDTH)
  print("Screen height:", SCREEN_HEIGHT)
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  

  while True:
     #pygame.Surface.fill(screen, (0,0,0))
    screen.fill((0, 0, 0))
    pygame.display.flip()


if __name__ == "__main__":
    main()
