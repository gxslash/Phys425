import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass
from random import random
from time import perf_counter
from multiprocessing import Pool



@dataclass
class CalcParams:
    

    def __init__(self, elapsed_time, point_count, pi) -> None:
        self._elapsed_time = elapsed_time
        self._point_count = point_count
        self._pi = pi



def timer(func):
    def wrapper(*args, **kwargs):
        starting_time = perf_counter()
        pi, point_count = func(*args, **kwargs)
        elapsed_time = perf_counter() -starting_time

        # print_time(func, point_count, pi, elapsed_time)
        return elapsed_time
    return wrapper


def print_time(func, point_count, pi, elapsed_time):
    print(func.__name__)
    print ("The value of pi for %d points is %f and the time is %f seconds"%(point_count, pi, elapsed_time))
    if func.__name__ == "unvectorized_calc":
        print('=============\n')


@timer
def vectorized_calc(inside, points):
    x=np.random.rand(points)
    y=np.random.rand(points)
    inside=np.where((x**2+y**2)**(0.5)<1,1,0).sum()
    mypi=4.0*(inside/points)
    return mypi, points


@timer
def unvectorized_calc(inside, points):
    for _ in range(points):
        x,y=random(),random()
        if (x**2+y**2)**(0.5)<1: inside=inside+1
    mypi=4.0*(inside/points)
    return mypi, points


def generate_points():
    k = np.array([1, 2, 3, 4, 5, 6, 7])
    return 10**k 


def plot(power, y):
    plt.plot(power, y)
    plt.show()


def calculation(func, inside):
    time_vec = []
    inside = 0
    for points in generate_points():
        time = func(inside, points)
        time_vec.append(time)
    return time_vec


def main():
    # all = eval(input('How many points?...'))
    print("\n\n")
    calculation(vectorized_calc)
    calculation(unvectorized_calc)


if __name__ == '__main__':
    main()