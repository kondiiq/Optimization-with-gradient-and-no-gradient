from scipy import misc
import time
import matplotlib.pyplot as plt
import numpy as np
import math

#----------------------------------------------------------------------------------------#
# Function

def fonction(x1,x2):
    return - 1.0 * math.exp(-x1**2 - x2**2);

def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return misc.derivative(wraps, point[var], dx = 1e-6)

#----------------------------------------------------------------------------------------#
# Plot Function

x1 = np.arange(-500, 500, 0.1)
x2 = np.arange(-500, 500, 0.1)

xx1,xx2 = np.meshgrid(x1,x2);
z = 0
for i in range(3):
    z = ((xx1 ** 2 + xx2 ** 2) - i) ** 2

h = plt.contourf(x1,x2,z)
#plt.show()

#----------------------------------------------------------------------------------------#
# Gradient Descent
start = time.time()
alpha = 0.1 # learning rate
nb_max_iter = 1000 # Nb max d'iteration
eps = 0.0001 # stop condition

x1_0 = 1.0 # start point
x2_0 = 1.5
x2_0 = 1.5
z0 = fonction(x1_0, x2_0)
plt.scatter(x1_0, x2_0)

cond = eps + 10.0 # start with cond greater than eps (assumption)
nb_iter = 0
tmp_z0 = z0
while cond > eps and nb_iter < nb_max_iter:
    tmp_x1_0 = x1_0 - alpha * partial_derivative(fonction, 0, [x1_0, x2_0])
    tmp_x2_0 = x2_0 - alpha * partial_derivative(fonction, 1, [x1_0, x2_0])
    x1_0 = tmp_x1_0
    x2_0 = tmp_x2_0
    z0 = fonction(x1_0, x2_0)
    nb_iter = nb_iter + 1
    cond = abs( tmp_z0 - z0 )
    tmp_z0 = z0
    print( f"X:{x1_0}, Y:{x2_0}, Val:{cond}, iter:{nb_iter}")
    plt.scatter(x1_0, x2_0)

plt.title("Gradient Descent Python (Qing function)")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
end = time.time()
total_time = end - start
print(f"Execution of script is {total_time} time unit")