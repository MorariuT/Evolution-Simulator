import random
import numpy as np
from utils import *
import pygame
WIDTH, HEIGHT = 1000, 768
NUM_AGENTS = 20
NUM_FOOD = 30
GENERATION_TIME = 10  # seconds
MUTATION_RATE = 0.5
class Agent:
    def __init__(self, brain=None, color=(0, 200, 0)):
        self.x = random.uniform(0, WIDTH);
        self.y = random.uniform(0, HEIGHT);
        self.food_eaten = 0;
        self.speed = 2;
        self.color = color

        if brain:
            self.brain = brain;
        else:
            self.brain = {
                "w1": np.random.randn(3, 10),
                "w2": np.random.randn(10, 10),
                "out": np.random.randn(10, 3),
            }

    def think(self, inputs):

        h = np.dot(inputs, self.brain["w1"])
        h = np.maximum(0, h);

        for idx in range(2, len(self.brain)):
            h = np.dot(h, self.brain["w" + str(idx)]);
            h = np.maximum(0, h);

        out = np.dot(h, self.brain["out"]);
        return np.tanh(out);

    def update(self, food_list):
        if not food_list:
            return

        closest = min(food_list, key=lambda f: distance(self.x, self.y, f[0], f[1]))
        dx = closest[0] - self.x;
        dy = closest[1] - self.y;
        dist = math.hypot(dx, dy);

        #inputs = np.array([dx, dy])
        #inputs = np.array([dx, dy])
        inputs = np.array([dx, dy, dist])
        #inputs = np.array([dx, dy, self.x, self.y])
        #inputs = self.sense(food_list)
        output = self.think(inputs);

        self.x += output[0] * output[2] * 2;
        self.y += output[1] * output[2] * 2;

        self.x = max(0, min(WIDTH - 1, self.x));
        self.y = max(0, min(HEIGHT - 1, self.y));

        if distance(self.x, self.y, closest[0], closest[1]) < 10:
            food_list.remove(closest)
            self.food_eaten += 1

    def sense(self, food_list):
        angles = []

        for i in range(180):
            angles.append(i);

        result = []

        for angle in angles:
            rad = math.radians(angle)
            dir_x = math.cos(rad)
            dir_y = math.sin(rad)

            sensed = 0
            for fx, fy in food_list:
                dx, dy = fx - self.x, fy - self.y
                dist = math.hypot(dx, dy)
                if dist < 100:  # sensor range
                    ndx, ndy = dx / dist, dy / dist
                    alignment = dir_x * ndx + dir_y * ndy
                    if alignment > 0.80:  # tight cone (~18°)
                        sensed = 1
                        break
            result.append(sensed)
        return np.array(result, dtype=float)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)
