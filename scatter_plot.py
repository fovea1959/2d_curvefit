

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import json

graphWidth = 800  # units are pixels
graphHeight = 600  # units are pixels


def scatter_plot(data, label):
    title = label + ' Scatter Plot (click-drag with mouse)'
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

    axes.scatter(x_data, y_data, z_data)

    f.add_axes(axes)

    plt.show()
    plt.close('all')  # clean up after using pyplot or else there can be memory and process problems


def do_plot(d, label):
    x = []
    y = []
    z = []
    for row in d[label]:
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
    data = [x, y, z]
    scatter_plot(data, label)


def main():
    with open('data.json', 'r') as f:
        data = json.load(f)
    do_plot(data, 'x')
    do_plot(data, 'y')
    do_plot(data, 'a')
    do_plot(data, 'd')


if __name__ == '__main__':
    main()
