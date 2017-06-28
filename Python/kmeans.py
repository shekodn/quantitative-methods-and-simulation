from __future__ import print_function
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math
from datetime import datetime
from matplotlib.finance import date2num
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import pylab
from dateutil import parser

def creacionDeArchivos(resultsK, resultsPCA, componentesPCA, newData, newCluster):

    #Resultados de clustering
    f = open('../Resultados/KMeans.txt', 'w')
    f.write("Numero\tID\tGrupo\n")
    cont = 0
    for x in resultFromKMeans.labels_:
        f.write(str(cont) + '\t' + str(cleanSessions['id'][cont]) + "\t"+ str(x) + '\n')
        cont += 1
    f.close()

    #Resultados del PCA
    f2 = open('../Resultados/PCA_Results.txt', 'w')
    f2.write("Numero\tID\t\tValores(Tiempo, Mes, Edad)\n")
    cont = 0
    for x in resultsPCA:
        f2.write(str(cont) + '\t' + str(cleanSessions['id'][cont]) + '\t' + str(x) + '\n')
        cont += 1
    f2.write('Varianza de los 3 componentes (variables): ' +  str(componentesPCA.explained_variance_[0]) + ' ' + str(componentesPCA.explained_variance_[1]) + ' ' + str(componentesPCA.explained_variance_[2]) + '\n')
    f2.close()

    #Resultados de clustering con nuevos datos
    f3 = open('../Resultados/NewData_Cluster.txt', 'w')
    #Archivos individuales para separar los grupos y analizarlos mejor
    f3_1 = open('../Resultados/NewData_Cluster_1.txt', 'w')
    f3_2 = open('../Resultados/NewData_Cluster_2.txt', 'w')
    f3_3 = open('../Resultados/NewData_Cluster_3.txt', 'w')
    f3.write('Numero\t\tGrupo\t\tTiempo\t\t\t\tMes\t\t\t\tEdad\n')
    f3_1.write('Numero\t\tGrupo\t\tTiempo\t\t\t\tMes\t\t\t\tEdad\n')
    f3_2.write('Numero\t\tGrupo\t\tTiempo\t\t\t\tMes\t\t\t\tEdad\n')
    f3_3.write('Numero\t\tGrupo\t\tTiempo\t\t\t\tMes\t\t\t\tEdad\n')
    for x in xrange(0,99):
        f3.write(str(x) + '\t\t' + str(newCluster[x]) + '\t\t' + str(newData[x][0]) + '\t\t\t' + str(newData[x][1]) + '\t\t\t' + str(newData[x][2]) + '\n')
        if newCluster[x] == 0:
            f3_1.write(str(x) + '\t\t' + str(newCluster[x]) + '\t\t' + str(newData[x][0]) + '\t\t\t' + str(newData[x][1]) + '\t\t\t' + str(newData[x][2]) + '\n')
        elif newCluster[x] == 1:
            f3_2.write(str(x) + '\t\t' + str(newCluster[x]) + '\t\t' + str(newData[x][0]) + '\t\t\t' + str(newData[x][1]) + '\t\t\t' + str(newData[x][2]) + '\n')
        else:
            f3_3.write(str(x) + '\t\t' + str(newCluster[x]) + '\t\t' + str(newData[x][0]) + '\t\t\t' + str(newData[x][1]) + '\t\t\t' + str(newData[x][2]) + '\n')
    f3.close()

def printDeResultados(resultsK, componentesPCA):
    print('K-Means results: ', resultsK.labels_)
    print('PCA Componentes (3): ', componentesPCA.explained_variance_)


def simulateNewData():
    newData = []
    #Datos aleatores de acuerdo a sus distribucion

    ##Tiempo para primer booking
    randomNorm = np.random.normal(50.872, 91.93, 100)

    ##Mes
    randomWeibull = np.random.weibull(1.6, 100)

    ##Edad
    randomGamma = np.random.gamma(5, 1, 100)

    #Normalizamos los datos sumando el minimo
    valorMin = min(randomNorm)
    for x in range(0, len(randomNorm)):
        randomNorm[x] += abs(valorMin)

    for l in xrange(0, 99):
        #Tiempo
        x = randomNorm[l]
        #Mes
        y = randomWeibull[l]
        #Edad
        z = randomGamma[l]
        newData.append(np.array([x, y, z]))
    return newData

####Arranque del codigo####
cleanSessions = pd.read_csv('../CSV/Datos.csv')
cleanSessions['date_first_booking_number'] = cleanSessions['date_first_booking']

first_Booking = []
cont = 0
for x in cleanSessions['date_first_booking']:
    first_Booking.append(float((x[5:7])))
cleanSessions['firstBooking'] = np.asarray(first_Booking)

#Creation of numpy array
data = []
cont = 0
for x in cleanSessions['bookingtime']:
    y = cleanSessions['firstBooking'][cont]
    z = cleanSessions['age'][cont]
    data.append(np.array([x,y,z]))
    cont += 1

#Calculo de K-Means
resultFromKMeans = KMeans(n_clusters = 3, n_jobs = 2).fit(data)

#Calculo de componentes de PCA y valores de PCA
componentesPCA = PCA(n_components = 3).fit(data)
resultsPCA = PCA(n_components = 3).fit_transform(data)

#Nuevos datos generados con distribuciones propias
newData = simulateNewData()
newCluster = resultFromKMeans.predict(newData)

#Creacion de Archivos y impresion en terminal
creacionDeArchivos(resultFromKMeans, resultsPCA, componentesPCA, newData, newCluster)
printDeResultados(resultFromKMeans, componentesPCA)
