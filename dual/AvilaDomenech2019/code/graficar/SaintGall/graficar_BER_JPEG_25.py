# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    shivani2017 = [
        0.417534,0.408689,0.389438,0.393861,0.375390,0.404527,0.393080,0.425078,0.396202,0.414152,0.386056,0.377211,0.374610,0.396722,0.388398,0.402445,0.404266,0.403486,0.396202,0.388918,0.422737,0.409469,0.373309,0.402706,0.403486,0.396462,0.388918,0.410510,0.382674,0.387877,0.373049,0.430541,0.428200,0.379032,0.407908,0.390739,0.398543,0.387357,0.422477,0.406868,0.389958,0.389958,0.412851,0.379553,0.425338,0.406608
    ]

    # ok
    liu2018_k02 = [
        0.381113,0.383715,0.375130,0.362903,0.395682,0.363424,0.379553,0.382154,0.384235,0.386316,0.374089,0.390739,0.381374,0.380593,0.362903,0.388398,0.392560,0.374870,0.379813,0.377471,0.378772,0.394901,0.388658,0.392040,0.387617,0.385536,0.362643,0.376951,0.370447,0.383455,0.370447,0.373309,0.372008,0.382414,0.370708,0.384495,0.386316,0.364204,0.381113,0.369927,0.378772,0.374610,0.382414,0.384235,0.374350,0.374089,0.366805,0.371228,0.388137,0.375390,0.385276,0.372529,0.375911,0.390219,0.376691,0.385016,0.385536,0.386837,0.375911,0.367326
    ]

    # ok
    liu2018_k04 = [
        0.382934,0.377732,0.386316,0.374610,0.389958,0.383455,0.379292,0.389698,0.374089,0.379292,0.386056,0.387357,0.375130,0.367066,0.375390,0.398803,0.389958,0.366545,0.375390,0.395421,0.376171,0.394641,0.382154,0.383195,0.375390,0.387097,0.389438,0.375911,0.383455,0.392560,0.376431,0.388658,0.374089,0.378772,0.388658,0.382414,0.381894,0.379813,0.381113,0.378252,0.372529,0.366025,0.381634,0.389698,0.376431,0.378772,0.375390,0.372789,0.378772,0.380853,0.392560,0.372789,0.381374,0.389698,0.370187,0.391519,0.376951,0.384755,0.384235,0.379813
    ]

    # ok
    liu2018_k08 = [
        0.344953,0.340271,0.343652,0.337929,0.346514,0.342092,0.338189,0.336368,0.328824,0.347555,0.337929,0.336108,0.339230,0.332206,0.326743,0.348335,0.341831,0.328044,0.349896,0.334807,0.333767,0.337669,0.341571,0.338450,0.340791,0.342352,0.333507,0.344953,0.346514,0.343392,0.344953,0.337409,0.342092,0.349376,0.328824,0.342092,0.335848,0.338970,0.340271,0.345213,0.344173,0.327263,0.330905,0.333507,0.340531,0.327784,0.328304,0.340791,0.340531,0.331426,0.354318,0.342092,0.329344,0.337669,0.335328,0.352497,0.332726,0.336108,0.335848,0.335068
    ]

    # ok
    liu2018_k1 = [
        0.341311,0.353018,0.331946,0.336368,0.344693,0.340271,0.344953,0.345473,0.350676,0.342092,0.342612,0.340531,0.339490,0.347555,0.347034,0.345473,0.342352,0.338710,0.351457,0.344693,0.342092,0.340010,0.336108,0.344953,0.348335,0.336368,0.335068,0.323881,0.348075,0.347815,0.334807,0.337149,0.349896,0.349116,0.338450,0.345734,0.345473,0.344953,0.345213,0.349116,0.350416,0.336368,0.353018,0.348855,0.346774,0.343392,0.350676,0.334027,0.348075,0.345473,0.344693,0.336889,0.347034,0.339750,0.347555,0.354839,0.340010,0.346514,0.335588,0.324142
    ]

    proposed = [
        0.021332,0.019511,0.018991,0.013528,0.020291,0.020031,0.020291,0.014828,0.016909,0.018470,0.020031,0.018470,0.016389,0.018470,0.014828,0.016389,0.019511,0.020031,0.017950,0.017430,0.018210,0.019771,0.017430,0.021332,0.018730,0.016389,0.017430,0.021332,0.016129,0.019251,0.016129,0.016129,0.014568,0.015609,0.018470,0.012487,0.022112,0.023673,0.019511,0.018470,0.019771,0.022112,0.018730,0.017170,0.020812,0.022112,0.018210,0.018210,0.020291,0.021852,0.013528,0.017950,0.021852,0.015088,0.019251,0.019251,0.019771,0.016389,0.019511,0.017430
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
    ax1.set_title('Saint Gall database (60 images)')
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