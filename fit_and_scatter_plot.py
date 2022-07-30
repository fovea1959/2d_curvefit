#!/usr/bin/env python3

import numpy
import scipy.optimize
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import re
import json

graphWidth = 800  # units are pixels
graphHeight = 600  # units are pixels


def csv_from_ndarray(nd):
    line = str(nd)
    line = re.sub(r'^\[\s*', '', line)
    line = re.sub(r'\s*]$', '', line)
    line = re.sub(r'\s+', ' ', line)
    return ', '.join(line.split())


def do_plot(data, label, func):
    fittedParameters = None
    title = label + ' Surface Plot: ' + str(func)
    f = plt.figure(title, figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)

    # matplotlib.pyplot.grid(True)
    axes = Axes3D(f, auto_add_to_figure=False)

    axes.set_xlabel('screen x')
    axes.set_ylabel('screen y')
    axes.set_zlabel(label)

    # extract data from the single list
    x_data = data[0]
    y_data = data[1]
    z_data = data[2]

    f.add_axes(axes)

    if func is not None:
        xModel = numpy.linspace(min(x_data), max(x_data), 13)
        yModel = numpy.linspace(min(y_data), max(y_data), 13)
        X, Y = numpy.meshgrid(xModel, yModel)

        # here a non-linear surface fit is made with scipy's curve_fit()
        fittedParameters, pcov = scipy.optimize.curve_fit(func, [x_data, y_data], z_data)

        Z = func(numpy.array([X, Y]), *fittedParameters)

        print(type(fittedParameters), csv_from_ndarray(fittedParameters))

        axes.text2D(0.05, 0.95, csv_from_ndarray(fittedParameters), transform=axes.transAxes)

        # axes.plot_surface(..., cmap=cm.coolwarm)
        # axes.plot_surface(..., cmap=cm.coolwarm, alpha=0.1)
        # axes.plot_surface(..., alpha=0.1)
        axes.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=1, antialiased=True,
                          shade=False, color='red')

    axes.scatter(x_data, y_data, z_data)

    plt.show()
    plt.close('all')  # clean up after using pyplot or else there can be memory and process problems

    return fittedParameters


def extract_and_plot(d, label, func):
    x = []
    y = []
    z = []
    for row in d[label]:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
    data = [x, y, z]

    fittedParameters = do_plot(data, label, func)

    print(label, func, 'parameters', csv_from_ndarray(fittedParameters))

    zdiffTotal = 0
    for row in d[label]:
        z1 = row[2]
        zcalc = func(row, *fittedParameters)
        zdiff = abs(z1 - zcalc)
        zdiffTotal += zdiff
        print(label, func, row, zdiff)
    print(label, func, 'Total', zdiffTotal)


def func_x2y2(data, xa, xb, ya, yb, c):
    x = data[0]
    y = data[1]
    return x*x*xa + x*xb + y*y*ya + y*yb + c


def func_x2y2_xy(data, xya, xyb, xa, xb, ya, yb, c):
    x = data[0]
    y = data[1]
    return x*x*y*y*xya + x*y*xyb + x*x*xa + x*xb + y*y*ya + y*yb + c


def main():
    with open('data.json', 'r') as f:
        data = json.load(f)
    extract_and_plot(data, 'x', func_x2y2)
    extract_and_plot(data, 'x', func_x2y2_xy)
    extract_and_plot(data, 'y', func_x2y2)
    extract_and_plot(data, 'y', func_x2y2_xy)
    extract_and_plot(data, 'a', func_x2y2)
    extract_and_plot(data, 'a', func_x2y2_xy)
    extract_and_plot(data, 'd', func_x2y2)
    extract_and_plot(data, 'd', func_x2y2_xy)


if __name__ == '__main__':
    main()
