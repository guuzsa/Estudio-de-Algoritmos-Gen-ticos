import math;
import random;
import pandas as pd;
import statistics;
import sort;


def funcion_objetivo(x,n_prob):

    n = len(x);

    if n_prob == 1:

        if n != 6:

            print("Error, la longitud del individuo debe ser 6");

        else:

            tetha = 2*math.pi / 100
            res = 0;

            for t in range(101):
                y_t = x[0] * (math.sin( x[1] * t * tetha + x[2] * math.sin( x[3] * t * tetha + x[4] * math.sin( x[4] * t * tetha) )));
                y_0 = 1 * (math.sin( 5 * t * tetha + 1.5 * math.sin( 4.8 * t * tetha + 2 * math.sin( 4.9 * t * tetha) )));
                res += (y_t - y_0)**2;


    elif n_prob == 2:

        if n%3 != 0: 

            print("Error pues el nº de variables debe ser multiplo de 3");

        else:

            n_atom = (n)//3; 
            res = 0;
            x_aux = sort.empaquetar_array(x,3);
    


            for i in range(n_atom-2): #Creo que es menos 2 por que cambiamos ir de 1 --> n-2 a 0 --> n-3
                for j in range(i+1,n_atom):
                    r_ij = math.sqrt( (x_aux[i][0]-x_aux[j][0] )**2 + (x_aux[i][1]-x_aux[j][1])**2 + (x_aux[i][2]-x_aux[j][2])**2); #Haciendolo asi creo que repito calculos
                    res += ( 1/ r_ij**12 ) - ( 2 / r_ij**6 );


    elif n_prob == 6:

        h_sum = [];
        m = 2*n -1;

        for j in range(1,2*m+1): #Realizamos este for para que el numero de fi_2i y fi_2i-1 no se vea alterado por el
        #cambio en los indices (sino iriamos de 0 a 2m-1);

            if j % 2 == 0: #Calculo de fi(2i)

                i = j // 2;
                h_sum.append(0);

                for k in range(i+1,n+1):

                    suma = 0;

                    for i1 in range(abs(2*i - k) + 1,k+1):
                        suma += x[i1-1];

                    h_sum[j-1] += math.cos(suma);
                h_sum[j-1] += 0.5;

            else:           #Calculo de fi(2i-1)
                i = (j+1) // 2;
                h_sum.append(0);

                for k in range(i,n+1):

                    suma = 0;

                    for i1 in range(abs(2*i - k -1) +1, k+1):
                        suma += x[i1-1];

                    h_sum[j-1] += math.cos(suma);

        res = max(h_sum);


    return res;





