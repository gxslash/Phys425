import numpy as np
import matplotlib.pyplot as plt
import math

class InitialCondition:

    def __init__(self, v0=20, alpha0=1.57, g=9.81, x=0, y=0):
        self._v0 = v0
        self._alpha0 = alpha0
        self._g = g
        self._x = x
        self._y = y

    @property
    def v0(self):
        return self._v0
    
    @v0.setter
    def v0(self, v0):
        self._v0 = v0

    @property
    def alpha0(self):
        return self._alpha0
    
    @alpha0.setter
    def alpha0(self, alpha0):
        self._alpha0 = alpha0
    
    @property
    def g(self):
        return self._g
    
    @g.setter
    def g(self, g):
        self._g = g

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self, y):
        self._y = y
    


def x_coordinate(v0, alpha0, t):
    return v0*np.cos(alpha0)*t


def y_coordinate(v0, alpha0, g, t):
    y = v0*np.sin(alpha0)*t - 0.5*g*t**2
    return y


def calculate_motion(condition: InitialCondition, t_increment):
    x_vals, y_vals = [], []
    t = 0
    x, y = condition.x, condition.y
    while y >= 0:
        x = x_coordinate(condition.v0, condition.alpha0, t)
        y = y_coordinate(condition.v0, condition.alpha0, condition.g, t)
        t += t_increment
        x_vals.append(x)
        y_vals.append(y)
    return x_vals, y_vals



def plot_motion(x_vals, y_vals):
    plt.plot(x_vals, y_vals)
    plt.show()


def validate_input():
    ...


def ask_user_input():
    is_input_customized = input('Do you want to use your custom initial condition variables: (y/n)\n')
    if is_input_customized == 'y':
        v0 = float(input('Enter v0\n'))
        alpha0 = float(input('Enter alpha0\n'))
        g = float(input('Enter g\n'))
        x = float(input('Enter initial x'))
        y = float(input('Enter initial y'))
        return InitialCondition(v0, alpha0, g, x, y)
    elif is_input_customized == 'n':
        ...    
    else:
        print("Undefined input: Write 'y' or 'n'\n")
        ask_user_input()


def main(debug):

    if (debug):
        init_cond = InitialCondition()
    else:
        ...

    t_increment = 0.1
    x, y = calculate_motion(init_cond, t_increment)
    plot_motion(x, y)



if __name__  == '__main__':
    # Debug mode enabled
    main(debug=True)

