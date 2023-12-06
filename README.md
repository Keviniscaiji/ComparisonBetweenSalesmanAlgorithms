# ComparisonBetweenSalesmanAlgorithms

## CSE 6140 / CX 4140 Project - TSP Report

**Authors:** Haoyang Zeng, Jiayi Qian, Kaiwen Gong, Zheng Wang, Zhikai Xu  
**Affiliation:** Georgia Institute of Technology

### Abstract

The Traveling Salesman Problem (TSP) is encountered in a wide range of areas including vehicle routing, circuit board drilling, and VLSI design. In this project, we solve TSP using four different algorithms: brute-force, approximate algorithm based on MST, genetic algorithm, and hill climbing algorithm. It is found that the genetic algorithm (local search) has the best balance between solution quality and computational time. Moreover, by changing the cutoff time for each algorithm, we found that the obtained total cost decreases along with the increase of cutoff time, which meets the expectation.

### Description of Algorithms

#### Brute Force Algorithm

- Checks for the time limit at the start of the backtracking method.
- Recursively explores all possible routes, updating the best path and minimum distance when a shorter route is found.

#### Approximate Algorithm

- Implements Prim or Kruskal algorithm to get the minimum spanning tree of the graph.
- Performs a preorder tree walk on the generated minimum spanning tree.

#### Hill Climbing Algorithm

- Accepts better solutions unconditionally.
- Accepts worse solutions with a probability decreasing over time, controlled by a decay parameter \(t\).

#### Genetic Algorithm

- Accepts better solutions unconditionally.
- Employs mutation and crossover for introducing variability.
- Utilizes a selection process to determine which individuals reproduce.
- Converges towards optimal solutions over generations.

### Results and Analysis

The results of addressing the TSP problem via different algorithms are tabulated. The algorithms show varying degrees of efficiency and accuracy, with genetic algorithms providing a balance between solution quality and computational time.
![result_difference_algorithms](https://github.com/Keviniscaiji/ComparisonBetweenSalesmanAlgorithms/assets/74641290/0b754e9b-f1f2-4922-8df0-7f57662c7fff)

### Conclusion

Four algorithms were tested for solving the TSP problem. While brute-force finds the best solution, it's computationally expensive. The genetic algorithm offers a practical balance between cost and quality. Among local search algorithms, the genetic algorithm outperforms hill climbing in terms of the experiments' results.


