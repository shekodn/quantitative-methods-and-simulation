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
from fitter import Fitter

def creacionDeArchivos(resultsK, resultsPCA):
    f = open("KMeans.txt", "w")
    cont = 0
    for x in resultFromKMeans.labels_:
        f.write(str(cont) + ". " + str(x) + "\n")
        cont += 1

    f2 = open("PCA_Results.txt", "w")
    cont = 0
    for x in x1:
        f2.write(str(cont) + ". " + str(cleanSessions['id'][cont]) + "\t" + str(x) + "\n")
        cont += 1

    f2.write("Varianza de los 3 componentes (variables): " +  str(pcaResults.explained_variance_[0]) + " " + str(pcaResults.explained_variance_[1]) + " " + str(pcaResults.explained_variance_[2]) + "\n")

cleanSessions = pd.read_csv('Datos.csv')
cleanSessions['date_first_booking_number'] = cleanSessions['date_first_booking']


#TODO
# f = Fitter(cleanSessions['bookingtime'], distributions=["gamma", "expon", "norm", "weibull_min", "pareto"])
# f = Fitter(cleanSessions['bookingtime'], distributions=["norm"])
# f.fit()
# f.summary()

# Sessions
# Best fit = norm
stats.probplot(cleanSessions['bookingtime'], dist="norm", plot=pylab)
plt.show()



# first_Booking = []
# cont = 0
# for x in cleanSessions['date_first_booking']:
#     first_Booking.append(float((x[5:7])))
# cleanSessions['firstBooking'] = np.asarray(first_Booking)
#
# #Creation of numpy array
# data = []
# cont = 0
# for x in cleanSessions['bookingtime']:
#     y = cleanSessions['firstBooking'][cont]
#     z = cleanSessions['age'][cont]
#     data.append(np.array([x,y,z]))
#     cont += 1
#
# #Calculo de K-Means
# resultFromKMeans = KMeans(n_clusters = 3, n_jobs = 2).fit(data)
#
# #Calculo de componentes de PCA y valores de PCA
# componentesPCA = PCA(n_components = 3).fit(data)
# resultsPCA = PCA(n_components = 3).fit_transform(data)
#
# print("K-Means results: ", resultFromKMeans.labels_)
# print("PCA Componentes (3): ", componentesPCA.explained_variance_)
#
# creacionDeArchivos(resultFromKMeans, resultsPCA)
