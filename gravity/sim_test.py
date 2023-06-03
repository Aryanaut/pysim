import numpy as np
import time
import argparse
import random
from classes.sim import Sim
from classes.body import Body

def gen_positions(xLimit, yLimit):
    return [random.randint(0, xLimit), random.randint(0, yLimit), 0]

def main():

    parser = argparse.ArgumentParser(description="Three Body Problem simulation.")
    parser.add_argument("--num_bodies", dest="N", required=False)
    parser.add_argument("--filename", dest="filename", required=False)
    args = parser.parse_args()

    N = 3
    if args.N:
        N = int(N)
    """
    bodies = []
    
    for i in range(N):

        # Triangle coordinates = (450, 350), (500, 450), (550, 350)
        temp = Body(np.array([gen_positions(1000, 800)]), 6e21, (255, 255, 255))
        temp.updateV(np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]]))
        bodies.append(temp)

    """

    body1 = Body(np.array([[450, 350, 0]]), 6e21, (255, 255, 255))
    body1.updateV(np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]]))

    body2 = Body(np.array([[500, 450, 0]]), 6e21, (255, 255, 255))
    body2.updateV(np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]]))

    body3 = Body(np.array([[550, 350, 0]]), 6e21, (255, 255, 255))
    body3.updateV(np.array([[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]]))

    bodies = [body1, body2, body3]

    sim = Sim()
    sim.init_environment(bodies)
    sim.display_env()

if __name__ == '__main__':
    main()