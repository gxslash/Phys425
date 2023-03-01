import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

#Define the data to be fit with some noise:
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)

np.random.seed(1729)

y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

#Fit for the parameters a, b, c of the function func:
popt,pcov= curve_fit(func, xdata, ydata)
print("a,b,c=",popt)

p1=plt.plot(xdata,ydata)
p2=plt.plot(xdata,func(xdata, *popt), 'r-')

myplot=p1+p2
plt.show()