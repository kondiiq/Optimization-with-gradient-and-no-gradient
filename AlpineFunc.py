import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    x, y = np.meshgrid(x, y)
    res = 0
    for i in range(3):
        res = res + np.abs(x * np.sin(x) + 0.1 * x + y * np.sin(y) + 0.1 * y)
        # print(f'{res}')
    ax.plot_surface(x, y, res, cmap='jet')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Alpine function surface chart')
    plt.show()
    plt.contour(x, y, res)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Alpine function contour chart')
    plt.colorbar(ax.plot_surface(x, y, res, cmap='jet'), shrink=1, aspect=5)
    plt.show()
"""
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    tbh = 0
    for i in range(3):
        tbh = tbh + np.abs(0.0000 * np.sin(0.0000) + 0.1 * 0.0000 + 2 * np.sin(0.0000) + 0.1 * 0.0000)
        print(f'AEZAKKI{tbh}')"""
