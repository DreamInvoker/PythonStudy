import matplotlib.pyplot as plt
import numpy as np

# demo
'''
plt.plot([0,2,4,6,8],[3,1,4,5,2])
plt.ylabel('Grade')
plt.axis([-1,10,0,6])
plt.show()
'''


# draw two pictures


def f(t):
    "衰减函数"
    return np.exp(-t) * np.cos(2 * np.pi * t)


a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(212)
plt.plot(a, np.cos(2 * np.pi * a), 'r:')
plt.show()
