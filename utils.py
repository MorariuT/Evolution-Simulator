import numpy as np
import random
import math
WIDTH, HEIGHT = 1000, 768
NUM_AGENTS = 20
NUM_FOOD = 30
GENERATION_TIME = 10
MUTATION_RATE = 0.8

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def mutate_brain(brain):
    new_brain = {}
    for key in brain:
        new_brain[key] = brain[key] + (np.random.randn(*brain[key].shape) * 0.3 if random.random() < MUTATION_RATE else 0)
    return new_brain


def generate_food():
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_FOOD)]
