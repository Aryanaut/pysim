import random
import pygame
import numpy as np

INTERVAL = 0.000005

class Body:
    def __init__(self, pos, mass, color, r=10):
        self.vel = np.array([[0, 0, 0]])
        self.force = np.array([[0, 0, 0]])
        self.mass = mass
        self.position = pos
        self.r = r
        self.color = color
        self.thickness = self.r * 2

    def pixel(self, grid):
        grid.fill(self.color, ((self.position[0][0], self.position[0][1]), (1, 1)))

    def draw(self, grid):
        pygame.draw.circle(grid, self.color, (self.position[0][0], self.position[0][1]), self.r, self.thickness)

    def updateV(self, nvel):
        self.vel = self.vel + nvel

    def updateF(self, nf):
        self.force = self.force + nf

    def movement(self):
        self.vel = self.vel + (self.force / self.mass) * INTERVAL
        self.position = self.position + self.vel * INTERVAL