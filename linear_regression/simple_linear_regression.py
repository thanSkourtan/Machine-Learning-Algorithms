"""


@author: than_skourtan
"""

from random import randint, random
import numpy as np
from numpy.random import rand, randn
import matplotlib.pyplot as plt



def fit(x_axis,y_axis):
    mean = lambda x_axis: sum(x_axis)/len(x_axis)
    nominator = sum([(x - mean(x_axis)) * (y - mean(y_axis)) for x, y in zip(x_axis,y_axis)])
    denominator = sum([pow((x - mean(x_axis)),2) for x in x_axis])
    
    first_parameter = nominator / denominator
    
    second_parameter = mean(y_axis) - first_parameter*mean(x_axis)
    return first_parameter, second_parameter

#===============================================================================
# TESTING
#===============================================================================

noise = [rand() for i in range(100)] 
print(noise)

x = [11,7,14,11,43,38,61,75,38,28,12,18,18,17,19,32,42,57,44,114,35,11,13,10]
y = [11,13,17,13,51,46,132,135,88,36,12,27,19,15,36,47,65,66,55,145,58,12,9,9]

plt.plot(x,y,".")

first, second = fit(x,y)
print(first)
print(second)

plt.show()


'''

noise = np.random.randn(100,1)
x = np.random.rand(100,1) * 10

y = 2 + 3.5 * x + noise

plt.plot(x,y,'.')
plt.show()

'''