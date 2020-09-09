import numpy as np
import matplotlib.pyplot as plt
from numpy import random as rd

from matplotlib.ticker import NullFormatter  # useful for `logit` scale


def give_array(n, param):
    x = np.arange(0, n, 1)
    powers = [1, 2, 3]
    y = list(map(lambda x: param*np.power(x, rd.choice(powers)), x))
    return [list(x), y]


def CreateGridPlot(n, data):
    # params = [1, 2, 3, 4]
    # array_dim = 10
    # data = GenerateData(2*n)
    # data = give_array(20, rd.choice(params))
    x = data[0]
    # x = give_array(array_dim, rd.choice(params))[0]

    fig, ax = plt.subplots(n, n)
    fig.suptitle(f'$\lambda$ evolution with $\epsilon/v$', fontsize=14)

    count = 0
    for i in range(n):
        for j in range(n):
            y = data[1][count]
            y_odd = data[2][count]
            # print(y_odd)
            # y = give_array(array_dim, rd.choice(params))[1]
            p = round(np.mean(y), 3)
            ax[i, j].plot(x, y, '-r', linewidth=2)
            ax[i, j].plot(x, y, 'or', markersize=3)
            ax[i, j].plot(x, y_odd, '-b', linewidth=2)
            ax[i, j].plot(x, y_odd, 'ob', markersize=3)
            ax[i, j].text(0.25, 0.75, f'$\lambda_{count+1}$', horizontalalignment='center',
                          verticalalignment='center', transform=ax[i, j].transAxes, fontsize=8)
            # ax[i, j].set_title(f'$\lambda{(i+1,j+1)}$')
            count = count+1
    for ax_id in ax.flat:
        # ax_id.set(xlabel=f'$q$', ylabel=f'$\lambda$')
        ax_id.set(xlabel=f'$\epsilon/V$')
        # xx=ax_id.get_yticks()
        # print(xx)
        ax_id.set_xticks(np.arange(0, 3.1, step=1))
        # xticks(np.arange(0, 1, step=0.2))

        # y = give_array(5, rd.choice(params))[1]
        # ax[0, 1].plot(x, y, '-k')
        # ax[0, 1].plot(x, y, 'or')
        # ax[0, 1].text(0.15, 0.75, 'N', horizontalalignment='center',
        #               verticalalignment='center', transform=ax[0,1].transAxes)
        # ax[0, 1].set_title(f'$\lambda_{n}$')

        # # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
        # plt.setp([a.get_xticklabels() for a in ax[0, :]], visible=False)
        # plt.setp([a.get_yticklabels() for a in ax[:, 1]], visible=False)

        # Tight layout often produces nice results
        # but requires the title to be spaced accordingly
    fig.tight_layout()
    fig.subplots_adjust(top=0.85)
    plt.savefig('../../Reports/grid_plot.pdf', bbox_inches='tight')

    # plt.show()

#     plt.subplot(332)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-2')

#     plt.subplot(333)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-3')

#     plt.subplot(334)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-1')

#     plt.subplot(335)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-2')

#     plt.subplot(336)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-3')

#     plt.subplot(337)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-3')

#     plt.subplot(338)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-3')

#     plt.subplot(339)
#     # linear plot
#     plt.plot(x, y1, '-or')
#     plt.plot(x, y1, '--b')
#     plt.yscale('linear')
#     plt.title('linear-3')


# # Format the minor tick labels of the y-axis into empty strings with
# # `NullFormatter`, to avoid cumbering the axis with too many labels.
# plt.gca().yaxis.set_minor_formatter(NullFormatter())

# # Adjust the subplot layout, because the logit one may take more space
# # than usual, due to y-tick labels like "1 - 10^{-3}"
# plt.subplots_adjust(top=0.9, bottom=0.1, left=0.10, right=1, hspace=0.5,
    # wspace=0.5)


def GenerateData(n):
    params = [1, 2, 3, 4, 5, 6]
    # xvalues
    qvalues = np.arange(0, 3.1, 0.5)
    # yvalues
    yvalues = []
    for id in range(n):
        y = map(lambda x: np.power(x, rd.choice(params)), qvalues)
        yvalues.append(list(y))
    return [list(qvalues), yvalues]


# print(f[0])
# for id in range(len(f[1])):
#     print(f[1][id])

# Actual representation of the eigenvalues of H
# holds up to n^2 solutions (e.g. for n=3, the first 9 solutions can be graphically represented)
nplots = 3
data = GenerateData(nplots*nplots)

# CreateGridPlot(nplots, data)
