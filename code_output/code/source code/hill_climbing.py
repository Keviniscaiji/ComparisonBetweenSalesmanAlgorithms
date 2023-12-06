'''
Reading Coordinates (getCoordinates):
This function reads coordinates of nodes (cities) from a file.
It checks for the 'NODE_COORD_SECTION' in the file, which indicates the beginning of the node coordinates.
After finding the section, it reads each node's coordinates into a list, converting them into a 2D numpy array.

Generating Distance Matrix (generate_matrix):
This function generates a matrix representing the distances between all pairs of nodes.
It calculates the Euclidean distance between each pair of nodes and forms a matrix where matrix[i][j] is the distance between node i and node j.

Finding a Random Solution (solution):
This function creates a random solution for the TSP.
It randomly selects a starting point and then randomly selects the next point until all points are included in thexx solution.

Calculating Path Length (path_length):
This function calculates the total distance of a given path (solution).
It sums up the distances between consecutive nodes in the solution, including the distance from the last node back to the first node.

Generating Neighbors (neighbors):
This function generates neighboring solutions by swapping pairs of cities in the current solution.
It then evaluates each neighbor and returns the one with the shortest path.

Hill Climbing Algorithm (hill_climbing):
The main function that implements the hill-climbing algorithm.
It starts with a random solution and iteratively improves it by moving to the neighboring solution if it offers a shorter path.
The process repeats until no better neighbors are found or a cutoff time is reached.

Time Management:
The hill-climbing function includes a cutoff time to prevent the algorithm from running indefinitely.
'''
import random
import numpy as np
import networkx as nx

import random
import numpy as np
import networkx as nx
import time

def getCoordinates(file_path):
    nodeList = []
    with open(file_path, 'r') as infile:
        stringList = infile.readline().strip().split()
        while stringList[0] != "NODE_COORD_SECTION":
            if stringList[0] == "DIMENSION:":
                dimension = int(stringList[1])
            stringList = infile.readline().strip().split()
        for i in range(dimension):
            x, y = infile.readline().strip().split()[1:]
            nodeList.append([float(x), float(y)])
        coordinate = np.array(nodeList)
    return np.array(coordinate), nodeList


def generate_matrix(coordinate):
    matrix = []
    for i in range(len(coordinate)):
        for j in range(len(coordinate)):
            p = np.linalg.norm(coordinate[i] - coordinate[j])
            matrix.append(p)
    matrix = np.reshape(matrix, (len(coordinate), len(coordinate)))
    return matrix


# finds a random solution
def solution(matrix,seed):
    random.seed(seed)
    points = list(range(0, len(matrix)))
    solution = []
    for i in range(0, len(matrix)):
        random_point = points[random.randint(0, len(points) - 1)]
        solution.append(random_point)
        points.remove(random_point)
    return solution


# calculate the path based on the random solution
def path_length(matrix, solution):
    cycle_length = 0
    for i in range(0, len(solution)):
        cycle_length += matrix[solution[i]][solution[i - 1]]
    return cycle_length


# generate neighbors of the random solution by swapping cities and returns the best neighbor
def neighbors(matrix, solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution.copy()
            neighbor[i] = solution[j]
            neighbor[j] = solution[i]
            neighbors.append(neighbor)

    # assume that the first neighbor in the list is the best neighbor
    best_neighbor = neighbors[0]
    best_path = path_length(matrix, best_neighbor)

    # check if there is a better neighbor
    for neighbor in neighbors:
        current_path = path_length(matrix, neighbor)
        if current_path < best_path:
            best_path = current_path
            best_neighbor = neighbor
    return best_neighbor, best_path


def hill_climbing(coordinate,seed=619, cutoff_time=50):
    start_time = time.time()
    matrix = generate_matrix(coordinate)
    current_solution = solution(matrix,seed)
    current_path = path_length(matrix, current_solution)
    neighbor = neighbors(matrix, current_solution)[0]
    best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)

    while best_neighbor_path < current_path:
        current_solution = best_neighbor
        current_path = best_neighbor_path
        neighbor = neighbors(matrix, current_solution)[0]
        best_neighbor, best_neighbor_path = neighbors(matrix, neighbor)
        end_time = time.time()
        if end_time - start_time >= cutoff_time:
            break

    return current_path, current_solution



