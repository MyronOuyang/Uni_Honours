import numpy as np
import random
import time
import functions
import math
import copy

W = 0.2
c1 = 2.15
c2 = 2.15
# W = 0.8
# c1 = 1.5
# c2 = 1.5


class Particle():
    def __init__(self, dimensions, bounds):
        self.position = np.array([])
        self.velocity = np.array([])
        self.lads = np.array([])
        self.best_lads_position = np.array([])
        self.best_lads_value = float('inf')

        self.best_value = float('inf')
        for _ in range(dimensions):
            random_position = random.uniform(bounds[0], bounds[1])
            random_velocity = random.uniform((bounds[0] - random_position), (bounds[1] - random_position))
            self.position = np.append(self.position, random_position)
            self.velocity = np.append(self.velocity, random_velocity)
        self.best_position = copy.deepcopy(self.position)

    def move(self):
        self.position += self.velocity

    def calc_best_lads_position(self, objective_function):
        old_best_val = copy.deepcopy(self.best_lads_value)
        for lad in self.lads:
            if (lad.position >= bounds[0]).all() and (lad.position <= bounds[1]).all():
                fitness_value = objective_function(lad)
                if(fitness_value < self.best_lads_value):
                    self.best_lads_value = float(fitness_value)
                    self.best_lads_position = copy.deepcopy(lad.position)
        return old_best_val == self.best_lads_value


class Space():
    def __init__(self, objective_function, num_particles, iterations, dimensions, bounds):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.iterations = iterations
        self.bounds = bounds
        self.objective_function = objective_function

        self.swarm = [Particle(self.dimensions, self.bounds) for _ in range(self.num_particles)]
        self.global_best_value = float('inf')
        self.global_best_position = np.array([])

        self.assign_lads()
        for particle in self.swarm:
            particle.calc_best_lads_position(objective_function)

    def assign_lads(self):
        for particle in self.swarm:
            particle.lads = np.array([])
            for _ in range(3):
                particle.lads = np.append(particle.lads, self.swarm[np.random.randint(0, self.num_particles)])
            particle.lads = np.append(particle.lads, particle)

    def eval_fitness(self):
        old_global_best = copy.deepcopy(self.global_best_value)
        for particle in self.swarm:
            # only update particle and global details if within bounds
            if (particle.position >= self.bounds[0]).all() and (particle.position <= self.bounds[1]).all():
                fitness_value = self.objective_function(particle)
                if(fitness_value < particle.best_value):
                    particle.best_value = float(fitness_value)
                    particle.best_position = copy.deepcopy(particle.position)
                if(fitness_value < self.global_best_value):
                    self.global_best_value = (fitness_value)
                    self.global_best_position = copy.deepcopy(particle.position)
                updated_best_lad = particle.calc_best_lads_position(self.objective_function)
                # if updated_best_lad:
                #     self.assign_lads()
            if old_global_best == self.global_best_value:
                self.assign_lads()

    def move_particles(self):
        for particle in self.swarm:
            alpha = particle.position + (c1 * random.random()) * (particle.best_position - particle.position)
            beta = particle.position + (c2 * random.random()) * (particle.best_lads_position - particle.position)
            gravity = np.array((particle.position + alpha + beta) / 3)

            sub = np.array(gravity - particle.position)
            sqr = np.array(sub ** 2)
            sum_val = np.sum(sqr)
            radius = float(math.sqrt(sum_val))

            re = np.random.random(self.dimensions)
            s = random.uniform(0, radius)
            re = np.array(re * s + gravity)

            new_velocity = (W * particle.velocity) + re - particle.position
            particle.velocity = np.array(new_velocity)
            particle.move()

    def search(self, f):
        for _ in range(1):
            functions.init_shift_rotate()

            self.swarm = [Particle(self.dimensions, self.bounds) for _ in range(self.num_particles)]
            self.assign_lads()
            for particle in self.swarm:
                particle.calc_best_lads_position(self.objective_function)
            self.global_best_position = np.array([])
            self.global_best_value = float('inf')
            for _ in range(self.iterations):
                self.eval_fitness()
                self.move_particles()
            f.write(str(self.global_best_value) + " ")
        f.write('\n')
        print("The best value is: ", self.global_best_value)


# f = open("Data_SPSO1.txt", "w")
# f.write(" ")
# f.close()
f = open("Data_SPSO.txt", "a")

# f.write("============== Sphere ================ \n")
# W = 0.25
# c1 = c2 = 2.5
# bounds = [-5.12, 5.12]
# pso = Space(objective_function=functions.Sphere, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== Ackley ================ \n")
# W = 0.2
# c1 = c2 = 2.3
# bounds = [-32, 32]
# pso = Space(objective_function=functions.Ackley, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

f.write("============== Katsuura ================ \n")
W = 0.09
c1 = c2 = 2.5
bounds = [-5, 5]
pso = Space(objective_function=functions.Katsuura, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(f)
end = time.time()
print("time: {}".format(end - start))

# f.write("============== Michalewicz ================ \n")
# W = 0.1
# c1 = c2 = 2.5
# bounds = [0, math.pi]
# pso = Space(objective_function=functions.Michalewicz, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== Shubert ================ \n")
# W = 0.1
# c1 = c2 = 2.7
# bounds = [-10, 10]
# pso = Space(objective_function=functions.Shubert, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== SHR_Ackley ================ \n")
# W = 0.2
# c1 = c2 = 2.3
# bounds = [-100, 100]
# pso = Space(objective_function=functions.SHR_Ackley, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== SHR_Michalewicz ================ \n")
# W = 0.1
# c1 = c2 = 2.5
# bounds = [-100, 100]
# pso = Space(objective_function=functions.SHR_Michalewicz, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== SHR_Shubert ================ \n")
# W = 0.1
# c1 = c2 = 2.7
# bounds = [-100, 100]
# pso = Space(objective_function=functions.SHR_Shubert, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

# f.write("============== SHR_Katsuura ================ \n")
# W = 0.09
# c1 = c2 = 2.5
# bounds = [-100, 100]
# pso = Space(objective_function=functions.SHR_Katsuura, num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
# start = time.time()
# pso.search(f)
# end = time.time()
# print("time: {}".format(end - start))

f.close()
