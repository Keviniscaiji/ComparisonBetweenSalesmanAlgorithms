"""
An evolutionary algorithm is a computational method inspired by biological evolution, 
using mechanisms such as selection, mutation, and crossover to iteratively improve solutions to complex problems.
"""

import numpy as np
import random
import time
import os
import glob
import pandas as pd
class Genetic:
    def __init__(self, filename, population_size=100, num_generations=500, mutation_rate=0.05,cutoff_time=300):
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.cities = self.load_data(filename)
        self.num_cities = len(self.cities)
        self.cutoff_time = cutoff_time
        self.population = [random.sample(range(self.num_cities), self.num_cities) for _ in range(population_size)]

    def load_data(self,filename):
        cities = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            start = False
            for line in lines:
                if line.strip() == 'NODE_COORD_SECTION':
                    start = True
                    continue
                if line.strip() == 'EOF' or line.strip() == 'EOF\n':
                    break
                if start:
                    parts = line.split()
                    # Assuming the city coordinates are the 2nd and 3rd items on each line
                    cities.append((float(parts[1]), float(parts[2])))
                    #print(cities)
        return cities

    def distance(self, city1, city2):
        return np.linalg.norm(np.array(city1) - np.array(city2))

    def total_distance(self, tour):
        return sum(self.distance(self.cities[tour[i]], self.cities[tour[i+1]]) for i in range(-1, self.num_cities-1))

    def fitness(self, tour):
        return 1 / self.total_distance(tour)

    def crossover(self, parent1, parent2):
        # Implement ordered crossover
        child = [-1] * self.num_cities
        start, end = sorted(random.sample(range(self.num_cities), 2))
        child[start:end] = parent1[start:end]

        current_pos = end
        for city in parent2:
            if city not in child:
                if current_pos == self.num_cities:
                    current_pos = 0
                child[current_pos] = city
                current_pos += 1

        return child

    def mutate(self, tour):
        a, b = random.sample(range(self.num_cities), 2)
        tour[a], tour[b] = tour[b], tour[a]

    def evolve(self, random_seed):
        start_time = time.time()
        if random_seed is not None:
            random.seed(random_seed)
        for generation in range(self.num_generations):
            if time.time() - start_time > self.cutoff_time:
                # print("Cutoff time reached at generation", generation, "stopping evolution.")
                break
            sorted_population = sorted(self.population, key=lambda tour: self.fitness(tour), reverse=True)
            parents = sorted_population[:int(0.2 * self.population_size)]

            children = []
            while len(children) < self.population_size:
                parent1, parent2 = random.sample(parents, 2)
                child = self.crossover(parent1, parent2)
                if random.random() < self.mutation_rate:
                    self.mutate(child)
                children.append(child)

            self.population = children

        return max(self.population, key=lambda tour: self.fitness(tour))