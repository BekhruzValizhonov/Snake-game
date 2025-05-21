import random

import pygame


class Apple:
  def __init__(self):
    self.apple = pygame.Surface((10, 10))
    self.apple.fill((255, 0, 0))
    self.position = (0, 0)

  def set_random_position(self):
    self.position = (random.randrange(0, 400 - 10, 10), random.randrange(0, 400 - 10, 10))
