import pygame
from classes.gravity import Engine
import time
import random
import numpy as np
from classes.body import Body

INTERVAL = 0.000005

class Sim:
    physics_engine = Engine()

    def __init__(self):
        self.run, self.space, self.bodies = None, None, None
        self.toroidal = False

    def write(self, text, position, color=(255, 255, 255)):
        font = pygame.font.SysFont("Arial", 18)        
        text_obj = font.render(text, True, color)
        self.space.blit(text_obj, position)


    def gen_positions(self, xLimit, yLimit):
        return np.array([[random.randint(100, xLimit), random.randint(100, yLimit), 0]])

    def gen_velocities(self, maxVel):
        return np.array([[
            random.randint(-1 * maxVel, maxVel), 
            random.randint(-1 * maxVel, maxVel), 
            0]])

    def init_environment(self, bodies):
        self.bodies = bodies
        size = (1000, 800)
        self.run = True

        pygame.init()
        pygame.display.set_caption("Orbit sim.")
        self.space = pygame.display.set_mode(size)

        self.physics_engine.define_bodies(bodies)

    def randomize(self):
        for i, body in enumerate(self.bodies):
            body.position = self.gen_positions(900, 600)
            body.force = self.gen_velocities(10000)
            body.vel = self.gen_velocities(100)

    def freeze(self):
        for i, body in enumerate(self.bodies):
            body.force = np.array([[0, 0, 0]])

    def display_env(self):
        trace = False
        positions = []
        freeze = False
        debug = False

        while self.run:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.randomize()

                        print("Randomizing...")

                    if event.key == pygame.K_f:
                        freeze = not freeze

                    if event.key == pygame.K_t:
                        print("Tracing...")
                        trace = not trace

                    if event.key == pygame.K_p:
                        debug = not debug

            self.space.fill((0, 0, 0))
            net_list = self.physics_engine.compute_force_vectors()

            for i, body in enumerate(self.bodies):
                body.force = net_list[i]

            for body in self.bodies:
                body.draw(self.space)

                if trace == True:
                    current_pos = (body.position[0][0], body.position[0][1])
                    positions.append(current_pos)
                    # print(positions)
                    
                    if len(positions) >= 2:
                        # print(positions)
                        pygame.draw.line(self.space, body.color, positions[0], positions[1])
                        positions[0] = positions[1]
                        positions.pop()

                if debug == True:
                    current_pos = (body.position[0][0] + 10, body.position[0][1])
                    self.write(str(body.force), current_pos)

                if self.toroidal:
                    x, y, z = (body.position[0][0], body.position[0][1], body.position[0][2])
                    w, h = self.space.get_size()

                    deltaR = 5
                    if x > w + deltaR:

                        body.position[0][0] = -deltaR
                    if x < -deltaR:

                        body.position[0][0] = w + deltaR
                    if y > h + deltaR:

                        body.position[0][1] = -deltaR
                    if y < -deltaR:

                        body.position[0][1] = h + deltaR


            for body in self.bodies:
                if freeze:
                    continue
                body.movement()

            time.sleep(INTERVAL)
            pygame.display.update()