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

cleanSessions = pd.read_csv('Datos.csv')


cleanSessions['date_first_booking_number'] = cleanSessions['date_first_booking']

first_Booking = []

cont = 0
for x in cleanSessions['date_first_booking']:
    first_Booking.append(float((x[5:7])))

#cleanSessions.to_csv("Datos.csv")

cleanSessions['firstBooking'] = np.asarray(first_Booking)
#print(cleanSessions['bookingtime'])
KArray = [cleanSessions['bookingtime'], cleanSessions['firstBooking'], cleanSessions['age']]

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

# f = open("KMeans.txt", "w")
# cont = 0
# for x in resultFromKMeans.labels_:
#     f.write(str(cont) + ". " + str(x) + "\n")
#     cont += 1

pcaResults = PCA(n_components = 3).fit(data)
x1 = PCA(n_components = 3).fit_transform(data)

f = open("PCA_Results.txt", "w")
cont = 0
for x in x1:
    f.write(str(cont) + ". " + str(cleanSessions['id'][cont]) + "\t" + str(x) + "\n")
    cont += 1

f.write("Varianza de los 3 componentes (variables): " +  str(pcaResults.explained_variance_[0]) + " " + str(pcaResults.explained_variance_[1]) + " " + str(pcaResults.explained_variance_[2]) + "\n")

print("K-Means results: ", resultFromKMeans.labels_)
print("PCA Componentes (3): ", pcaResults.explained_variance_)
