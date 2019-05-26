# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.432362,0.418574,0.441988,0.434964,0.437045,0.433143,0.431061,0.438606,0.445890,0.441207,0.434183,0.436785,0.442248,0.449792,0.427159
    ]

    # ok
    liu2018_k02 = [
        0.365765,0.368626,0.360822,0.370708,0.361342,0.360302,0.369147,0.362903,0.376691,0.368366,0.364724,0.369927,0.367066,0.358481,0.367326,0.362643,0.364204,0.364464,0.370447,0.365245,0.370708,0.362383,0.365245,0.364204,0.362383,0.362383,0.368887,0.369667,0.364464,0.369407,0.362643,0.354058,0.367066,0.363684,0.360822,0.373569,0.367586,0.369667,0.359781,0.368106,0.369407,0.363424,0.367066,0.366805,0.367326,0.368106,0.370708
    ]

    # ok
    liu2018_k04 = [
        0.380853,0.387097,0.377992,0.385796,0.383195,0.363163,0.384235,0.390479,0.382154,0.384495,0.366025,0.383455,0.379553,0.373049,0.379553,0.368626,0.383715,0.381113,0.392040,0.381374,0.387357,0.378772,0.395421,0.369667,0.376171,0.382934,0.380593,0.399063,0.374350,0.381894,0.377992,0.391779,0.373049,0.384755,0.387617,0.380593,0.382934,0.393080,0.380333,0.374870,0.387877,0.389958,0.392820,0.373829,0.381113,0.379813,0.368626
    ]

    # ok
    liu2018_k08 = [
        0.327263,0.345994,0.336889,0.324922,0.325702,0.322581,0.336889,0.347294,0.336629,0.323881,0.327523,0.330905,0.334287,0.332466,0.333247,0.328564,0.324922,0.322841,0.331946,0.327003,0.328304,0.321540,0.315297,0.328564,0.329344,0.335848,0.347294,0.339230,0.318158,0.316857,0.319459,0.312695,0.324922,0.321020,0.335328,0.342352,0.352497,0.343132,0.323881,0.319459,0.337409,0.332726,0.341311,0.322060,0.318939,0.338450,0.323101
    ]

    # ok
    liu2018_k1 = [
        0.283299,0.314256,0.285380,0.295005,0.286941,0.295786,0.292144,0.289282,0.287461,0.294485,0.287981,0.310354,0.303850,0.288762,0.286681,0.296306,0.286420,0.280957,0.311394,0.290323,0.302289,0.293704,0.293965,0.295265,0.297607,0.302029,0.309573,0.316077,0.292404,0.280697,0.289282,0.290062,0.289542,0.288241,0.288241,0.292144,0.314256,0.297867,0.285380,0.302549,0.304891,0.304370,0.283559,0.293704,0.280697,0.294745,0.283039
    ]

    # ok
    proposed = [
        0.085588,0.073621,0.078824,0.084547,0.082466,0.053330,0.094953,0.090531,0.081686,0.078044,0.074142,0.084287,0.083507,0.082466,0.078304,0.055931,0.070239,0.091051,0.063996,0.086889,0.083247,0.083507,0.082986,0.082986,0.091831,0.067118,0.083247,0.083767,0.080905,0.093392,0.079344,0.065036,0.035380,0.088450,0.084027,0.082726,0.078304,0.083507,0.091311,0.075702,0.077523,0.078044,0.084807,0.086368,0.067898,0.088450,0.087929
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