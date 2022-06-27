import AG_1;
import AG_2;
import AG_3;
import AG_4;
import pandas as pd;
import matplotlib.pyplot as plt;
from scipy import stats;


datos3 = [AG_1.resultadosT_6_90_2000,AG_1.resultadosT_6_450_2000,AG_1.resultadosT_6_90_20000,AG_1.resultadosT_6_150_10000,AG_2.resultadosR_6_90_2000,AG_2.resultadosR_6_450_2000,AG_2.resultadosR_6_90_20000,AG_2.resultadosR_6_150_10000,AG_3.resultadosR2_6_90_2000,AG_3.resultadosR2_6_450_2000,AG_3.resultadosR2_6_90_20000,AG_3.resultadosR2_6_150_10000,AG_4.resultadosT2_6_90_2000,AG_4.resultadosT2_6_450_2000,AG_4.resultadosT2_6_90_20000,AG_4.resultadosT2_6_150_10000]

optimos3, individuos3 = [],[];


for i in range(16):
    for j in range(20):
        

        optimos3.append(datos3[i][j][0])


        individuos3.append(datos3[i][j][1] )

#Serie de todos los optimos obtenidos


op3 = pd.Series(optimos3);

#Serie de los optimos obtenidos en cada algoritmo

op3_alg1 = op3[:80];
op3_alg2 = op3[80:160];
op3_alg3 = op3[160:240];
op3_alg4 = op3[240:320];

#Data frame con los individuos de las mejores soluciones



df_individuos3 = pd.DataFrame(individuos3);

#Data frame de los individuos por algoritmos


df_individuos3_alg1 = df_individuos3[:80]
df_individuos3_alg2 = df_individuos3[80:160]
df_individuos3_alg3 = df_individuos3[160:240]
df_individuos3_alg4 = df_individuos3[240:320]




#Problema 3

print("Resultados problema3 considerando todos los algoritmos:")
print(op3.describe())

print("Resultados problema3 con algoritmo1:")
print(op3_alg1.describe());

print("Resultados problema3 con algoritmo 2:")
print(op3_alg2.describe());

print("Resultados problema3 con algoritmo 3:")
print(op3_alg3.describe());

print("Resultados problema3 con algoritmo 4:")
print(op3_alg4.describe());

fig, ax = plt.subplots()
ax.hist(op3)
ax.set_title("Resultados todos los algoritmos")
plt.show()


#Resultados con cada algoritmo
fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op3_alg1, label = "Alg. 1")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op3_alg2, label = "Alg. 2",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op3_alg3, label = "Alg. 3",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op3_alg4, label = "Alg. 4",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend();
plt.show()

#Problema 3 con Algoritmo 1 y las respectivas configuraciones

op3_alg1_config1 = op3_alg1[:20];
op3_alg1_config2 = op3_alg1[20:40];
op3_alg1_config3 = op3_alg1[40:60];
op3_alg1_config4 = op3_alg1[60:80];

print("Resultados algoritmo1 con configuracion1:")
print(op3_alg1_config1.describe())

print("Resultados algoritmo1 con configuracion2:")
print(op3_alg1_config2.describe());

print("Resultados algoritmo1 con configuracion3:")
print(op3_alg1_config3.describe());

print("Resultados algoritmo1 con configuracion4:")
print(op3_alg1_config4.describe());


fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op3_alg1_config1, label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op3_alg1_config2, label="(450,2000)",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op3_alg1_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op3_alg1_config4, label="(150,10000)",color = "black")
fig.legend();
#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Prorblema 1 con algoritmo 2 y respectivas configuraciones

op3_alg2_config1 = op3_alg2[:20];
op3_alg2_config2 = op3_alg2[20:40];
op3_alg2_config3 = op3_alg2[40:60];
op3_alg2_config4 = op3_alg2[60:80];

print("Resultados algoritmo2 con configuracion1:")
print(op3_alg2_config1.describe())

print("Resultados algoritmo2 con configuracion2:")
print(op3_alg2_config2.describe());

print("Resultados algoritmo2 con configuracion3:")
print(op3_alg2_config3.describe());

print("Resultados  algoritmo2 con configuracion4:")
print(op3_alg2_config4.describe());


fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op3_alg2_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op3_alg2_config2, label="(450,2000)",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op3_alg2_config3,label="(90,20000)", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op3_alg2_config4, label="(150,10000)",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend();
plt.show()

#Problema 1 con algoritmo 3 y respectivas conffiguraciones

op3_alg3_config1 = op3_alg3[:20];
op3_alg3_config2 = op3_alg3[20:40];
op3_alg3_config3 = op3_alg3[40:60];
op3_alg3_config4 = op3_alg3[60:80];

print("Resultados algoritmo3 con configuracion1:")
print(op3_alg3_config1.describe())

print("Resultados algoritmo3 con configuracion2:")
print(op3_alg3_config2.describe());

print("Resultados algoritmo3 con configuracion3:")
print(op3_alg3_config3.describe());

print("Resultados  algoritmo3 con configuracion4:")
print(op3_alg3_config4.describe());


fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op3_alg3_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op3_alg3_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op3_alg3_config3, label="(90,20000)", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op3_alg3_config4, label="(150,10000)",color = "black")
fig.legend();
#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Problema 3 con algoritmo 4 y respectivas conffiguraciones

op3_alg4_config1 = op3_alg4[:20];
op3_alg4_config2 = op3_alg4[20:40];
op3_alg4_config3 = op3_alg4[40:60];
op3_alg4_config4 = op3_alg4[60:80];

print("Resultados algoritmo4 con configuracion1:")
print(op3_alg4_config1.describe())

print("Resultados algoritmo4 con configuracion2:")
print(op3_alg4_config2.describe());

print("Resultados algoritmo4 con configuracion3:")
print(op3_alg4_config3.describe());

print("Resultados  algoritmo4 con configuracion4:")
print(op3_alg4_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op3_alg4_config1, label = "(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op3_alg4_config2, label = "(450,2000)",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op3_alg4_config3, label = "(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op3_alg4_config4,label ="(150,10000)", color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend();
plt.show()

print("TEST KRUSKAL-WALLIS")

print("------------")
print("Configuraciones y comparativa de los 4:")
print(stats.kruskal(op3_alg1_config1,op3_alg2_config1,op3_alg3_config1,op3_alg4_config1))
print(stats.kruskal(op3_alg1_config2,op3_alg2_config2,op3_alg3_config2,op3_alg4_config2))
print(stats.kruskal(op3_alg1_config3,op3_alg2_config3,op3_alg3_config3,op3_alg4_config3))
print(stats.kruskal(op3_alg1_config4,op3_alg2_config4,op3_alg3_config4,op3_alg4_config4))

print("Configuracion 1 y comparativa 2 a 2:")
print(stats.kruskal(op3_alg1_config1,op3_alg2_config1))
print(stats.kruskal(op3_alg1_config1,op3_alg3_config1))
print(stats.kruskal(op3_alg1_config1,op3_alg4_config1))
print(stats.kruskal(op3_alg2_config1,op3_alg3_config1))
print(stats.kruskal(op3_alg2_config1,op3_alg4_config1))
print(stats.kruskal(op3_alg3_config1,op3_alg4_config1))

print("Configuracion 2 y comparativa 2 a 2:")
print(stats.kruskal(op3_alg1_config2,op3_alg2_config2))
print(stats.kruskal(op3_alg1_config2,op3_alg3_config2))
print(stats.kruskal(op3_alg1_config2,op3_alg4_config2))
print(stats.kruskal(op3_alg2_config2,op3_alg3_config2))
print(stats.kruskal(op3_alg2_config2,op3_alg4_config2))
print(stats.kruskal(op3_alg3_config2,op3_alg4_config2))

print("Configuracion 3 y comparativa 2 a 2:")
print(stats.kruskal(op3_alg1_config3,op3_alg2_config3))
print(stats.kruskal(op3_alg1_config3,op3_alg3_config3))
print(stats.kruskal(op3_alg1_config3,op3_alg4_config3))
print(stats.kruskal(op3_alg2_config3,op3_alg3_config3))
print(stats.kruskal(op3_alg2_config3,op3_alg4_config3))
print(stats.kruskal(op3_alg3_config3,op3_alg4_config3))

print("Configuracion 4 y comparativa 2 a 2:")
print(stats.kruskal(op3_alg1_config4,op3_alg2_config4))
print(stats.kruskal(op3_alg1_config4,op3_alg3_config4))
print(stats.kruskal(op3_alg1_config4,op3_alg4_config4))
print(stats.kruskal(op3_alg2_config4,op3_alg3_config4))
print(stats.kruskal(op3_alg2_config4,op3_alg4_config4))
print(stats.kruskal(op3_alg3_config4,op3_alg4_config4))
