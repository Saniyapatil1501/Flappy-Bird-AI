import pygame
import config
from neural_network import NeuralNetwork

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0

        self.alive = True
        self.fitness = 0

        self.brain = NeuralNetwork()

    def move(self):
        self.velocity += config.GRAVITY
        self.y += self.velocity
        self.fitness += 1

    def jump(self):
        self.velocity = config.JUMP_STRENGTH

    def decide(self, pipe):
        inputs = [
            self.y / config.HEIGHT,
            pipe.height / config.HEIGHT,
            (pipe.height + pipe.gap) / config.HEIGHT,
            (pipe.x - self.x) / config.WIDTH,
            self.velocity / 10
        ]

        output = self.brain.forward(inputs)

        if output > 0:
            self.jump()

    def draw(self, screen, is_best=False):
        color = (255, 0, 0) if is_best else (255, 255, 0)

        # Body
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 12)

        # Eye
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x)+5, int(self.y)-3), 3)

        # Beak
        pygame.draw.polygon(screen, (255, 165, 0), [
            (self.x+12, self.y),
            (self.x+20, self.y-3),
            (self.x+20, self.y+3)
        ])