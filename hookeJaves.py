import math
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
from matplotlib import pyplot as plt


class Alpine:
    def narysujFunkcje(self, x_tmps, y_tmps, z_tmps, x_b_zero,tmpStartowy,pokaz_sciezke):
        fig = plt.figure()
        ax = p3.Axes3D(fig)
        x = np.arange(-10, 10, 0.1)
        y = np.arange(-10, 10, 0.1)
        [X, Y] = np.meshgrid(x,y)
        Z = np.abs(X * np.sin(X) + 0.1 * X + Y * np.sin(Y) + 0.1 * Y)
        ax.plot_wireframe(X,Y,Z)
        ax.scatter([x_b_zero[0]], [x_b_zero[1]], [self.funkcja(x_b_zero)], color='r', s=20)
        if pokaz_sciezke:
            ax.scatter(x_tmps, y_tmps, z_tmps, color='y', alpha=1)
        ax.scatter([tmpStartowy[0]], [tmpStartowy[1]], [self.funkcja(tmpStartowy)], color='b')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Alpine function chart with Hooke-Jeevs  optimization method')
        plt.show()

    def funkcja(self, point):
        return point[0] ** 2 + point[1] ** 2


class Qing:
    def narysujFunkcje(self, x_tmps, y_tmps, z_tmps, x_b_zero,tmpStartowy,pokaz_sciezke):
        fig = plt.figure()
        ax = p3.Axes3D(fig)
        x = np.arange(-500, 500, 0.1)
        y = np.arange(-500, 500, 0.1)
        res = 0

        [X, Y] = np.meshgrid(x, y)
        for i in range(3):
            res = res + ((X ** 2 + Y ** 2) - i) ** 2
        Z = res
        ax.plot_wireframe(X, Y, Z)
        ax.scatter([x_b_zero[0]], [x_b_zero[1]], [self.funkcja(x_b_zero)], color='g', s=20)
        if pokaz_sciezke:
            ax.scatter(x_tmps, y_tmps, z_tmps, color='y', alpha=1)
        ax.scatter([tmpStartowy[0]], [tmpStartowy[1]], [self.funkcja(tmpStartowy)], color='r')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Qing function chart with Hooke-Jeevs  optimization method')
        plt.show()

    def funkcja(self, point, Y=None):
        if Y:
            X = point
            point = [X, Y]
        A = 1 +( ( point[0] + point[1] + 1 ) ** 2 ) * ( 19 - 14 * point[0] + 3 * point[1] ** 2 - 14 * point[1] + 6 * point[0] * point[1] + 3 * point[1] ** 2)
        B = 30 + (( 2 * point[0] - 3 * point[1]) ** 2) * ( 18 - 32 * point[0] + 12 * point[0] ** 2 + 48 * point[1] - 36 * point[0] * point[1] + 27 * point[1] ** 2)
        return A * B
