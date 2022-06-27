
import AG_1;
import AG_2;
import AG_3;
import AG_4;
import pandas as pd;
import matplotlib.pyplot as plt;
from scipy import stats;


datos2 = [AG_1.resultadosT_2_90_2000,AG_1.resultadosT_2_450_2000,AG_1.resultadosT_2_90_20000,AG_1.resultadosT_2_150_10000,AG_2.resultadosR_2_90_2000,AG_2.resultadosR_2_450_2000,AG_2.resultadosR_2_90_20000,AG_2.resultadosR_2_150_10000,AG_3.resultadosR2_2_90_2000,AG_3.resultadosR2_2_450_2000,AG_3.resultadosR2_2_90_20000,AG_3.resultadosR2_2_150_10000,AG_4.resultadosT2_2_90_2000,AG_4.resultadosT2_2_450_2000,AG_4.resultadosT2_2_90_20000,AG_4.resultadosT2_2_150_10000]

optimos2,individuos2 = [],[];


for i in range(16):
    for j in range(20):
        
        optimos2.append(datos2[i][j][0]) 

        individuos2.append(datos2[i][j][1] )

#Serie de todos los optimos obtenidos

op2 = pd.Series(optimos2);

op2_norm = (op2 - op2.mean())/(op2.std())

#Serie de los optimos obtenidos en cada algoritmo


op2_alg1 = op2[:80];
op2_alg2 = op2[80:160];
op2_alg3 = op2[160:240];
op2_alg4 = op2[240:320];

fig,ax = plt.subplots();
ax.boxplot(op2_alg1);
plt.show();

#Data frame con los individuos de las mejores soluciones


df_individuos2 = pd.DataFrame(individuos2);

#Data frame de los individuos por algoritmos



df_individuos2_alg1 = df_individuos2[:80]
df_individuos2_alg2 = df_individuos2[80:160]
df_individuos2_alg3 = df_individuos2[160:240]
df_individuos2_alg4 = df_individuos2[240:320]



#Problema 2

print("Resultados problema2 considerando todos los algoritmos:")
print(op2.describe())

print("Resultados problema2 con algoritmo1:")
print(op2_alg1.describe());

print("Resultados problema2 con algoritmo 2:")
print(op2_alg2.describe());

print("Resultados problema2 con algoritmo 3:")
print(op2_alg3.describe());

print("Resultados problema2 con algoritmo 4:")
print(op2_alg4.describe());

fig, ax = plt.subplots()
ax.hist(op2)
ax.set_title("Resultados todos los algoritmos")
plt.show()


#Resultados  problema 2 con los algoritmos

fig,ax = plt.subplots(2,2, sharex=(True), sharey = True);
ax[0,0].hist(op2_alg1,label= "Alg. 1")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op2_alg2,label= "Alg. 2", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op2_alg3,label= "Alg. 3", color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op2_alg4, label= "Alg. 4",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend();
plt.show()

#Problema 2 con Algoritmo 1 y las respectivas configuraciones

op2_alg1_config1 = op2_alg1[:20];
op2_alg1_config2 = op2_alg1[20:40];
op2_alg1_config3 = op2_alg1[40:60];
op2_alg1_config4 = op2_alg1[60:80];

print("Resultados algoritmo1 con configuracion1:")
print(op2_alg1_config1.describe())

print("Resultados algoritmo1 con configuracion2:")
print(op2_alg1_config2.describe());

print("Resultados algoritmo1 con configuracion3:")
print(op2_alg1_config3.describe());

print("Resultados  algoritmo1 con configuracion4:")
print(op2_alg1_config4.describe());



fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op2_alg1_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op2_alg1_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op2_alg1_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op2_alg1_config4,label="(150,10000)", color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend()
plt.show()

#Prorblema 2 con algoritmo 2 y respectivas configuraciones

op2_alg2_config1 = op2_alg2[:20];
op2_alg2_config2 = op2_alg2[20:40];
op2_alg2_config3 = op2_alg2[40:60];
op2_alg2_config4 = op2_alg2[60:80];

print("Resultados algoritmo2 con configuracion1:")
print(op2_alg2_config1.describe())

print("Resultados algoritmo2 con configuracion2:")
print(op2_alg2_config2.describe());

print("Resultados algoritmo2 con configuracion3:")
print(op2_alg2_config3.describe());

print("Resultados  algoritmo2 con configuracion4:")
print(op2_alg2_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op2_alg2_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op2_alg2_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op2_alg2_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op2_alg2_config4, label="(150,10000)",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend()
plt.show()

#Problema 2 con algoritmo 3 y respectivas conffiguraciones

op2_alg3_config1 = op2_alg3[:20];
op2_alg3_config2 = op2_alg3[20:40];
op2_alg3_config3 = op2_alg3[40:60];
op2_alg3_config4 = op2_alg3[60:80];

print("Resultados algoritmo3 con configuracion1:")
print(op2_alg3_config1.describe())

print("Resultados algoritmo3 con configuracion2:")
print(op2_alg3_config2.describe());

print("Resultados algoritmo3 con configuracion3:")
print(op2_alg3_config3.describe());

print("Resultados  algoritmo3con configuracion4:")
print(op2_alg3_config4.describe());

fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op2_alg3_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op2_alg3_config2, label="(450,2000)",color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op2_alg3_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op2_alg3_config4, label="(150,10000)",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend();
plt.show()

#Problema 2 con algoritmo 4 y respectivas conffiguraciones

op2_alg4_config1 = op2_alg4[:20];
op2_alg4_config2 = op2_alg4[20:40];
op2_alg4_config3 = op2_alg4[40:60];
op2_alg4_config4 = op2_alg4[60:80];

print("Resultados algoritmo2 con configuracion1:")
print(op2_alg4_config1.describe())

print("Resultados algoritmo2 con configuracion2:")
print(op2_alg4_config2.describe());

print("Resultados algoritmo2 con configuracion3:")
print(op2_alg4_config3.describe());

print("Resultados  algoritmo2 con configuracion4:")
print(op2_alg4_config4.describe());


fig,ax = plt.subplots(2,2,sharex=(True),sharey = True);
ax[0,0].hist(op2_alg4_config1,label="(90,2000)")
#ax[0,0].set_title("Resultados algoritmo 1")
ax[0,1].hist(op2_alg4_config2,label="(450,2000)", color = "red")
#ax[0,1].set_title("Resultados algoritmo 2")
ax[1,0].hist(op2_alg4_config3, label="(90,20000)",color ="orange")
#ax[1,0].set_title("Resultados algoritmo 3")
ax[1,1].hist(op2_alg4_config4, label="(150,10000)",color = "black")
#ax[1,1].set_title("Resultados algoritmo 4")
fig.legend()
plt.show()

print("TEST KRUSKAL-WALLIS")

print("------------")
print("Configuraciones:")
print(stats.kruskal(op2_alg1_config1,op2_alg2_config1,op2_alg3_config1,op2_alg4_config1))
print(stats.kruskal(op2_alg1_config2,op2_alg2_config2,op2_alg3_config2,op2_alg4_config2))
print(stats.kruskal(op2_alg1_config3,op2_alg2_config3,op2_alg3_config3,op2_alg4_config3))
print(stats.kruskal(op2_alg1_config4,op2_alg2_config4,op2_alg3_config4,op2_alg4_config4))

print("Configuracion 1 y comparativa 2 a 2:")
print(stats.kruskal(op2_alg1_config1,op2_alg2_config1))
print(stats.kruskal(op2_alg1_config1,op2_alg3_config1))
print(stats.kruskal(op2_alg1_config1,op2_alg4_config1))
print(stats.kruskal(op2_alg2_config1,op2_alg3_config1))
print(stats.kruskal(op2_alg2_config1,op2_alg4_config1))
print(stats.kruskal(op2_alg3_config1,op2_alg4_config1))

print("Configuracion 2 y comparativa 2 a 2:")
print(stats.kruskal(op2_alg1_config2,op2_alg2_config2))
print(stats.kruskal(op2_alg1_config2,op2_alg3_config2))
print(stats.kruskal(op2_alg1_config2,op2_alg4_config2))
print(stats.kruskal(op2_alg2_config2,op2_alg3_config2))
print(stats.kruskal(op2_alg2_config2,op2_alg4_config2))
print(stats.kruskal(op2_alg3_config2,op2_alg4_config2))

print("Configuracion 3 y comparativa 2 a 2:")
print(stats.kruskal(op2_alg1_config3,op2_alg2_config3))
print(stats.kruskal(op2_alg1_config3,op2_alg3_config3))
print(stats.kruskal(op2_alg1_config3,op2_alg4_config3))
print(stats.kruskal(op2_alg2_config3,op2_alg3_config3))
print(stats.kruskal(op2_alg2_config3,op2_alg4_config3))
print(stats.kruskal(op2_alg3_config3,op2_alg4_config3))

print("Configuracion 4 y comparativa 2 a 2:")
print(stats.kruskal(op2_alg1_config4,op2_alg2_config4))
print(stats.kruskal(op2_alg1_config4,op2_alg3_config4))
print(stats.kruskal(op2_alg1_config4,op2_alg4_config4))
print(stats.kruskal(op2_alg2_config4,op2_alg3_config4))
print(stats.kruskal(op2_alg2_config4,op2_alg4_config4))
print(stats.kruskal(op2_alg3_config4,op2_alg4_config4))


