import random
import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook
#%matplotlib widget


def get_possible_directions(point):
    """Point is in form (x, y, z)"""
    directions = [
        (point[0]+1, point[1], point[2]),  # right
        (point[0]-1, point[1], point[2]),  # left
        (point[0], point[1]+1, point[2]),  # forward
        (point[0], point[1]-1, point[2]),  # backward
        (point[0], point[1], point[2]+1),  # up
        (point[0], point[1], point[2]-1)   # down
    ]
    return directions


def random_walk_3D(N):
    Nsteps = range(N)
    current_position = (0, 0, 0)
    visited_points = []
    for _ in Nsteps:
        visited_points.append(current_position)
        all_directions = get_possible_directions(current_position)
        not_visited_directions = [direction for direction in all_directions if direction not in visited_points]
        current_position = random.choice(not_visited_directions)

    xp, yp, zp = zip(*visited_points)
    return xp, yp, zp  # returns tuples. If you want lists, just do list(xp), ...


if __name__ == "__main__":
    x, y, z = random_walk_3D(1000)
    
    print("x", " y ", " z ")
    print(x,y,z) 
np.savetxt("saw.txt",[*zip(x,y,z)],fmt= '%i')
    
  


    