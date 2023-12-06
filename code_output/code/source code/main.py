'''
Author: Zheng Wang zwang3478@gatech.edu
Date: 2023-11-30 19:48:35
LastEditors: Zheng Wang zwang3478@gatech.edu
LastEditTime: 2023-12-04 15:50:22
FilePath: /final_project/main.py
Description: This file is the interface of running the whole program to solve TSP, 
             users can get the solution file (.sol) by giving different 
             values of parameters (-inst, -alg, -time, -seed).
'''
import os
import os
import argparse
import time 
import glob
import math
import pandas as pd

from approx import Approx
from brute_force import BruteForce
from evolutionary import Genetic
from hill_climbing import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='TSP Solutions')
    parser.add_argument('-inst', metavar='<filename>', type=str, help='The filename of the instance file')
    parser.add_argument('-alg', metavar='[BF | Approx | LS | genetic | hill_climbing]', type=str, help='The algorithm to use')
    parser.add_argument('-time', metavar='<cutoff_in_seconds>', type=int, default=50, help='Time cutoff in seconds')
    parser.add_argument('-seed', metavar='<random_seed>', type=int, help='Random seed', default=42)

    args = parser.parse_args()

    bestPaths = []
    minDistances = []
    times = []
    isFinisheds = []
    file_name = './DATA/' + args.inst + '.tsp'
    
    if args.alg == 'BF':
        TSP_algo = BruteForce(args.time)
        TSP_algo.getTSP(file_name, args.time)
        bestPaths.append(TSP_algo.bestArr)
        minDistances.append(TSP_algo.minDistance)
        times.append(TSP_algo.time)
        if TSP_algo.isFinished:
            isFinisheds.append("Yes")
        else:
            isFinisheds.append("No")
        file_path = './' + args.inst + '_BF_' + str(args.time) + '.sol' 
    elif args.alg == "Approx":
        TSP_algo = Approx()
        TSP_algo.read_tsplib_file(file_name)
        start_time = time.time()
        TSP_algo.prim_mst_from_matrix(args.seed)
        end_time = time.time()
        minDistances.append(TSP_algo.prox_weight)
        bestPaths.append(TSP_algo.pre_order_seq)
        times.append(end_time - start_time)
        file_path = './' + args.inst + '_Approx_' + str(args.seed) + '.sol' 
    elif args.alg == "LS" or args.alg == "genetic":
        TSP_algo = Genetic(file_name, cutoff_time=args.time)
        start_time = time.time()
        best_tour = TSP_algo.evolve(args.seed)
        end_time = time.time()
        
        best_tour_full = best_tour.copy()
        best_tour_full.append(best_tour[0])
        best_tour_full = [x+1 for x in best_tour_full]

        minDistances.append(TSP_algo.total_distance(best_tour))
        bestPaths.append(best_tour_full)
        times.append(end_time - start_time)
        file_path = './' + args.inst + '_LS_' + str(args.time) + '_' + str(args.seed) + '.sol' 
    elif args.alg == "hill_climbing":
        coordinates, nodeList = getCoordinates(file_name)
        start_time = time.time()
        execution_time, sol_quality = hill_climbing(coordinate=coordinates, seed=args.seed, cutoff_time=args.time)
        end_time = time.time()
        
        distance = 0
        sol_quality.append(sol_quality[0])
        for i in range(1, len(sol_quality)):
            current_node = nodeList[sol_quality[i]]
            previous_node = nodeList[sol_quality[i - 1]]
            distance += math.sqrt((current_node[0] - previous_node[0]) ** 2 + (current_node[1] - previous_node[1]) ** 2)

        minDistances.append(distance)
        bestPaths.append([x + 1 for x in sol_quality])
        times.append(end_time - start_time)
        file_path = './' + args.inst + '_LS_' + str(args.time) + '_' + str(args.seed) + '.sol' 
    else:
        print("Unsupported algorithm specified.")
    
    # write the output file
    with open(file_path, 'w') as file:
        file.write(str(minDistances[0]))
        file.write('\n')
        file.write(','.join(map(str, bestPaths[0])))




        
    
            

            

            




            




    

    


    
