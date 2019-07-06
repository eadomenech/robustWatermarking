# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    DCT_1_100 = [
        0.028356,0.031478,0.025234,0.027315,0.028356,0.015349,0.030177,0.031998,0.033559,0.027315,0.028096,0.023153,0.026535,0.033559,0.031738,0.032778,0.023673,0.032778,0.027055,0.025754,0.030177,0.023413,0.014048,0.016129,0.020812,0.029657,0.031478,0.025754,0.026275,0.030697,0.031478,0.030697,0.020812,0.027055,0.022373,0.027315,0.029136,0.022893,0.027575,0.023153,0.032778,0.033559,0.024454,0.030177,0.027836,0.030177,0.004422,
    ]

    # ok
    DCT_36_90 = [
        0.034079,0.035640,0.031998,0.040843,0.036681,0.021592,0.040062,0.040062,0.038502,0.036681,0.033559,0.030437,0.030697,0.029917,0.034079,0.034079,0.033039,0.034860,0.038502,0.030437,0.032518,0.029917,0.024454,0.025754,0.034860,0.034079,0.037461,0.033559,0.032778,0.034860,0.036941,0.036420,0.031217,0.035900,0.028096,0.029917,0.037461,0.038762,0.030437,0.035120,0.037461,0.037721,0.027575,0.034339,0.036160,0.038762,0.008065,
    ]

    # ok
    proposed = [
        0.085588,0.073621,0.078824,0.084547,0.082206,0.053330,0.094953,0.091051,0.081686,0.078044,0.074142,0.084287,0.083507,0.082466,0.078304,0.055931,0.070239,0.091051,0.063996,0.086889,0.083247,0.083767,0.082986,0.082986,0.092092,0.067118,0.083247,0.083767,0.081426,0.093652,0.079865,0.065036,0.035640,0.088450,0.084027,0.082726,0.078304,0.083507,0.091571,0.075702,0.077784,0.078304,0.084807,0.086629,0.067898,0.088450,0.087929
    ]

    data = [DCT_1_100, DCT_36_90, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('BER')
    fig.subplots_adjust(left=0.11, right=0.95, top=0.95, bottom=0.15)

    bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='blue')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], marker='+', color='blue')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(
        True, linestyle='-', which='major', color='lightgrey',
        alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title('Parzival database (47 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('BER')

    # Now fill the boxes with desired colors
    numDists = 3
    boxColors = ['#ade1f9', 'blue', 'red']
    for i in range(numDists):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = np.column_stack([boxX, boxY])
        boxPolygon = Polygon(boxCoords, facecolor=boxColors[i])
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        # Finally, overplot the sample averages, with horizontal alignment in the center of each box
        ax1.plot([np.average(med.get_xdata())], [np.average(data[i])],
                color='w', marker='*', markeredgecolor='k')

    ax1.set_xticklabels(
        [
            'DCT (1, 100)', 'DCT (36, 90)', 'Krawtchouk (19, 128)'
        ],
        rotation=-30, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()