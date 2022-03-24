import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.arange(-500, 500, 0.1)
    y = np.arange(-500, 500, 0.1)
    x, y = np.meshgrid(x, y)
    res = 0
    for i in range(3):
        res = res + ((x ** 2 + y ** 2) - i) ** 2

    ax.plot_surface(x, y, res, cmap='jet')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Qing function surface chart')
    plt.show()
    plt.contour(x, y, res)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Qing function contour chart')
    plt.colormaps()
    plt.colorbar(ax.plot_surface(x, y, res, cmap='jet'), shrink=1, aspect=5)
    plt.show()
    """
    x = np.arange(-500, 500, 0.1)
    y = np.arange(-500, 500, 0.1)
    tbh = 0
    for i in range(3):
        tbh = tbh + ((np.sqrt(i) ** 2 + np.sqrt(i) ** 2) - i) ** 2
        print(f'AEZAKKI{tbh}')
"""