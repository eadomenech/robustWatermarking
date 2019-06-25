# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    shivani2017 = [
        0.457596,0.446930,0.452653,0.452133,0.454735,0.448751,0.452133,0.444849,0.446930,0.464620,0.442768,0.452133,0.449792,0.462279,0.449272,0.457856,0.449272,0.450052,0.448491,0.462279,0.453694,0.460198,0.466441,0.461238,0.448231,0.454475,0.461498,0.458897,0.460458,0.449792,0.450832,0.472164,0.467222,0.456816,0.456035,0.452914,0.459157,0.441727,0.469043,0.444589,0.460458,0.461238,0.454214,0.433923,0.462019,0.449532
    ]

    # ok
    liu2018_k02 = [
        0.366545,0.374089,0.359001,0.355619,0.377732,0.348595,0.363944,0.362903,0.366545,0.369147,0.363424,0.368366,0.375390,0.370187,0.359521,0.366025,0.372529,0.363424,0.356139,0.354839,0.363944,0.373829,0.371748,0.372529,0.373309,0.374610,0.354839,0.365765,0.357440,0.369407,0.359521,0.363163,0.364724,0.363944,0.353538,0.364464,0.368106,0.349376,0.356400,0.365245,0.369407,0.361342,0.368106,0.372008,0.366025,0.366805,0.361082,0.363163,0.370708,0.360822,0.370447,0.361342,0.361602,0.375130,0.368626,0.367066,0.365505,0.375650,0.361602,0.350937
    ]

    # ok
    liu2018_k04 = [
        0.326223,0.314776,0.334547,0.319979,0.323361,0.331165,0.319199,0.327003,0.320760,0.313476,0.322581,0.327523,0.326223,0.309834,0.322841,0.332986,0.324922,0.318158,0.320239,0.324922,0.316597,0.336108,0.328044,0.326223,0.316597,0.325963,0.332206,0.319979,0.325442,0.327003,0.322320,0.314516,0.313215,0.311394,0.327784,0.311394,0.317638,0.323361,0.322841,0.328564,0.307752,0.312955,0.324662,0.324402,0.322841,0.326743,0.319719,0.326743,0.321280,0.329865,0.324402,0.318939,0.313996,0.316597,0.316857,0.335328,0.315557,0.319459,0.328824,0.316337
    ]

    # ok
    liu2018_k08 = [
        0.319459,0.316597,0.318939,0.317378,0.316857,0.327263,0.315036,0.318418,0.311394,0.320499,0.309834,0.317638,0.323881,0.317638,0.320760,0.320499,0.318158,0.310874,0.322841,0.318939,0.317378,0.313476,0.310874,0.313215,0.308533,0.321020,0.308533,0.322060,0.310354,0.321280,0.325963,0.314256,0.323101,0.316337,0.313996,0.312695,0.312955,0.322320,0.318939,0.325442,0.313996,0.300989,0.312175,0.315557,0.320239,0.307752,0.309313,0.323361,0.316857,0.309834,0.325182,0.320499,0.320760,0.313736,0.312695,0.322841,0.310094,0.319719,0.315557,0.315036
    ]

    # ok
    liu2018_k1 = [
        0.306191,0.305931,0.297347,0.303330,0.309313,0.307752,0.305671,0.311655,0.308012,0.309834,0.309834,0.304370,0.307752,0.319719,0.313215,0.312695,0.308273,0.307492,0.307752,0.306972,0.306191,0.300989,0.303850,0.313996,0.314256,0.303590,0.303590,0.294485,0.317378,0.317898,0.307492,0.304110,0.316077,0.313215,0.311394,0.304891,0.308793,0.315297,0.309834,0.311134,0.306712,0.310614,0.314776,0.310874,0.318418,0.311915,0.311394,0.302549,0.306972,0.307492,0.313736,0.311134,0.315036,0.307492,0.314516,0.327263,0.306191,0.304891,0.306191,0.294225
    ]

    proposed = [
        0.021072,0.018991,0.017430,0.012747,0.019251,0.020031,0.019251,0.013528,0.016389,0.017690,0.019251,0.017690,0.016129,0.018210,0.013788,0.016129,0.018470,0.018470,0.017170,0.016649,0.017170,0.018470,0.016909,0.019771,0.018210,0.015088,0.017430,0.018730,0.015349,0.018730,0.016129,0.015869,0.014308,0.015609,0.017430,0.012487,0.021332,0.023153,0.018470,0.017690,0.018730,0.021592,0.017950,0.016649,0.019771,0.021852,0.017430,0.016649,0.020031,0.020812,0.012487,0.016649,0.021332,0.014828,0.018730,0.018730,0.019251,0.015609,0.017690,0.016909
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