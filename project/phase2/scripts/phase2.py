'''Phase 2 of ATA Capstone Project
 Mlworle 5/9/16
 python script to read munged last and who commands, data.dat and who.dat respectively.  See munged_data.sh for cleaning process.

The purpose of this script is to read the data from the files. And show some pertinent statistics on user consumption as indicated by time logged on.
Graphs will be provided as visualization to the statistics.

Please see, DTH_Network.ipynb for the development of this process.
'''

import pandas as pd
import matplotlib .pyplot as plt
import numpy as np

# Explore the data.dat file containing munged historical data from last command
data = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/l9.dat", sep=" ",names=["name", 'terminal','ip', 'DOW','month', 'date', 'total_time']) 

# correction to tr ":" "." in munge_data.sh
data['total_time']=data['total_time'].apply(lambda x : (np.floor(x)  + (x - np.floor(x))*(5/3))) 

# groupby() resembles sql...sweet!
data.groupby('name').total_time.sum()
data.groupby('name').total_time.max()
data.groupby('date').total_time.sum()
data.groupby('DOW').total_time.sum()

# some basic stats
data.total_time.max()
data.total_time.mean()
data.total_time.std()
data.total_time.min()


fig = plt.figure()
plt.plot(data.total_time)
plt.show()

plt.hist(data.total_time, bins=20)
plt.show()

plt.scatter(data.date, data.total_time)
plt.show()

plt.plot(data.groupby('name').total_time.cumsum())
plt.show()


who = pd.read_csv("/home/mragy/AkamaiAcademy/project/data/who.dat", sep=" ",names=["name", 'terminal','month', 'date', 'total_time', 'ip'])
who['total_time']=who['total_time'].apply(lambda x : (np.floor(x) + (x - np.floor(x))*(5/3))) 
who.groupby('name').total_time.max()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_title('Current Users\' Time vs Historical Time')
#ax.set_xlabel('Users')
#ax.set_ylabel('Time in Hours')
#ax.plot(data.total_time)
#ax.plot(who.total_time, color='r')
# this plot is confusing. change to boxplot

ax.set_xlabel('Time in Hours')
data['total_time'].plot(kind='box', color='b', label='Historical')
who['total_time'].plot(kind='box', color='r',label='Current')
#ax.legend()

#plt.show()
#save to file instead for longterm
plt.savefig('/home/mragy/AkamaiAcademy/project/graphs/box_current_vs_historical.pdf')





