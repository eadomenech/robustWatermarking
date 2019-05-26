# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.476847,0.473465,0.482570,0.479448,0.485952,0.490895,0.481009,0.492716,0.491155,0.485692,0.480229,0.482310,0.486993,0.496878,0.489854,
    ]

    # ok
    liu2018_k02 = [
        0.331165,0.328044,0.326483,0.332206,0.331946,0.325702,0.330385,0.324402,0.330645,0.327003,0.331165,0.329344,0.327263,0.328304,0.331165,0.327003,0.324662,0.326223,0.330125,0.323881,0.326223,0.328824,0.324922,0.327523,0.327263,0.324922,0.329084,0.329344,0.324402,0.325442,0.326223,0.324922,0.330645,0.325182,0.327003,0.326223,0.332206,0.331426,0.327263,0.325702,0.326483,0.328044,0.324922,0.327523,0.328564,0.326223,0.330645
    ]

    # ok
    liu2018_k04 = [
        0.330645,0.329605,0.330645,0.330905,0.327003,0.327263,0.330905,0.327003,0.328564,0.328824,0.328304,0.325963,0.328304,0.330125,0.329344,0.327523,0.331946,0.329344,0.326483,0.329344,0.330125,0.326743,0.330385,0.325963,0.329865,0.327784,0.333247,0.334287,0.330905,0.333507,0.331686,0.330645,0.332206,0.332986,0.326743,0.329865,0.330905,0.326223,0.328044,0.327523,0.332726,0.328304,0.327784,0.331946,0.328044,0.328824,0.331946
    ]

    # ok
    liu2018_k08 = [
        0.328564,0.321280,0.325442,0.331165,0.326483,0.328044,0.329344,0.331165,0.323881,0.325442,0.326223,0.335068,0.323361,0.329344,0.325702,0.325702,0.324142,0.330385,0.326223,0.330645,0.325702,0.330385,0.325442,0.321020,0.330125,0.326483,0.324142,0.326223,0.325182,0.325182,0.329084,0.329344,0.332726,0.324922,0.323361,0.327003,0.326223,0.328304,0.332206,0.331165,0.326223,0.328304,0.324142,0.330905,0.329605,0.329344,0.327523
    ]

    # ok
    liu2018_k1 = [
        0.323881,0.328824,0.333767,0.328564,0.322060,0.323361,0.326223,0.329344,0.324402,0.323101,0.324662,0.321280,0.323361,0.324402,0.322581,0.322320,0.324142,0.323361,0.329865,0.320760,0.327784,0.325182,0.319199,0.329084,0.330385,0.328044,0.325182,0.328824,0.328304,0.327523,0.324922,0.323101,0.327003,0.323881,0.329084,0.327003,0.324142,0.322841,0.323361,0.330905,0.328824,0.328824,0.325963,0.323621,0.330125,0.328044,0.321280
    ]

    # ok
    proposed = [
        0.085588,0.073621,0.078824,0.084547,0.082206,0.053330,0.094953,0.091051,0.081686,0.078044,0.074142,0.084287,0.083507,0.082466,0.078304,0.055931,0.070239,0.091051,0.063996,0.086889,0.083247,0.083767,0.082986,0.082986,0.092092,0.067118,0.083247,0.083767,0.081426,0.093652,0.079865,0.065036,0.035640,0.088450,0.084027,0.082726,0.078304,0.083507,0.091571,0.075702,0.077784,0.078304,0.084807,0.086629,0.067898,0.088450,0.087929
    ]

    data = [shivani2017, liu2018_k02, liu2018_k04, liu2018_k08, liu2018_k1, proposed]

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
    numDists = 6
    boxColors = ['darkkhaki', 'green', 'blue', 'red', '#c586c0', '#ade1f9']
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
            '[9]', '[6] k=0.2', '[6] k=0.4', '[6] k=0.8', '[6] k=1', 'Proposed'
        ],
        rotation=-30, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()