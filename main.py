from code1 import Stiffener
import numpy
import matplotlib.pyplot as plt


s1 = Stiffener(50, 5, 2000, 780)

tab = numpy.random.uniform(0.0, 5.0, 250)


plt.hist(tab, 5)
plt.show()

