import random;

def lim_correctos(x, n, x_max, x_min, num_prob,i):

    if num_prob <= 8:

        for j in range(n):

            if (x[i][j] < x_min[j]):

                x[i][j] = x_min[j] + random.random()*(x_max[j] - x_min[j]);

            elif x[i][j] > x_max[j]:

                x[i][j] = x_min[j] + random.random()*(x_max[j] - x_min[j]);

    return [x, n, x_max, x_min];




