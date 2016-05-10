# Phase2 of ATA Capstone PRoject
# cron file to display graphs of munged last and who commands

import pandas as pd
import matplotlib .pyplot as plt
import numpy as np

# read in and give column names to the data from last command
# CHECK FILE PATH
data = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/l9.dat", sep=" ",names=["name", 'terminal','ip', 'DOW','month', 'date', 'total_time']) 

# correction to tr ":" "." in munge_data.sh
data['total_time']=data['total_time'].apply(lambda x : (np.floor(x)  + (x - np.floor(x))*(5/3))) 


# read in and give column names to the data from who command
# CHECK FILE PATH
who = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/who.dat", sep=" ",names=["name", 'terminal','month', 'date', 'total_time', 'ip'])

# correction to tr":" "." in munge_data.sh
who['total_time']=who['total_time'].apply(lambda x : (np.floor(x) + (x - np.floor(x))*(5/3))) 


# one figure with 4 graphs
fig = plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

# line graph of all past users and their total time online
ax1.set_title("Historical Total Time")
ax1.set_xlabel('total_time')
ax1.plot(data.total_time)

# line graph of all past users and their cumulative time logged on
ax2.set_title('Total Time by Index')
ax2.set_xlabel('name')
ax2.set_ylabel('Total Time CumSum')
ax2.plot(data.groupby('name').total_time.cumsum())

# histogram of all past users and thier total time logged on
ax3.set_title('Historical Total Time')
ax3.set_xlabel('total_time')
ax3.hist(data.total_time, bins=10)

# scatter plot of all past users total log-on times according to date
time = data.sort_values(by='date')
who_time = who.sort_values(by='date')
ax4.set_title("Total TIme vs Date")
ax4.set_xlabel('date')
ax4.set_ylabel('total time')
ax4.scatter(time.date, time.total_time)
ax4.scatter(who_time.date, who_time.total_time, color ='r')

# print to stdout
plt.show()
# print to file
# CHECK FILE PATH
# plt.savefig("aggregate_time_analysis.pdf")

