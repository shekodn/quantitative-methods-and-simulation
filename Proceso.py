from __future__ import print_function
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math
import datetime
from scipy import stats
from matplotlib import pylab

sns.set_style("white", {'ytick.major.size': 10.0})
sns.set_context("poster", font_scale=1.1)

cleanSessions = pd.read_csv('Datos.csv')

cleanSessions['date_first_booking'] = pd.to_datetime(cleanSessions['date_first_booking'])
cleanSessions['date_account_created'] = pd.to_datetime(cleanSessions['date_account_created'])
cleanSessions['bookingtime'] = cleanSessions['date_first_booking'] - cleanSessions['date_account_created']


##Plot de porcetaje de edades
# plt.xlabel("Edad")
# plt.ylabel("Porcentaje")
# sns.distplot(cleanSessions.age.dropna(), color='#FD5C64')
# sns.despine()

##Plot de first booking en meses
#cleanSessions['date_first_booking'].groupby(cleanSessions['date_first_booking'].dt.month).count().plot(kind="bar")

##Plot de buckets de tiempo
#cleanSessions['bookingtime'].groupby(cleanSessions['bookingtime'].dt.days).count().plot(kind='line')


# plt.xlabel("Tiempo (Dias)")
# plt.ylabel("Cantidad (Bookings)")
# plt.show()

#Funciones
def printStatistics():
    row, minmax, mean, variance, skewness, kurtosis = stats.describe(cleanSessions['age'])
    print('*Age descriptive statistics*\n''rows: ', row, '\t', 'min and max: ', minmax, '\t', 'mean: ', '{0:.5g}'.format(mean), '\t', 'variance: ', '{0:.5g}'.format(variance), '\t', 'skewness: ', '{0:.5g}'.format(skewness), '\t', 'kurtosis: ', '{0:.5g}'.format(kurtosis), '\n')

    row, minmax, mean, variance, skewness, kurtosis = stats.describe(cleanSessions['bookingtime'].dt.days)
    print('*Sessions duration descriptive statistics*\n''rows: ', row, '\t', 'min and max: ', minmax, '\t', 'mean: ', '{0:.5g}'.format(mean), '\t', 'variance: ', '{0:.5g}'.format(variance), '\t', 'skewness: ', '{0:.5g}'.format(skewness), '\t', 'kurtosis: ', '{0:.5g}'.format(kurtosis), '\n')
