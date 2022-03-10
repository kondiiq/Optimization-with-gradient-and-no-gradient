import numpy as np
import matplotlib as mpl


A = 1

def quin_sum():
    return



if __name__ == '__main__':
    if __name__ == '__main__':
        import numpy as np
        import matplotlib.pyplot as plt

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        x = np.arange(-10, 10, 0.1)
        y = np.arange(-10, 10, 0.1)
        x, y = np.meshgrid(x, y)
        res = 0
        for i in range(3):
            res = res + np.abs(x * np.sin(x) + 0.1 * x + y * np.sin(y) + 0.1 * y)

        ax.plot_surface(x, y, res, cmap='jet')
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Alpine function surface chart')
        plt.show()
        plt.contour(x, y, res)
        plt.xlabel('')
        plt.ylabel('')
        plt.title('Alpine function contour chart')
        plt.show()