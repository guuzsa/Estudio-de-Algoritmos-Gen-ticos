import math;
import random;
import pandas as pd;
import statistics;

def definir_limites(n,n_prob):

    x_min = [];
    x_max = [];

    if n_prob == 1:

        n = 6;

        for i in range(n):
            x_min.append(-6.4);
            x_max.append(6.35);

    elif n_prob == 2:

        n = 3*10; #Tomo 12 atomos para el problema, (30-3)/3 + 3 atomos

        for i in range(n):

            if i <= 1:

                x_min.append(0);
                x_max.append(4);

            elif i == 2:

                x_min.append(0);
                x_max.append(math.pi);

            else:

                x_min.append(-4 - (1/4) * math.floor( ( (i+1) - 4 ) / 3 ) );
                x_max.append(4 + (1/4) * math.floor( ( (i+1) - 4 ) / 3 ) );

    elif n_prob == 6:

        n = 20; #Consideramos R^20

        for j in range(n):

            x_min.append(0);
            x_max.append(math.pi);


    return [n, x_min, x_max]