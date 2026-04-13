import pygame
import sys
import matplotlib.pyplot as plt

from bird import Bird
from pipe import Pipe
from ga import next_generation
import config

pygame.init()

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("Flappy Bird AI (Advanced)")

clock = pygame.time.Clock()

birds = [Bird() for _ in range(config.POPULATION_SIZE)]
pipes = [Pipe()]

generation = 1
best_score = 0
scores = []

font = pygame.font.SysFont("Arial", 24)

frame_count = 0
MAX_FRAMES = 600

# Clouds
clouds = [[100, 100], [300, 200], [200, 50]]


def get_nearest_pipe(bird):
    for pipe in pipes:
        if pipe.x + pipe.width > bird.x:
            return pipe
    return pipes[0]


def check_collision(bird, pipe):
    if bird.y < 0 or bird.y > config.HEIGHT:
        return True

    if pipe.x < bird.x < pipe.x + pipe.width:
        if bird.y < pipe.height or bird.y > pipe.height + pipe.gap:
            return True

    return False


running = True
while running:
    clock.tick(60)
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pipes[-1].x < 300:
        pipes.append(Pipe())

    for pipe in pipes:
        pipe.move()

    pipes = [p for p in pipes if not p.off_screen()]

    alive = 0
    best_bird = None
    max_fit = -1

    for bird in birds:
        if bird.alive:
            alive += 1
            bird.move()

            pipe = get_nearest_pipe(bird)
            bird.decide(pipe)

            if check_collision(bird, pipe):
                bird.alive = False

            if bird.fitness > max_fit:
                max_fit = bird.fitness
                best_bird = bird

    if max_fit > best_score:
        best_score = max_fit

    if alive == 0 or frame_count > MAX_FRAMES:
        scores.append(best_score)
        birds = next_generation(birds, config.POPULATION_SIZE, config.MUTATION_RATE)
        pipes = [Pipe()]
        generation += 1
        frame_count = 0

    # 🌤 Background
    screen.fill((135, 206, 235))

    # ☁ Clouds
    for cloud in clouds:
        pygame.draw.circle(screen, (255, 255, 255), cloud, 30)
        pygame.draw.circle(screen, (255, 255, 255), (cloud[0]+30, cloud[1]), 25)
        pygame.draw.circle(screen, (255, 255, 255), (cloud[0]-30, cloud[1]), 25)

        cloud[0] -= 1
        if cloud[0] < -50:
            cloud[0] = config.WIDTH + 50

    for pipe in pipes:
        pipe.draw(screen)

    for bird in birds:
        if bird.alive:
            bird.draw(screen, bird == best_bird)

    # UI TEXT
    screen.blit(font.render(f"Gen: {generation}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Alive: {alive}", True, (0, 0, 0)), (10, 40))
    screen.blit(font.render(f"Best: {int(best_score)}", True, (0, 0, 0)), (10, 70))

    pygame.display.update()

pygame.quit()

# 📊 GRAPH
plt.plot(scores)
plt.title("AI Learning Progress")
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.show()

sys.exit()