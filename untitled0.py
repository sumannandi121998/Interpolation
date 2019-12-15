
"""
Created on Sun Dec 15 19:08:29 2019

@author: suman
"""

from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.interpolate import CubicSpline
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]
plt.plot(x,y,'o',label='data points')
spl1 = InterpolatedUnivariateSpline(x,y,k=1)
spl2 = InterpolatedUnivariateSpline(x,y,k=2)
spl3 = InterpolatedUnivariateSpline(x,y,k=3)
cs=CubicSpline(x,y)
poly = lagrange(x, y)
z=np.linspace(0,5,100)
plt.plot(z, poly(z),label='lagrange interpolation')
plt.plot(z, spl1(z),label='linear spline')
plt.plot(z, spl2(z),label='quadratic spline')
plt.plot(z, spl3(z),label='cubic spline')
plt.legend()
plt.show()
