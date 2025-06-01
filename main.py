import pygame
import random
import math
import numpy as np
from utils import *
from Agent import Agent

# 1366x768
WIDTH, HEIGHT = 1366, 768
NUM_AGENTS = 20
NUM_FOOD = 30
GENERATION_TIME = 10  # seconds

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

agents = [Agent() for _ in range(NUM_AGENTS)]
food = generate_food()
generation = 0
gen_timer = 0

def new_generation(prev_agents):
    sorted_agents = sorted(prev_agents, key=lambda a: -a.food_eaten)
    survivors = sorted_agents[:len(prev_agents)//5]
    new_agents = []

    for _ in range(len(prev_agents)):
        parent = random.choice(survivors)
        child_brain = mutate_brain(parent.brain)
        new_agents.append(Agent(brain=child_brain))

    return new_agents
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
running = True
while running:


    dt = clock.tick(60) / 1000.0
    gen_timer += dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    generation_text = my_font.render('Generation {}'.format(generation), False, (255, 255, 255))
    screen.blit(generation_text, (1100,50))


    for f in food:
        pygame.draw.circle(screen, (255, 255, 0), f, 4)

    prev_max_food = 0;
    prev_max_food_idx = 0;
    for i, ag in enumerate(agents):
        if(prev_max_food < ag.food_eaten):
            prev_max_food = ag.food_eaten;
            prev_max_food_idx = i

    for agent in agents:
        agent.update(food)
        agent.draw(screen)


    max_food = 0;
    max_food_idx = 0;
    for i, ag in enumerate(agents):
        if(max_food < ag.food_eaten):
            max_food = ag.food_eaten;
            max_food_idx = i

    agents[prev_max_food_idx].color = (0, 200, 0)
    agents[max_food_idx].color = (200, 0, 0)

    max_food_text = my_font.render('Max Score {}'.format(max_food), False, (255, 255, 255))
    screen.blit(max_food_text, (1100, 100))

    if gen_timer > GENERATION_TIME:
        generation += 1
        gen_timer = 0
        print(f"--- Generation {generation} ---")
        agents = new_generation(agents)
        food = generate_food()


    pygame.display.flip()

pygame.quit()

