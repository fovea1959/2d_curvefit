#!/usr/bin/env python3

# from https://stats.stackexchange.com/a/446405

import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

graphWidth = 1200  # units are pixels
graphHeight = 900  # units are pixels

x = []
y = []
z = []
r = None

for i in range(100002):
    if i == 0:
        r = 1
    else:
        r = (r * 65539) % 2147483648
    v = r / 2147483648.0
    xyz = i % 3
    if xyz == 0:
        x.append(v)
    elif xyz == 1:
        y.append(v)
    else:
        z.append(v)

xData = numpy.array(x)
yData = numpy.array(y)
zData = numpy.array(z)
print(len(xData), len(yData), len(zData))

# place the data in a single list
data = [xData, yData, zData]
# print(data)


def ScatterPlot():
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)

    # matplotlib.pyplot.grid(True)
    axes = Axes3D(f, auto_add_to_figure=False)
    f.add_axes(axes)

    # extract data from the single list
    x_data = data[0]
    y_data = data[1]
    z_data = data[2]

    axes.scatter(x_data, y_data, z_data, s=1)

    axes.set_title('Scatter Plot (click-drag with mouse)')
    axes.set_xlabel('X Data')
    axes.set_ylabel('Y Data')
    axes.set_zlabel('Z Data')

    axes.view_init(elev=31., azim=-126)

    plt.show()
    plt.close('all')  # clean up after using pyplot or else there can be memory and process problems


if __name__ == "__main__":
    ScatterPlot()
