"""
Brute Force Algorithm is to find all the permutations (paths) of 
the points and calculate the minimum distances among the permutations 
recursively.
"""
import tsplib95
import sys
import time
import os
import glob
import pandas as pd

class BruteForce:
    def __init__(self, time_limit) -> None:
        self.bestArr = []
        self.minDistance = sys.float_info.max
        self.isFinished = False
        self.time = time_limit

    def getTSP(self, filename: str, time_limit: int) -> None:
        graph = tsplib95.load(filename)
        numNodes = len(list(graph.get_nodes()))
        visited = [False for i in range(numNodes + 1)]
        start_time = time.time()
        self.backtracking(graph, numNodes, 1, visited, [], start_time, time_limit)
        end_time = time.time()
        if (end_time - start_time < self.time):
            self.time = end_time - start_time
            self.isFinished = True

    def backtracking(self, graph, numNodes: int, pos: int, visited: list, retArray: list, start_time, time_limit) -> None:
        if (time.time() - start_time >= time_limit):
            return
        if (pos > numNodes):
            index = 1
            distance = 0
            while (index < numNodes):
                edge = retArray[index - 1], retArray[index]
                weight = graph.get_weight(*edge)
                distance += weight
                index += 1
            
            lastEdge = retArray[index - 1], retArray[0]
            lastWeight = graph.get_weight(*lastEdge)
            distance += lastWeight
            if (distance < self.minDistance):
                self.minDistance = distance
                self.bestArr = retArray.copy()
                self.bestArr.append(retArray[0])

        for i in range(1, numNodes + 1):
            if (visited[i] == False):
                visited[i] = True
                retArray.append(i)
                self.backtracking(graph, numNodes, pos + 1, visited, retArray, start_time, time_limit)
                visited[i] = False
                retArray.pop()

