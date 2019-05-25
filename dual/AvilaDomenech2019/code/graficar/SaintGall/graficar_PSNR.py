# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        39.412400,37.953329,39.405832,38.916522,38.439209,37.999932,38.835189,37.935623,38.755422,37.274261,38.235718,37.396278,37.745851,37.487157,37.877802,37.422671,37.066242,38.170408,37.704153,37.574749,37.589621,37.812069,37.548741,37.335278,37.162564,37.086484,37.729254,37.735927,38.254805,38.744720,37.203511,37.621834,36.762054,38.031645,36.726871,37.931698,37.911517,39.595517,38.034024,37.400031,38.340388,37.830170,38.160768,39.374882,37.688412,37.946189,37.771573,37.482753,36.664810,36.918083,37.218706,37.204875,37.825845,36.613349,36.749791,38.279079,37.347104,36.789668,36.474545,36.135333]

    # ok
    liu2018_k02 = [
        32.341864,32.109268,32.056192,32.123270,32.133641,32.126601,32.248303,32.193186,32.300735,32.115689,32.095046,31.924626,32.315135,32.092707,32.106197,32.783785,32.818154,32.384344,32.183988,32.221451,32.322031,32.136301,32.099759,32.401152,32.020466,31.995531,32.229249,32.112703,32.217392,32.262832,32.391492,32.403716,32.406374,32.178923,32.001054,32.193924,32.116301,32.418423,32.048152,32.219377,32.070396,32.203240,32.211249,32.382410,32.307814,32.153932,32.580226,32.022377,32.097460,32.087999,32.553910,31.961131,31.929909,32.484225,32.440164,32.851949,32.397438,32.597433,31.821383,32.173026
    ]

    # ok
    liu2018_k04 = [
        32.331859,32.099708,32.047146,32.114249,32.124376,32.117772,32.238632,32.183696,32.291386,32.106276,32.085908,31.915775,32.305541,32.083716,32.096823,32.773287,32.807384,32.375036,32.174672,32.211941,32.312572,32.126755,32.091025,32.391724,32.011642,31.986562,32.220199,32.103485,32.208090,32.253663,32.381753,32.393859,32.396742,32.169662,31.992176,32.184354,32.107401,32.408561,32.039222,32.210420,32.061283,32.193790,32.202004,32.372529,32.298031,32.144885,32.569942,32.013397,32.088313,32.079328,32.543880,31.952614,31.921091,32.474193,32.431124,32.841649,32.388008,32.587619,31.813161,32.163924
    ]

    # ok
    liu2018_k08 = [
        32.294633,32.063893,32.012796,32.076545,32.086859,32.081309,32.199690,32.148278,32.253113,32.069894,32.048987,31.880673,32.267965,32.047108,32.060025,32.730091,32.765740,32.335753,32.136097,32.174962,32.273279,32.092789,32.054260,32.351335,31.977315,31.951984,32.183900,32.067554,32.170534,32.214676,32.343467,32.355469,32.358969,32.133309,31.958004,32.147989,32.071266,32.370201,32.001832,32.174043,32.024930,32.155035,32.165214,32.335000,32.260566,32.109697,32.527628,31.978408,32.052279,32.043006,32.503074,31.917288,31.886424,32.434650,32.389193,32.799574,32.347449,32.545690,31.779306,32.127048
    ]

    # ok
    liu2018_k1 = [
        32.268661,32.038639,31.987085,32.052579,32.059333,32.055270,32.173065,32.117664,32.225505,32.042894,32.023321,31.855492,32.238837,32.022696,32.036444,32.700308,32.732546,32.307294,32.110225,32.146682,32.245212,32.063030,32.026267,32.324742,31.949959,31.926676,32.154388,32.039447,32.146078,32.186361,32.315289,32.325098,32.327800,32.106079,31.930036,32.122688,32.042781,32.339795,31.977134,32.147077,31.997758,32.130351,32.136560,32.306262,32.232062,32.081547,32.502564,31.953081,32.025146,32.016595,32.474235,31.892747,31.862776,32.408114,32.362409,32.763300,32.316352,32.516532,31.753926,32.098226
    ]

    proposed = [
        47.878285,47.853420,48.046414,47.907034,47.939477,47.735455,47.935446,47.854021,48.042707,48.057450,47.922732,47.890937,48.039144,47.941093,47.888722,48.052789,47.899229,47.838873,47.879789,48.114369,47.995086,47.864612,47.945915,48.057047,47.821185,47.923829,47.894378,47.893424,48.005227,47.908769,47.802983,47.909813,47.961407,48.023033,47.846028,47.950894,47.825479,47.810997,47.854622,47.887811,47.953857,48.050256,48.069505,47.921089,47.801456,47.899878,47.760746,47.884980,47.952854,47.921674,47.749830,47.810677,47.889319,47.923516,47.834536,47.942949,47.874924,47.914484,47.852892,47.995507
    ]

    data = [shivani2017, liu2018_k02, liu2018_k04, liu2018_k08, liu2018_k1, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('PSNR')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.15)

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
    ax1.set_ylabel('PSNR')

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