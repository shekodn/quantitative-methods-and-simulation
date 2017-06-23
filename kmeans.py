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
from matplotlib import pylab
from dateutil import parser

cleanSessions = pd.read_csv('Datos.csv')

# cont = 0
# for x in cleanSessions['date_first_booking']:
#     if x[1] == '/':
#         cleanSessions['date_first_booking'][cont] = '0' + x
#     if cleanSessions['date_first_booking'][cont][4] == '/':
#         test = cleanSessions['date_first_booking'][cont]
#         cleanSessions['date_first_booking'][cont] = test[:3] + '0' + test[3:]
#     cont += 1
#     print(cleanSessions['date_first_booking'][cont])

#


cleanSessions['date_first_booking_number'] = cleanSessions['date_first_booking']

firstBooking = []

cont = 0
for x in cleanSessions['date_first_booking']:
    cleanSessions['date_first_booking_number'][cont] = datetime.strptime(x,'%Y-%m-%d')
    firstBooking.append(np.datetime64(cleanSessions['date_first_booking_number'][cont]).astype('uint64'))
    cont += 1


# cont = 0
# for x in cleanSessions['date_first_booking_number']:
#     cleanSessions['date_first_booking_number'][cont] = np.datetime64(x).astype('uint64') / 1e6
#     print(cleanSessions['date_first_booking_number'][cont])
#     cont += 1




#cleanSessions.to_csv("Datos.csv")


KArray = [cleanSessions['bookingtime'], firstBooking, cleanSessions['age']]
print("LISTO")
resultFromKMeans = KMeans(n_clusters = 2).fit(KArray)
print(resultFromKMeans.labels_)
