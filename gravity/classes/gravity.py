import numpy as np

CONST_G = 6.674e-11

def _magnitude(arr):
    return np.sqrt(pow(arr[0], 2) + pow(arr[1], 2) + pow(arr[2], 2))

def _unit_vector(arr):
    mag = _magnitude(arr)
    return np.array([
        [
            arr[0] / mag,
            arr[1] / mag,
            arr[2] / mag,
        ]
    ])

class Engine:
    def __init__(self):
        self.body_pos_array = np.array([]).reshape((0, 3))
        self.body_list = None

    def define_bodies(self, body_list):
        self.body_list = [np.array([i, body]) for i, body in enumerate(body_list)]

    def calculate_collision(self, m1, m2, x1, x2, v1, v2):
        
        # vf = -1 * v1

        if _magnitude(x1 - x2) == 0:
            vf = -1 * v1
        else:
            vf = v1 - ((2 * m2) / m1 + m2) * (np.inner((v1 - v2), (x1 - x2)) / pow(_magnitude(x1 - x2), 2)) * (x1 - x2) * 0.25
        # vf2 = v2 - ((2 * m1) / m1 + m2) * (np.dot(v2 - v1, x2 - x1) / pow(_magnitude(x2 - x1), 2)) * (x1 - x2)

        return vf


    def compute_force_vectors(self):
        distance_list = []
        force_list = []
        net_force = []

        for primary_body in self.body_list:
            temp = np.array([]).reshape((0, 3))
            for secondary_body in self.body_list:
                temp = np.append(
                    temp,
                    (primary_body[1].position - secondary_body[1].position) * np.array([[-1, -1, 1]]),
                    axis=0
                )
            distance_list.append(temp)
            temp = np.array([]).reshape((0, 3))

        for primary_body in self.body_list:
            temp = np.array([]).reshape((0, 3))
            for secondary_body in self.body_list:
                if _magnitude(distance_list[primary_body[0]][secondary_body[0]]) >= 10:
                    force = CONST_G * primary_body[1].mass * secondary_body[1].mass * (
                            1 / pow(_magnitude(distance_list[primary_body[0]][secondary_body[0]]) * 0.25, 2))
                    force = force * _unit_vector(distance_list[primary_body[0]][secondary_body[0]])
                    temp = np.append(
                        temp,
                        force * np.array([[1, 1, 1]]),
                        axis=0
                    )

                else:
                    temp = np.append(
                        temp,
                        np.array([[0.0, 0.0, 0.0]]),
                        axis=0
                    ) 

                    
            force_list.append(temp)
            temp = np.array([]).reshape((0, 3))

        # print(force_list)
        for obj in force_list:
            net_force.append(obj.sum(axis=0))

        return net_force
