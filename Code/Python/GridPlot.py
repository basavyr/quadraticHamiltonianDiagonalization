import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# create data to be used in the grid plot
param = 2
x = np.arange(0, 10, 1)
y1 = list(map(lambda x: param*x*x, x))
y2 = list(map(lambda x: -param*x*x, x))


def CreateGridPlot(x, y):
   # initialize the figure and chose the size of the grid
    fig=plt.figure()
    fig.suptitle('Main title') # or plt.suptitle('Main title')
    plt.subplot(331)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-1')

    plt.subplot(332)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-2')

    plt.subplot(333)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-3')

    plt.subplot(334)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-1')

    plt.subplot(335)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-2')

    plt.subplot(336)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-3')

    plt.subplot(337)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-3')

    plt.subplot(338)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-3')

    plt.subplot(339)
    # linear plot
    plt.plot(x, y1, '-or')
    plt.plot(x, y1, '--b')
    plt.yscale('linear')
    plt.title('linear-3')

    # # Format the minor tick labels of the y-axis into empty strings with
    # # `NullFormatter`, to avoid cumbering the axis with too many labels.
    plt.gca().yaxis.set_minor_formatter(NullFormatter())

    # # Adjust the subplot layout, because the logit one may take more space
    # # than usual, due to y-tick labels like "1 - 10^{-3}"
    plt.subplots_adjust(top=0.9, bottom=0.1, left=0.10, right=1, hspace=0.5,
                        wspace=0.5)
    plt.savefig('../../Reports/grid_plot.jpeg', bbox_inches='tight')


CreateGridPlot(x, y1)
