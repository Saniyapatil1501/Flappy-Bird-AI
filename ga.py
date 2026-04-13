import random
import copy

def next_generation(old_birds, size, mutation_rate):
    old_birds.sort(key=lambda b: b.fitness, reverse=True)

    new_birds = []

    for i in range(size):
        parent = random.choice(old_birds[:10])
        child = copy.deepcopy(parent)

        child.brain.mutate(mutation_rate)

        child.x = 100
        child.y = 300
        child.velocity = 0
        child.alive = True
        child.fitness = 0

        new_birds.append(child)

    return new_birds