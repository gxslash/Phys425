import numpy as np
import matplotlib.pyplot as plt
import random
import time
from multiprocessing import Pool



# Generates different sizes of random arrays
def random_vector_generator(count):
    vecs = []
    for c in count:
        vec = random.sample(range(1, 100*int(c)), 100*int(c)-1)
        vecs.append(vec)
    return vecs

# Generates different sizes of sorted arrays
def sorted_vector_generator(count):
    vecs = []
    for c in count:
        vec = np.linspace(1, 100*c, 100*c)
        vecs.append(vec)
    return vecs

def bubblesort_timer(m_vector):
    time1 = time.time()
    for i in range(len(m_vector) - 1):
        for j in range(0, len(m_vector)-i-1): 
            if (m_vector[j] > m_vector[j + 1]):
                m_vector[j], m_vector[j + 1] = m_vector[j + 1], m_vector[j]
    time2 = time.time()
    return time2-time1


def main():
    counts = np.linspace(1, 100, 100)

    m_vecs = random_vector_generator(counts)
    times = []
    
    for vec in m_vecs:
        time_diff = bubblesort_timer(vec)
        times.append(time_diff)

    plt.plot(np.linspace(1, len(times), len(times)), times)
    plt.show()


def parallel_processing():
    counts = np.linspace(1, 100, 100)

    m_vecs = random_vector_generator(counts)

    with Pool(4) as p:
        times = p.map(bubblesort_timer, m_vecs)
    
    plt.plot(np.linspace(1, len(times), len(times)), times)
    plt.show()


if __name__ == '__main__':
    time1 = time.time()
    parallel_processing()
    time2 = time.time()
    print(time2-time1)
    
    time1 = time.time()
    main()
    time2 = time.time()
    print(time2-time1)

    

    
