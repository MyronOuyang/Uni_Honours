import math
import random
import numpy as np
from scipy.linalg import qr
import copy

shift_arr = np.random.uniform(-80, 80, size=(20))
rotate_matrix = np.random.randn(20, 20)


def Sphere(particle):
    total = 0
    for i in range(len(particle.position)):
        total += particle.position[i] ** 2
    return (total)


def Ackley(particle):
    firstSum = 0.0
    secondSum = 0.0
    for c in particle.position:
        firstSum += c**2.0
        secondSum += math.cos(2.0 * math.pi * c)
    n = float(len(particle.position))
    return -20.0 * math.exp(-0.2 * math.sqrt(firstSum / n)) - math.exp(secondSum / n) + 20 + math.e


def Katsuura(particle):
    val = 1.0
    dimension = len(particle.position)
    for i in range(dimension):
        valt = 0.0
        for j in range(1, 33):
            valt += math.fabs(2 ** j * particle.position[i] - round(2 ** j * particle.position[i])) / 2 ** j
        val *= (1 + (i + 1) * valt) ** (10 / dimension ** 1.2) - (10 / dimension ** 2)
    return (10 / dimension ** 2) * val


def Michalewicz(particle):
    m = 10
    michalewicz = 0.0
    j = 1
    for c in particle.position:
        michalewicz += math.sin(c) * math.sin(j * c**2 / math.pi) ** (2 * m)
        j += 1
    return -michalewicz


def Shubert(particle):
    shubert = 1.0
    for c in particle.position:
        valt = 0.0
        for i in range(1, 6):
            valt += i * math.cos((i + 1) * c + i)
        shubert *= valt
    return shubert


def SHR_Sphere(particle):
    new_particle = copy.deepcopy(particle)
    new_particle.position = Shift_Rotate(particle.position)
    return Sphere(new_particle)


def SHR_Ackley(particle):
    new_particle = copy.deepcopy(particle)
    new_particle.position = np.array(Shift_Rotate(particle.position))
    return Ackley(new_particle) - 140


def SHR_Katsuura(particle):
    new_particle = copy.deepcopy(particle)
    new_particle.position = Shift_Rotate(particle.position)
    return Katsuura(new_particle) + 130


def SHR_Michalewicz(particle):
    new_particle = copy.deepcopy(particle)
    new_particle.position = Shift_Rotate(particle.position)
    return Michalewicz(new_particle) - 100


def SHR_Shubert(particle):
    new_particle = copy.deepcopy(particle)
    new_particle.position = Shift_Rotate(particle.position)
    return Shubert(new_particle) - 120


def Shift_Rotate(position):
    global rotate_matrix, shift_arr

    new_position = copy.deepcopy(position)
    new_position = new_position - shift_arr

    q, r = qr(rotate_matrix)
    new_position = q.dot(new_position)

    return (new_position)


def init_shift_rotate():
    global rotate_matrix, shift_arr

    shift_arr = np.random.uniform(-80, 80, size=(20))
    rotate_matrix = np.random.randn(20, 20)
