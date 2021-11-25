from numpy import *
import matplotlib.pyplot as plt
import pylab

x = linspace(0, 5, 51)
y = (5*sin(10*x)*sin(3*x))
plt.plot(x, y, 'g--', label=('5*sin(10*x)*sin(3*x)')

plt.axis([0, 5 , -2, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік')
plt.legend()

plt.show
pylab.show()