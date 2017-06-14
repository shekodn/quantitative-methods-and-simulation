import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import math

# Set figure aesthetics
sns.set_style("white", {'ytick.major.size': 10.0})
sns.set_context("poster", font_scale=1.1)

# Load the data into DataFrames
train_users = pd.read_csv('train_users_2.csv')
test_users = pd.read_csv('test_users.csv')
sessions_users = pd.read_csv('sessions.csv')

# Merge train and test users
users = pd.concat((train_users, test_users), axis=0, ignore_index=True)
users.head()

users.gender.replace('-unknown-', np.nan, inplace=True)
users_nan = (users.isnull().sum() / users.shape[0]) * 100
users_nan[users_nan > 0].drop('country_destination')
users.age.describe()
users[users.age > 122]['age'].describe()
users[users.age < 18]['age'].describe()
users.loc[users.age > 95, 'age'] = np.nan
users.loc[users.age < 13, 'age'] = np.nan

########################################
categorical_features = [
    'affiliate_channel',
    'affiliate_provider',
    'country_destination',
    'first_affiliate_tracked',
    'first_browser',
    'first_device_type',
    'gender',
    'language',
    'signup_app',
    'signup_method'
]

for categorical_feature in categorical_features:
    users[categorical_feature] = users[categorical_feature].astype('category')

users['date_account_created'] = pd.to_datetime(users['date_account_created'])
users['date_first_booking'] = pd.to_datetime(users['date_first_booking'])
#print(users)
users['date_first_active'] = pd.to_datetime((users.timestamp_first_active // 1000000), format='%Y%m%d')


cleanUsers = users[users['date_first_booking'].notnull()]
cleanUsers = cleanUsers.sort_values(['id'], ascending=[1])
notCleanUseres = users[users['date_first_booking'].isnull()]
sessions_users.rename(columns={'user_id':'id'}, inplace=True)

#Plot de porcetaje de edades
plt.xlabel("Edad")
plt.ylabel("Porcentaje")
sns.distplot(cleanUsers.age.dropna(), color='#FD5C64')
plt.show()
sns.despine()

cleanUsers2013 = cleanUsers[cleanUsers['date_first_booking'] > pd.to_datetime(20130101, format='%Y%m%d')]
cleanUsers2013 = cleanUsers2013[cleanUsers2013['date_first_booking'] < pd.to_datetime(20140101, format='%Y%m%d')]
cleanUsers2013['date_first_booking'] = cleanUsers2013['date_first_booking'].astype("datetime64[ns]")
cleanUsers2013['date_first_booking'].groupby(cleanUsers2013['date_first_booking'].dt.month).count().plot(kind="bar")

# cleanUsers2013.date_first_booking.value_counts().plot(kind='line', linewidth=2, color='#FD5C64')
plt.show()

grpby = sessions_users.groupby(['id'])['secs_elapsed'].sum().reset_index()
grpby.columns = ['id','secs_elapsed']

cleanGroupSec = grpby[grpby['secs_elapsed'].notnull()]

##########################################

cleanSessions = cleanUsers.merge(cleanGroupSec, how="left")
cleanSessions = cleanSessions[~np.isnan(cleanSessions['secs_elapsed'])]
