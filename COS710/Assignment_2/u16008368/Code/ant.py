import math
import threading
import time
from collections import deque
import numpy as np


class Ant(threading.Thread):
    def __init__(self, thread_id, maze_width, current_node, start_node, exit_node, alpha, beta, r_constant, q_constant, local_evaporation_rate, global_evaporation_rate):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

        self.alpha = alpha
        self.beta = beta
        self.r_constant = r_constant
        self.q_constant = q_constant

        self.maze_width = maze_width
        self.exit_node = exit_node
        self.start_node = start_node
        self.local_evaporation_rate = local_evaporation_rate
        self.global_evaporation_rate = global_evaporation_rate

        self.current_node = current_node
        self.acc_distance = deque()
        self.stack_nodes = deque([current_node])
        self.arr_nodes = np.zeros((maze_width ** 2), dtype=bool)
        self.visted_nodes = np.zeros((maze_width ** 2), dtype=bool)
        self.total_distance = 0

    def update_global_pheromone(self, global_evaporation_rate, best_path, best_distance):
        print("Ant {}: Resetting".format(self.thread_id))
        while len(self.stack_nodes) > 1:
            current_node = self.stack_nodes.pop()
            neighbour_node = self.stack_nodes[-1]
            self.update_pheromone(False, current_node, neighbour_node, best_path, best_distance)

    def move_decision(self, neighbours):
        random_val = np.random.rand()
        if random_val <= self.r_constant:
            return self._r_less_than(neighbours)
        else:
            return self._r_greater_than(neighbours)

    def _r_less_than(self, neighbours):
        max_value = (None, None)
        for index, neighbour in enumerate(neighbours):
            if neighbour is not None:
                heuristic_value = self._calc_heuristic(index, neighbour['distance'])
                val = neighbour['pheromone'] * math.pow(heuristic_value, self.beta)
                if (max_value == (None, None)) or (val > max_value[1]):
                    max_value = (neighbour, val)

        return max_value[0]

    def _r_greater_than(self, neighbours):
        denom = 0
        probability_arr = [0, 0, 0, 0]
        for index, neighbour in enumerate(neighbours):
            if neighbour is not None:
                heuristic_value = self._calc_heuristic(index, neighbour['distance'])
                val = math.pow(neighbour['pheromone'], self.alpha) * math.pow(heuristic_value, self.beta)
                denom += val
        for index, neighbour in enumerate(neighbours):
            if neighbour is not None:
                heuristic_value = self._calc_heuristic(index, neighbour['distance'])
                val = math.pow(neighbour['pheromone'], self.alpha) * math.pow(heuristic_value, self.beta)
                val = val / denom
                probability_arr[index] = val

        return np.random.choice(neighbours, p=probability_arr)

    def _calc_heuristic(self, index, distance):
        if index == 0:
            return distance
        if index == 2:
            return distance * 0.75
        else:
            return distance * 0.5

    def calc_available_neighbours(self, neighbours):
        available_neighbours = [None, None, None, None]
        for index, neighbour in enumerate(neighbours):
            if (neighbour['node'] is not None):
                pos = neighbour['node'].Position[0] * self.maze_width + neighbour['node'].Position[1]
                if not self.visted_nodes[pos]:
                    available_neighbours[index] = neighbour

        if available_neighbours == [None, None, None, None]:
            return None
        else:
            return available_neighbours

    def update_pheromone(self, local, current_node, neighbour_node, best_path=[], best_distance=0):
        for neighbour in current_node.Neighbours:
            if (neighbour['node'] is not None) and (neighbour['node'].Position == neighbour_node.Position):
                if local:
                    updated_pheromone = (1 - self.local_evaporation_rate) * neighbour['pheromone'] + self.local_evaporation_rate * 1
                else:
                    quality = self.q_constant / (self.total_distance / best_distance)
                    pos = neighbour['node'].Position[0] * self.maze_width + neighbour['node'].Position[1]
                    delta_pheromone = quality if best_path[pos] else 0
                    # delta_pheromone = quality if neighbour['node'].Position in best_path else 0
                    updated_pheromone = (1 - self.global_evaporation_rate) * neighbour['pheromone'] + self.global_evaporation_rate * delta_pheromone
                neighbour['pheromone'] = updated_pheromone
        for neighbour in neighbour_node.Neighbours:
            if (neighbour['node'] is not None) and (neighbour['node'].Position == current_node.Position):
                if local:
                    updated_pheromone = (1 - self.local_evaporation_rate) * neighbour['pheromone'] + self.local_evaporation_rate * 1
                else:
                    quality = self.q_constant / (best_distance / self.total_distance)
                    pos = neighbour['node'].Position[0] * self.maze_width + neighbour['node'].Position[1]
                    delta_pheromone = quality if best_path[pos] else 0
                    # delta_pheromone = quality if neighbour['node'].Position in best_path else 0
                    updated_pheromone = (1 - self.global_evaporation_rate) * neighbour['pheromone'] + self.global_evaporation_rate * delta_pheromone
                neighbour['pheromone'] = updated_pheromone

    def remove_local_pheromone(self, current_node, neighbour_node):
        for neighbour in current_node.Neighbours:
            if (neighbour['node'] is not None) and (neighbour['node'].Position == neighbour_node.Position):
                neighbour['pheromone'] = 0.01
        for neighbour in neighbour_node.Neighbours:
            if (neighbour['node'] is not None) and (neighbour['node'].Position == current_node.Position):
                neighbour['pheromone'] = 0.01

    def run(self):
        print("Ant {}: Searching".format(self.thread_id))
        while True:
            if self.current_node.Position == self.exit_node.Position:
                break
            else:
                neighbours = self.calc_available_neighbours(self.current_node.Neighbours)
                if neighbours is None:
                    self.acc_distance.pop()
                    prev_node = self.stack_nodes.pop()
                    self.current_node = self.stack_nodes[-1]
                    pos = prev_node.Position[0] * self.maze_width + prev_node.Position[1]
                    self.arr_nodes[pos] = False
                    self.remove_local_pheromone(self.current_node, prev_node)
                else:
                    dict_neighbour = self.move_decision(neighbours)
                    self.update_pheromone(True, self.current_node, dict_neighbour['node'])
                    self.current_node = dict_neighbour['node']
                    self.stack_nodes.append(dict_neighbour['node'])
                    pos = dict_neighbour['node'].Position[0] * self.maze_width + dict_neighbour['node'].Position[1]
                    self.arr_nodes[pos] = True
                    self.visted_nodes[pos] = True
                    self.acc_distance.append(dict_neighbour['distance'])

        self.total_distance = np.sum(self.acc_distance)
        print("Ant {}: Finished".format(self.thread_id))
