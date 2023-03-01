import numpy as np
import matplotlib.pyplot as plt

from dataclasses import dataclass
from random import random
from time import perf_counter



@dataclass
class CalcResult:
    
    elapsed_time: float
    point_count: int
    pi: float


def timer(func):
    def wrapper(*args, **kwargs):
        starting_time = perf_counter()  # Start timer
        pi, point_count = func(*args, **kwargs) # Perform calculation
        elapsed_time = perf_counter() -starting_time # End timer
        calc_params = CalcResult(elapsed_time, point_count, pi)
        print_time(func, calc_params)
        return calc_params
    return wrapper


def print_time(func, params: CalcResult):
    print(func.__name__)
    print ("The value of pi for %d points is %f and the time is %f seconds"%(params.point_count, params.pi, params.elapsed_time))
    if func.__name__ == "unvectorized_calc":
        print('=============\n')


@timer
def vectorized_calc(inside, points):
    """numpy uses vectorization to calculate the result"""
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
    k = np.array([1, 2, 3, 4, 5, 6, 7]) # Generate points from 10^1 to 10^7
    return 10**k 


def plot_comparsion(calc_res_vect, calc_res_unvect):
    time1 = [res.elapsed_time for res in calc_res_vect]
    p1 = [res.point_count for res in calc_res_vect]
    pi1 = [res.pi for res in calc_res_vect]
    time2 = [res.elapsed_time for res in calc_res_unvect]
    p2 = [res.point_count for res in calc_res_unvect]
    pi2 = [res.pi for res in calc_res_unvect]

    _, axis = plt.subplots(2, 1)

    axis[0].plot(time1, p1, '-b', label="vectorized")
    axis[0].plot(time2, p2, '-r', label="unvectorized")
    axis[0].set_title("point count vs time it takes to calculate pi")

    axis[1].plot(pi1, p1, '-b', label="vectorized")
    axis[1].plot(pi2, p2, '-r', label="unvectorized")
    axis[1].set_title("point count vs calculated PI")
    plt.show()


def calculation(func):
    calc_results = []
    inside = 0
    for points in generate_points():
        res = func(inside, points)
        calc_results.append(res)
    return calc_results


def main():
    # all = eval(input('How many points?...'))
    print("\n\n")
    vect_calc_res = calculation(vectorized_calc)
    unvect_calc_res = calculation(unvectorized_calc)
    plot_comparsion(vect_calc_res, unvect_calc_res)


if __name__ == '__main__':
    main()