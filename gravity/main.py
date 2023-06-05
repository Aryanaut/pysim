import numpy as np
import time
import argparse
import random
from classes.sim import Sim
from classes.body import Body

def gen_positions(xLimit, yLimit):
    return [random.randint(0, xLimit), random.randint(0, yLimit), 0]

def main():

    helpStr = """
    Controls: \n
    r: Randomize positions and velocities.\n
    t: Draw triangle.\n
    p: Display force values.\n
    f: Freeze simulation.\n
    \nRun with --toroidal to have endless space.\n
    """

    parser = argparse.ArgumentParser(description=helpStr)
    parser.add_argument("--toroidal", action="store_true", dest="toroid", required=False)
    args = parser.parse_args()

    body1 = Body(np.array([[400, 300, 0]]), 6e21, (255, 255, 0))
    body1.updateV(np.array([[random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]]))

    body2 = Body(np.array([[500, 500, 0]]), 6e21, (0, 255, 255))
    body2.updateV(np.array([[random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]]))

    body3 = Body(np.array([[600, 300, 0]]), 6e21, (255, 0, 255))
    body3.updateV(np.array([[random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)]]))

    bodies = [body1, body2, body3]

    sim = Sim()

    if args.toroid:
        sim.toroidal = True

    sim.init_environment(bodies)
    sim.display_env()

if __name__ == '__main__':
    main()