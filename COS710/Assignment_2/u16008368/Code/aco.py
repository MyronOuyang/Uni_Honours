import numpy as np
import math
from ant import Ant
import copy
import sys


class ACO:
    def __init__(self, maze_width, num_ants, start_node, end_node, alpha, beta, global_evaporation_rate, local_evaporation_rate, r_constant, q_constant):
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.global_evaporation_rate = global_evaporation_rate
        self.local_evaporation_rate = local_evaporation_rate
        self.r_constant = r_constant
        self.q_constant = q_constant
        self.best_path = []
        self.maze_width = maze_width

        self.start_node = start_node
        self.end_node = end_node
        self.arr_path = [False] * (maze_width ** 2)

    def solve(self, epoch):
        sys.setrecursionlimit(1500)
        arr_threads = []
        best_path = []
        longest_distance = 0

        for _ in range(epoch):
            for i in range(self.num_ants):
                ant = Ant(i, self.maze_width, self.start_node, self.start_node, self.end_node, self.alpha, self.beta,
                          self.r_constant, self.q_constant, self.local_evaporation_rate, self.global_evaporation_rate)
                arr_threads.append(ant)

            for ant in arr_threads:
                ant.start()
            for ant in arr_threads:
                ant.join()

            for ant in arr_threads:
                if ant.total_distance > longest_distance:
                    longest_distance = copy.deepcopy(ant.total_distance)
                    resultpath = [node.Position for node in ant.stack_nodes]
                    best_path = resultpath
                    self.arr_path = ant.arr_nodes
            for ant in arr_threads:
                ant.update_global_pheromone(self.global_evaporation_rate, self.arr_path, longest_distance)
            arr_threads = []
        print("All Ants Done Traversing")
        return (best_path, [longest_distance])
