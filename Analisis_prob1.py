import AG_1;
import AG_2;
import AG_3;
import AG_4;
import pandas as pd;
import matplotlib.pyplot as plt;
from scipy import stats;


datos1 = [AG_1.resultadosT_1_90_2000,AG_1.resultadosT_1_450_2000,AG_1.resultadosT_1_90_20000,AG_1.resultadosT_1_150_10000,AG_2.resultadosR_1_90_2000,AG_2.resultadosR_1_450_2000,AG_2.resultadosR_1_90_20000,AG_2.resultadosR_1_150_10000,AG_3.resultadosR2_1_90_2000,AG_3.resultadosR2_1_450_2000,AG_3.resultadosR2_1_90_20000,AG_3.resultadosR2_1_150_10000,AG_4.resultadosT2_1_90_2000,AG_4.resultadosT2_1_450_2000,AG_4.resultadosT2_1_90_20000,AG_4.resultadosT2_1_150_10000]

optimos1, individuos1 = [],[];


for i in range(16):
    for j in range(20):
        
        optimos1.append(datos1[i][j][0])

        individuos1.append(datos1[i][j][1]) 

#Serie de todos los optimos obtenidos

op1 = pd.Series(optimos1);


#Serie de los optimos obtenidos en cada algoritmo

op1_alg1 = op1[:80];
op1_alg2 = op1[80:160];
op1_alg3 = op1[160:240];
op1_alg4 = op1[240:320];

#Data frame con los individuos de las mejores soluciones


df_individuos1 = pd.DataFrame(individuos1);


#Data frame de los individuos por algoritmos

df_individuos1_alg1 = df_individuos1[:80]
df_individuos1_alg2 = df_individuos1[80:160]
df_individuos1_alg3 = df_individuos1[160:240]
df_individuos1_alg4 = df_individuos1[240:320]


#Problema 1

print("Resultados problema1 considerando todos los algoritmos:")
print(op1.describe())
fig, ax = plt.subplots()
ax.hist(op1)
ax.set_title("Resultados todos los algoritmos")
plt.show()

print("Resultados problema1 con algoritmo1:")
print(op1_alg1.describe());

print("Resultados problema1 con algoritmo 2:")
print(op1_alg2.describe());


print("Resultados problema1 con algoritmo 3:")
print(op1_alg3.describe());


print("Resultados problema1 con algoritmo 4:")
print(op1_alg4.describe());


fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op1_alg1, label="Alg. 1")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op1_alg2, label="Alg. 2",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op1_alg3, label="Alg. 3",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op1_alg4, label="Alg. 4",color = "black")
fig.legend();
#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Problema 1 con Algoritmo 1 y las respectivas configuraciones

op1_alg1_config1 = op1_alg1[:20];
op1_alg1_config2 = op1_alg1[20:40];
op1_alg1_config3 = op1_alg1[40:60];
op1_alg1_config4 = op1_alg1[60:80];

print("Resultados algoritmo1 con config1:")
print(op1_alg1_config1.describe());

print("Resultados algoritmo1 con config2:")
print(op1_alg1_config2.describe());


print("Resultados algoritmo1 con config3:")
print(op1_alg1_config3.describe());


print("Resultados algoritmo1 con config4:")
print(op1_alg1_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op1_alg1_config1, label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op1_alg1_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op1_alg1_config3,label="(90,20000)", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op1_alg1_config4,label="(150,10000)", color = "black")
fig.legend();

#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Prorblema 1 con algoritmo 2 y respectivas configuraciones

op1_alg2_config1 = op1_alg2[:20];
op1_alg2_config2 = op1_alg2[20:40];
op1_alg2_config3 = op1_alg2[40:60];
op1_alg2_config4 = op1_alg2[60:80];

print("Resultados algoritmo2 con config1:")
print(op1_alg2_config1.describe());

print("Resultados algoritmo2 con config2:")
print(op1_alg2_config2.describe());


print("Resultados algoritmo2 con config3:")
print(op1_alg2_config3.describe());


print("Resultados algoritmo2 con config4:")
print(op1_alg2_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op1_alg2_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op1_alg2_config2,label="(450,20000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op1_alg2_config3,label="(90,20000)", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op1_alg2_config4, label="(150,10000)",color = "black")
fig.legend();

#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Problema 1 con algoritmo 3 y respectivas conffiguraciones

op1_alg3_config1 = op1_alg3[:20];
op1_alg3_config2 = op1_alg3[20:40];
op1_alg3_config3 = op1_alg3[40:60];
op1_alg3_config4 = op1_alg3[60:80];

print("Resultados algoritmo3 con config1:")
print(op1_alg3_config1.describe());

print("Resultados algoritmo3 con config2:")
print(op1_alg3_config2.describe());


print("Resultados algoritmo3 con config3:")
print(op1_alg3_config3.describe());


print("Resultados algoritmo3 con config4:")
print(op1_alg3_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op1_alg3_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op1_alg3_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op1_alg3_config3,label="(90,20000)", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op1_alg3_config4,label="(150,10000)", color = "black")
fig.legend();
#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()

#Problema 1 con algoritmo 3 y respectivas conffiguraciones

op1_alg4_config1 = op1_alg4[:20];
op1_alg4_config2 = op1_alg4[20:40];
op1_alg4_config3 = op1_alg4[40:60];
op1_alg4_config4 = op1_alg4[60:80];

print("Resultados algoritmo4 con config1:")
print(op1_alg4_config1.describe());

print("Resultados algoritmo4 con config2:")
print(op1_alg4_config2.describe());


print("Resultados algoritmo4 con config3:")
print(op1_alg4_config3.describe());


print("Resultados algoritmo4 con config4:")
print(op1_alg4_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op1_alg4_config1, label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op1_alg4_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op1_alg4_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op1_alg4_config4, label="(150,10000)",color = "black")
fig.legend();

#ax[1,1].set_title("Resultados algoritmo 4")
plt.show()


print("TEST KRUSKAL-WALLIS")

print("------------")
print("Configuraciones y comparativa 4 a 4:")
print(stats.kruskal(op1_alg1_config1,op1_alg2_config1,op1_alg3_config1,op1_alg4_config1))
print(stats.kruskal(op1_alg1_config2,op1_alg2_config2,op1_alg3_config2,op1_alg4_config2))
print(stats.kruskal(op1_alg1_config3,op1_alg2_config3,op1_alg3_config3,op1_alg4_config3))
print(stats.kruskal(op1_alg1_config4,op1_alg2_config4,op1_alg3_config4,op1_alg4_config4))

print("Configuracion 1 y comparativa 2 a 2:")
print(stats.kruskal(op1_alg1_config1,op1_alg2_config1))
print(stats.kruskal(op1_alg1_config1,op1_alg3_config1))
print(stats.kruskal(op1_alg1_config1,op1_alg4_config1))
print(stats.kruskal(op1_alg2_config1,op1_alg3_config1))
print(stats.kruskal(op1_alg2_config1,op1_alg4_config1))
print(stats.kruskal(op1_alg3_config1,op1_alg4_config1))

print("Configuracion 2 y comparativa 2 a 2:")
print(stats.kruskal(op1_alg1_config2,op1_alg2_config2))
print(stats.kruskal(op1_alg1_config2,op1_alg3_config2))
print(stats.kruskal(op1_alg1_config2,op1_alg4_config2))
print(stats.kruskal(op1_alg2_config2,op1_alg3_config2))
print(stats.kruskal(op1_alg2_config2,op1_alg4_config2))
print(stats.kruskal(op1_alg3_config2,op1_alg4_config2))

print("Configuracion 3 y comparativa 2 a 2:")
print(stats.kruskal(op1_alg1_config3,op1_alg2_config3))
print(stats.kruskal(op1_alg1_config3,op1_alg3_config3))
print(stats.kruskal(op1_alg1_config3,op1_alg4_config3))
print(stats.kruskal(op1_alg2_config3,op1_alg3_config3))
print(stats.kruskal(op1_alg2_config3,op1_alg4_config3))
print(stats.kruskal(op1_alg3_config3,op1_alg4_config3))

print("Configuracion 4 y comparativa 2 a 2:")
print(stats.kruskal(op1_alg1_config4,op1_alg2_config4))
print(stats.kruskal(op1_alg1_config4,op1_alg3_config4))
print(stats.kruskal(op1_alg1_config4,op1_alg4_config4))
print(stats.kruskal(op1_alg2_config4,op1_alg3_config4))
print(stats.kruskal(op1_alg2_config4,op1_alg4_config4))
print(stats.kruskal(op1_alg3_config4,op1_alg4_config4))