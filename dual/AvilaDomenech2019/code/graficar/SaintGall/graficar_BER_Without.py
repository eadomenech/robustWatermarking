# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.093392,0.085328,0.079605,0.087409,0.078044,0.058793,0.089230,0.089750,0.083767,0.078564,0.084807,0.065557,0.092872,0.088710,0.087669,0.081165,0.069199,0.090791,0.069719,0.079605,0.080385,0.068939,0.062695,0.060614,0.071540,0.078304,0.095994,0.079865,0.080385,0.080125,0.078824,0.077263,0.066077,0.084547,0.058012,0.082466,0.077263,0.085848,0.080645,0.081946,0.080125,0.092612,0.079084,0.086629,0.084027,0.085328,0.039022
    ]

    liu2018 = [
        0.093392,0.085328,0.079605,0.087409,0.078044,0.058793,0.089230,0.089750,0.083767,0.078564,0.084807,0.065557,0.092872,0.088710,0.087669,0.081165,0.069199,0.090791,0.069719,0.079605,0.080385,0.068939,0.062695,0.060614,0.071540,0.078304,0.095994,0.079865,0.080385,0.080125,0.078824,0.077263,0.066077,0.084547,0.058012,0.082466,0.077263,0.085848,0.080645,0.081946,0.080125,0.092612,0.079084,0.086629,0.084027,0.085328,0.039022
    ]

    avila2018 = [
        0.093392,0.085328,0.079605,0.087409,0.078044,0.058793,0.089230,0.089750,0.083767,0.078564,0.084807,0.065557,0.092872,0.088710,0.087669,0.081165,0.069199,0.090791,0.069719,0.079605,0.080385,0.068939,0.062695,0.060614,0.071540,0.078304,0.095994,0.079865,0.080385,0.080125,0.078824,0.077263,0.066077,0.084547,0.058012,0.082466,0.077263,0.085848,0.080645,0.081946,0.080125,0.092612,0.079084,0.086629,0.084027,0.085328,0.039022
    ]

    proposed = [
        0.017170,0.018470,0.017950,0.019251,0.018991,0.015869,0.017170,0.021592,0.016649,0.016389,0.022373,0.020031,0.017170,0.019511,0.015869,0.018470,0.023413,0.022893,0.017170,0.013528,0.014048,0.019511,0.016649,0.015869,0.015349,0.021332,0.021332,0.016909,0.016129,0.020031,0.016389,0.020812,0.015609,0.021852,0.015088,0.018470,0.021072,0.016649,0.017690,0.022112,0.021332,0.018210,0.011707,0.018991,0.018991,0.013788,0.020291,0.015088,0.020291,0.016389,0.027575,0.018730,0.015088,0.018470,0.022633,0.020291,0.016649,0.022112,0.012747,0.017430
    ]

    data = [shivani2017, liu2018, avila2018, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('BER')
    fig.subplots_adjust(left=0.11, right=0.95, top=0.95, bottom=0.05)

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
    ax1.set_title('Saint Gall database (60 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('BER')

    # Now fill the boxes with desired colors
    numDists = 4
    boxColors = ['darkkhaki', 'green', 'blue', 'red']
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
            '[10]', '[7]', '[2]', 'Proposed'
        ],
        rotation=0, fontsize=14)
    plt.show()


if __name__ == "__main__":
    run_main()