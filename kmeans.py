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

def creacionDeArchivos(resultsK, resultsPCA, componentesPCA):
    f = open("KMeans.txt", "w")
    cont = 0
    for x in resultFromKMeans.labels_:
        f.write(str(cont) + ". " + str(x) + "\n")
        cont += 1
    f.close()

    f2 = open("PCA_Results.txt", "w")
    cont = 0
    for x in resultsPCA:
        f2.write(str(cont) + ". " + str(cleanSessions['id'][cont]) + "\t" + str(x) + "\n")
        cont += 1
    f2.write("Varianza de los 3 componentes (variables): " +  str(componentesPCA.explained_variance_[0]) + " " + str(componentesPCA.explained_variance_[1]) + " " + str(componentesPCA.explained_variance_[2]) + "\n")
    f2.close()


def printDeResultados(resultsK, componentesPCA):
    print("K-Means results: ", resultsK.labels_)
    print("PCA Componentes (3): ", componentesPCA.explained_variance_)


def simulateNewData(datosLinealesUno, datosLinealesDos, datosLinealesTres):
    for x in range(0, 10):
        print(np.random.choice(datosLinealesUno))


cleanSessions = pd.read_csv('Datos.csv')
cleanSessions['date_first_booking_number'] = cleanSessions['date_first_booking']


first_Booking = []
cont = 0
for x in cleanSessions['date_first_booking']:
    first_Booking.append(float((x[5:7])))
cleanSessions['firstBooking'] = np.asarray(first_Booking)

#Creation of numpy array
data = []
datosLinealesUno = []
datosLinealesDos = []
datosLinealesTres = []
cont = 0
for x in cleanSessions['bookingtime']:
    y = cleanSessions['firstBooking'][cont]
    z = cleanSessions['age'][cont]
    data.append(np.array([x,y,z]))
    datosLinealesUno.append(x)
    datosLinealesDos.append(y)
    datosLinealesTres.append(z)
    cont += 1

#Calculo de K-Means
resultFromKMeans = KMeans(n_clusters = 3, n_jobs = 2).fit(data)

#Calculo de componentes de PCA y valores de PCA
componentesPCA = PCA(n_components = 3).fit(data)
resultsPCA = PCA(n_components = 3).fit_transform(data)


simulateNewData(datosLinealesUno, datosLinealesDos, datosLinealesTres)

#Creacion de Archivos y impresion en terminal
creacionDeArchivos(resultFromKMeans, resultsPCA, componentesPCA)
printDeResultados(resultFromKMeans, componentesPCA)
