import numpy as np
import random
import time
import functions
import math

W = 0.8
c1 = 1.5
c2 = 1.5


class Particle():
    def __init__(self, dimensions, bounds):
        self.position = np.array([])
        self.velocity = np.array([])
        self.best_position = np.array([])
        self.best_value = float('inf')
        for _ in range(dimensions):
            self.position = np.append(self.position, random.uniform(bounds[0], bounds[1]))
            self.velocity = np.append(self.velocity, random.random())

    def move(self):
        self.position += self.velocity


class Space():
    def __init__(self, num_particles, iterations, dimensions, bounds):
        self.num_particles = num_particles
        self.dimensions = dimensions
        self.iterations = iterations
        self.bounds = bounds

        self.swarm = [Particle(self.dimensions, self.bounds) for _ in range(self.num_particles)]
        self.global_best_value = float('inf')
        self.global_best_position = np.array([])

    def eval_fitness(self, objective_function):
        for particle in self.swarm:
            # only update particle and global details if within bounds
            if (particle.position >= self.bounds[0]).all() and (particle.position <= self.bounds[1]).all():
                fitness_value = objective_function(particle)
                if(fitness_value < particle.best_value):
                    particle.best_value = fitness_value
                    particle.best_position = list(particle.position)
                if(fitness_value < self.global_best_value):
                    self.global_best_value = fitness_value
                    self.global_best_position = list(particle.position)

    def move_particles(self):
        for particle in self.swarm:
            cognitive_velocity = (c1 * np.random.random(self.dimensions)) * (particle.best_position - particle.position)
            social_velocity = (c2 * np.random.random(self.dimensions)) * (self.global_best_position - particle.position)
            new_velocity = (W * particle.velocity) + cognitive_velocity + social_velocity

            particle.velocity = new_velocity
            particle.move()

    def search(self, objective_function, f):
        for _ in range(30):
            functions.init_shift_rotate()

            self.swarm = [Particle(self.dimensions, self.bounds) for _ in range(self.num_particles)]
            self.global_best_position = np.array([])
            self.global_best_value = float('inf')
            for _ in range(self.iterations):
                self.eval_fitness(objective_function)
                self.move_particles()
            f.write(str(self.global_best_value) + " ")
        f.write('\n')
        print("The best value is: ", self.global_best_value)


f = open("Data_PSO.txt", "w")
f.write(" ")
f.close()
f = open("Data_PSO.txt", "a")

f.write("============== Sphere ================ \n")
W = 0.7
c1 = c2 = 1.5
bounds = [-5.12, 5.12]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.Sphere, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== Ackley ================ \n")
W = 0.75
c1 = c2 = 1.55
bounds = [-32, 32]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.Ackley, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== Katsuura ================ \n")
W = 0.5
c1 = c2 = 1.6
bounds = [-5, 5]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.Katsuura, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== Michalewicz ================ \n")
W = 0.7
c1 = c2 = 1.75
bounds = [0, math.pi]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.Michalewicz, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== Shubert ================ \n")
W = 0.6
c1 = c2 = 1.9
bounds = [-10, 10]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.Shubert, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== SHR_Ackley ================ \n")
W = 0.75
c1 = c2 = 1.55
bounds = [-100, 100]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.SHR_Ackley, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== SHR_Michalewicz ================ \n")
W = 0.7
c1 = c2 = 1.75
bounds = [-100, 100]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.SHR_Michalewicz, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== SHR_Shubert ================ \n")
W = 0.6
c1 = c2 = 1.9
bounds = [-100, 100]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.SHR_Shubert, f)
end = time.time()
print("time: {}".format(end - start))

f.write("============== SHR_Katsuura ================ \n")
W = 0.5
c1 = c2 = 1.6
bounds = [-100, 100]
pso = Space(num_particles=20, iterations=1000, dimensions=20, bounds=bounds)
start = time.time()
pso.search(functions.SHR_Katsuura, f)
end = time.time()
print("time: {}".format(end - start))

f.close()
