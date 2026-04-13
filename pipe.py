import pygame
import random
import config

class Pipe:
    def __init__(self):
        self.x = config.WIDTH
        self.width = 70
        self.gap = config.PIPE_GAP
        self.height = random.randint(100, 400)

    def move(self):
        self.x -= config.PIPE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 0),
                         (self.x, 0, self.width, self.height))
        pygame.draw.rect(screen, (0, 200, 0),
                         (self.x, self.height + self.gap,
                          self.width, config.HEIGHT))

    def off_screen(self):
        return self.x < -self.width