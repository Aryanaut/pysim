import random
import pygame
import numpy as np

class Body:
    def __init__(self, pos, mass, color, r=10, trace=True, INTERVAL = 0.000004):
        self.vel = np.array([[0, 0, 0]])
        self.force = np.array([[0, 0, 0]])
        self.mass = mass
        self.position = pos
        self.r = r
        self.color = color
        self.thickness = self.r * 2
        self.trace = trace
        self.trail = [(pos[0][0], pos[0][1]), (pos[0][0], pos[0][1])]
        self.INTERVAL = INTERVAL

    def pixel(self, grid):
        grid.fill(self.color, ((self.position[0][0], self.position[0][1]), (1, 1)))

    def draw(self, grid):
        pygame.draw.circle(grid, self.color, (self.position[0][0], self.position[0][1]), self.r, self.thickness)
        
        if self.trace:
            pygame.draw.lines(grid, self.color, False, self.trail)

            if len(self.trail) == 300:
                self.trail.pop(0)

    def updateV(self, nvel):
        self.vel = self.vel + nvel

    def updateF(self, nf):
        self.force = self.force + nf

    def movement(self):
        self.vel = self.vel + (self.force / self.mass) * self.INTERVAL
        self.position = self.position + self.vel * self.INTERVAL
        self.trail.append((self.position[0][0], self.position[0][1]))