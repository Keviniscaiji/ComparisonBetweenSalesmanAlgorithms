# -*- coding: utf-8 -*-
"""
this approximation algorithm is achieved 
using the Preorder tree walk on the Minimum spanning tree of the graph,
which is proved to be a 2-approximation algorithm.
"""

import tsplib95
import numpy as np
import heapq
import time
import glob
import os
import random
import pandas as pd

class Approx:
    
    def __init__(self):
        self.mst_weight = 0
        self.prox_weight = 0
        self.mst_edges = []
        self.pre_order_seq = []
    
    def read_tsplib_file(self, file_path):
        problem = tsplib95.load(file_path)
        nodes = list(problem.get_nodes())
        nodes_num = len(nodes)
        W = np.zeros((nodes_num, nodes_num))
        for i in range(nodes_num):
            for j in range(nodes_num):
                W[i,j] = problem.get_weight(i+1, j+1)
        
        self.W = W  
        self.nodes_num = nodes_num  
    
    def construct_adj_list(self):
        self.adj_list = [[] for _ in range(self.nodes_num)]
        for (u, v, _) in self.mst_edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u) 
            
    def dfs_preorder(self, node, visited):
        visited[node] = True
        self.pre_order_seq.append(node)
        for next_node in self.adj_list[node]:
            if not visited[next_node]:
                self.dfs_preorder(next_node, visited)
                
    def prim_mst_from_matrix(self, seed=None):
        num_nodes = self.nodes_num
        visited = [False] * num_nodes
        if seed is not None:
            random.seed(seed)
        start_node = random.randint(0, num_nodes - 1)
        min_heap = [(0, start_node, -1)]  # (weight, current_node, previous_node)
    
        while min_heap:
            weight, current_node, prev_node = heapq.heappop(min_heap)
        
            if visited[current_node]:
                continue
            
            visited[current_node] = True
            self.mst_weight += weight  
            self.pre_order_seq 
        
            if prev_node != -1: 
                self.mst_edges.append((prev_node, current_node, weight))                            
            
            for next_node in range(num_nodes):
                if not visited[next_node] and self.W[current_node][next_node] != 0:
                    heapq.heappush(min_heap, (self.W[current_node][next_node], next_node, current_node))
                    
        self.construct_adj_list()
        visited = [False] * self.nodes_num
        self.dfs_preorder(start_node, visited)
        
        for i in range(len(self.pre_order_seq)-1):
            self.prox_weight += self.W[self.pre_order_seq[i]][self.pre_order_seq[i+1]]
            
        self.prox_weight += self.W[self.pre_order_seq[-1]][self.pre_order_seq[0]]
        self.pre_order_seq.append(start_node)
        self.pre_order_seq = [i+1 for i in self.pre_order_seq]

