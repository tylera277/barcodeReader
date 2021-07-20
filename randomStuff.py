import numpy as np
import matplotlib.pyplot as plt

def plotter(changeList):

    print('MIN:', min(changeList))
    print('MAX:', max(changeList))

    bins = np.arange(0, 35, 1)

    plt.xlim([0, max(changeList)+5])
    plt.hist(changeList, bins=bins)

    plt.show()