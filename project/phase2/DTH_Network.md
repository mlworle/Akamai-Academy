
# Akamai Technical Academy Capstone Project

#### This is an extension of the bash program for the team project. We are instructed to find all users online and offline at one time. We are advised to user SHell scripting and Python.  Testing and exploration will be done here, rather than the command line  in order to preserve the process. Mara Worle, lead architect 4/27/16


```python
import os,re
import numpy
import pandas as pd
```


```python
os.getcwd()
```


```python
os.system("w | awk '/mragy/ {print $1;}'")
```


```python
string = raw_input("Please enter the system information: \n")  
```


```python
 info = string.split(",")
```
Now its time to set up the python enviroment on my system.
That means creating a new virtualenv bubble.
$ mkdir <newproject>
$ cd <newproject>
$ virtualenv venv 
  # get installation notice here
$ . venv/bin/activate 
  # once the venv is activated look for 
  # (venv)path $ 
  # type away
$ deactivate
  # when done

```python
os.system("/home/mragy/AkamaiAcademy/project/virtualenv --version") 
```




    32512




```python
info= raw_input("Please enter the information: ")
info.split(" ")

```

    Please enter the information: mragy,:0





    ['mragy,:0']




```python
for i in info:
    if re.match('^[a-zA-Z0-9_-]{3,15}$',i):
        string = "w | awk \'/%s/ {print \'%s is online.\';}\' > /home/mragy/AkamaiAcademy/project/online" %(name, name)    
        online = os.system(string)
```


```python
os.listdir('/home/mragy/AkamaiAcademy/project/')
```




    ['docs',
     'check_status.py',
     'online',
     'check_sys.sh',
     'shared_functions.py',
     '.ipynb_checkpoints',
     'data',
     'diff_file',
     'venv',
     'DTH_Network.ipynb']




```python
os.system("cat online") 
# in iPython Notebook this will print to the console
# assigning os.system() to a variable still prints to the console
    
```


```python
# try putting all the valid information in an array of arrays
# compare to dictionary
valid_array = []
names=['one','two','three']
uids=['mguser1','mguser2','mguser3','mguser4']
terms=['tty1','tty2']
ips=[]
valid_array.append(names)
```


```python
valid_array.append(uids)
```


```python
valid_array.append(terms)
valid_array.append(ips)
```


```python
# if i want to get mguser2
valid_array[1][1]
```




    'mguser2'




```python
len(valid_array)
```




    4




```python
len(valid_array[3])
```




    0




```python
# now try a dictionary and choose the best datatype
valid_dict = {}
valid_dict['names']= names
valid_dict.update({'uids':uids})
valid_dict['terms']=terms
valid_dict['ips']=ips
```


```python
# to access mguser2
valid_dict["uids"][1]
```




    'mguser2'


I think this is more intuitive. Then we can access the type of data and compare repetitions.

```python
valid_dict['names'].append('four')
valid_dict['names']
```




    ['one', 'two', 'three', 'four']




```python
data = os.system("cat data.dat")
```


```python
data
```




    256



## Graphs 
Moving to graphing portion of the project. THe required search for online and offline users has been completed using shell scripting. gnuPlot would be another way to go with the graphing. hOwever, I'd like to bring in python to the project since the client suggested it.


```python
import pandas as pd
```


```python
last=pd.read_csv("/home/mragy/AkamaiAcademy/project/last_sq.txt", sep="\n", index_col=None)  
```


```python
last[:1]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mragy pts/1 :0 Tue May 3 18:02 still logged in</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mragy :0 :0 Tue May 3 17:58 still logged in</td>
    </tr>
  </tbody>
</table>
</div>




```python
# read the entire dataframe into one string
# then split according to line break or \n
last_arr=last.to_string(index=False).split('\n')
x=last_arr.__getitem__(1)
x.split(" ")
```




    ['',
     '',
     '',
     '',
     '',
     'mragy',
     ':0',
     ':0',
     'Tue',
     'May',
     '3',
     '17:58',
     'still',
     'logged',
     'in',
     '']




```python
data=[]
for i in range(len(last_arr)):
    x=last_arr.__getitem__(i)
    data.append(x.split(" "))
```


```python
data[1][5]
```




    'mragy'




```python
len(data)
```




    17




```python
# list comprehensions 
# https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
# squares = [x**2 for x in range(10)]
x= [data[i][1] for i in range(len(data))]
print(x)
```

    ['pts/1', '', 'system', '', '', 'system', '', '', '', 'system', '', '', 'system', 'mragy', '', 'system', '']



```python
print(data[10][12])
```

    



```python
# dir(x)
```

## Starting over
cleaning and munging the file in bash
used sed


```python
import pandas as pd
import numpy as np

file=pd.read_csv("/home/mragy/AkamaiAcademy/project/data/data.dat", sep=",", index_col=None) 
```


```python
# read the entire dataframe into one string
# then split according to line break or \n
string_file=file.to_string(index=False).split('\n')
#temp=string_file.__getitem__(1)
#temp.split(" ")

```


```python
arr=[]
for i in range(len(string_file)):
    x=string_file.__getitem__(i)
    arr.append(x.split(" "))
```


```python
arr[0][9]
```




    '00.00'




```python
#sum=0
#for i in range(len(arr)):
#    print(arr[i][9])
    #sum += int(arr[i][9])*(5/3)
#print(sum)
```


```python

```


```python
# put the array row in a dictionary with keys: 
# name, terminal, ip, DOW, month, date, time_on, time_off, total 

# try a list comprehension
# https://www.python.org/dev/peps/pep-0274/


dict={"name": [arr[k][0] for k in range(1-len(arr))]}
#, "terminal":[], "ip":[], "DOW":[], "month":[],"date":[],"time_on":[],"time_off":[],"total":[]} 
dict["name"]
```




    []




```python
for i in range(1-len(arr)):
    dict["name"].append(arr[i][0])
    dict["terminal"].append(arr[i][1])
    dict["ip"].append(arr[i][2])
    dict["DOW"].append(arr[i][3])
    dict["month"].append(arr[i][4])
    dict["date"].append(arr[i][5])
    dict["time_on"].append(arr[i][6])
    dict["time_off"].append(arr[i][8])
    dict["total"].append(arr[i][9])
```


```python
arr[0][1]
dict={"name":[], "terminal":[], "ip":[], "DOW":[], "month":[],"date":[],"time_on":[],"time_off":[],"total":[]} 
dict["name"].append("mara")
dict["name"].append("worle")
dict["name"]
```




    ['mara', 'worle']




```python
# I even thought about this!
cut -d" " -f1 data.dat > name.dat
cut -d" " -f2 data.dat > terminal.dat
cut -d" " -f3 data.dat > ip.dat
cut -d" " -f4,5,6 data.dat > date.dat
cut -d" " -f7,9 data.dat > time_on_off.dat
cut -d" " -f10 data.dat > total_time.dat
```

# Stats


```python
last.std()
```




    00.00    4.158048
    dtype: float64




```python
last.count()
```




    00.00    187
    dtype: int64




```python
x_data =[range(last.len)] 
y_data = [last.get_value(n,'1') for n in range(1,129)]  

fig = plt.figure(figsize=(10,6))
# create an axes obj
ax = fig.add_subplot(1,1,1)
# plot the data
ax.scatter(x_data, y_data, color="blue", marker="." ) 
# add axes labels
ax.set_xlabel("x")
ax.set_ylabel("y")
```

## Another Bash Munging

Cleaned the data some more
using cut to separate the fields


```python
import pandas as pd
import numpy as np

time=pd.read_csv("/home/mragy/AkamaiAcademy/project/data/total_time.dat", sep=",", index_col=None) 
```


```python
# time
```


```python
time.mean()*(5/3)
```




    00.00    3.670657
    dtype: float64




```python
time.std()*(5/3)
```




    00.00    2.629858
    dtype: float64




```python
time.max()
```




    00.00    9.49
    dtype: float64




```python
time.min()
```




    00.00    0.0
    dtype: float64



## Matplotlib
http://cs.smith.edu/dftwiki/index.php/MatPlotLib_Tutorial_1


```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
x_data = [range(len(time))] 
y_data = [time.get_value(n, "00.00") for n in range(len(time))]
```


```python
y_data
```




    [0.0,
     0.14000000000000001,
     0.16,
     3.0499999999999998,
     2.1499999999999999,
     2.1400000000000001,
     2.1600000000000001,
     2.1800000000000002,
     2.25,
     1.02,
     2.1099999999999999,
     3.1600000000000001,
     2.1299999999999999,
     2.29,
     2.2799999999999998,
     2.1699999999999999,
     2.3399999999999999,
     3.29,
     0.0,
     3.1099999999999999,
     0.57999999999999996,
     2.1800000000000002,
     2.2799999999999998,
     2.1299999999999999,
     2.3500000000000001,
     2.1699999999999999,
     2.1099999999999999,
     2.1800000000000002,
     2.1099999999999999,
     3.1299999999999999,
     3.3700000000000001,
     0.050000000000000003,
     2.3100000000000001,
     3.1800000000000002,
     2.2000000000000002,
     2.1099999999999999,
     3.1099999999999999,
     2.21,
     4.4800000000000004,
     2.2400000000000002,
     0.54000000000000004,
     4.2300000000000004,
     7.0700000000000003,
     2.1800000000000002,
     3.1099999999999999,
     5.1399999999999997,
     0.48999999999999999,
     3.25,
     8.1099999999999994,
     4.0999999999999996,
     0.32000000000000001,
     3.1099999999999999,
     3.1099999999999999,
     3.1099999999999999,
     2.1400000000000001,
     0.33000000000000002,
     0.029999999999999999,
     2.3700000000000001,
     0.02,
     2.2400000000000002,
     3.1899999999999999,
     3.1000000000000001,
     2.1099999999999999,
     0.089999999999999997,
     1.3400000000000001,
     0.52000000000000002,
     3.1099999999999999,
     0.34999999999999998,
     1.47,
     2.1699999999999999,
     2.21,
     0.01,
     2.2599999999999998,
     3.2599999999999998,
     5.1799999999999997,
     2.3999999999999999,
     0.10000000000000001,
     4.0999999999999996,
     2.1899999999999999,
     4.0599999999999996,
     2.2599999999999998,
     4.2599999999999998,
     5.3399999999999999,
     4.1100000000000003,
     2.48,
     2.1099999999999999,
     5.1100000000000003,
     0.040000000000000001,
     4.1100000000000003,
     1.1699999999999999,
     0.29999999999999999,
     1.47,
     4.2199999999999998,
     2.5299999999999998,
     1.04,
     2.1099999999999999,
     2.2200000000000002,
     0.16,
     2.2599999999999998,
     2.2799999999999998,
     2.2999999999999998,
     2.2999999999999998,
     2.3199999999999998,
     0.089999999999999997,
     2.1099999999999999,
     2.3700000000000001,
     3.1099999999999999,
     0.050000000000000003,
     0.02,
     2.3999999999999999,
     2.1400000000000001,
     3.1000000000000001,
     3.1000000000000001,
     3.1099999999999999,
     2.1600000000000001,
     2.1099999999999999,
     3.21,
     0.22,
     2.1099999999999999,
     2.1299999999999999,
     3.29,
     0.56999999999999995,
     2.1899999999999999,
     1.1299999999999999,
     5.1100000000000003,
     4.2199999999999998,
     0.14000000000000001,
     2.21,
     2.23,
     5.2800000000000002,
     3.1099999999999999,
     0.059999999999999998,
     2.1600000000000001,
     2.21,
     0.20000000000000001,
     0.17000000000000001,
     0.20000000000000001,
     2.21,
     2.4399999999999999,
     2.3500000000000001,
     2.3399999999999999,
     0.38,
     0.56000000000000005,
     2.1099999999999999,
     0.029999999999999999,
     2.1200000000000001,
     0.34999999999999998,
     2.4500000000000002,
     2.1499999999999999,
     2.1499999999999999,
     3.1099999999999999,
     3.1099999999999999,
     3.2799999999999998,
     3.1099999999999999,
     3.2799999999999998,
     0.040000000000000001,
     3.3199999999999998,
     3.3199999999999998,
     3.1099999999999999,
     3.3599999999999999,
     2.1400000000000001,
     1.3700000000000001,
     2.1099999999999999,
     1.26,
     3.1099999999999999,
     3.1200000000000001,
     2.3500000000000001,
     3.1200000000000001,
     2.4500000000000002,
     2.1899999999999999,
     3.1099999999999999,
     0.0,
     6.1100000000000003,
     4.0999999999999996,
     4.2000000000000002,
     2.5499999999999998,
     0.0,
     0.0,
     2.1099999999999999,
     3.1099999999999999,
     0.20000000000000001,
     7.1100000000000003,
     8.1500000000000004,
     2.1699999999999999,
     0.14999999999999999,
     0.12,
     5.1100000000000003,
     1.1599999999999999,
     0.28000000000000003,
     2.3900000000000001,
     0.51000000000000001,
     2.3799999999999999,
     2.1699999999999999,
     1.51,
     1.52,
     1.0800000000000001,
     4.1100000000000003,
     1.49,
     2.0099999999999998,
     1.3600000000000001,
     0.40999999999999998,
     0.46000000000000002,
     2.0600000000000001,
     2.1400000000000001,
     3.1899999999999999,
     4.3399999999999999,
     2.2799999999999998,
     0.02,
     2.0099999999999998,
     0.070000000000000007,
     2.0499999999999998,
     2.1600000000000001,
     2.2200000000000002,
     9.4900000000000002,
     0.16,
     2.4100000000000001,
     2.4199999999999999,
     0.37,
     2.5499999999999998,
     3.1400000000000001,
     0.22,
     8.1099999999999994,
     3.3999999999999999,
     2.1800000000000002,
     0.12,
     2.2400000000000002,
     3.1000000000000001,
     2.0,
     4.4000000000000004,
     4.4400000000000004,
     4.5,
     3.1000000000000001,
     0.5,
     3.1000000000000001,
     3.1000000000000001,
     0.45000000000000001,
     0.13,
     3.21,
     6.2300000000000004,
     5.0700000000000003,
     2.1099999999999999,
     5.0899999999999999,
     3.1000000000000001,
     5.1100000000000003,
     5.0999999999999996,
     0.059999999999999998,
     0.029999999999999999,
     0.11,
     2.29,
     2.2599999999999998,
     2.2799999999999998,
     0.55000000000000004,
     0.040000000000000001,
     2.2400000000000002,
     1.1200000000000001,
     1.3600000000000001,
     2.0,
     4.0,
     1.52,
     3.1000000000000001,
     0.01,
     3.2200000000000002,
     1.1299999999999999,
     2.3100000000000001,
     2.2400000000000002,
     3.2200000000000002,
     0.27000000000000002,
     2.1000000000000001,
     0.37,
     0.14000000000000001,
     4.1600000000000001,
     4.2199999999999998,
     0.55000000000000004,
     2.3199999999999998,
     0.37,
     1.26,
     2.2200000000000002,
     2.2799999999999998,
     2.1400000000000001,
     4.3899999999999997,
     2.1099999999999999,
     0.02,
     2.1499999999999999,
     2.1899999999999999,
     2.21,
     2.2200000000000002,
     2.2000000000000002,
     2.1899999999999999,
     3.1499999999999999,
     2.3799999999999999,
     3.1000000000000001,
     3.1000000000000001,
     3.1099999999999999,
     0.01,
     3.1099999999999999,
     3.1200000000000001,
     3.2400000000000002,
     3.0299999999999998,
     0.02,
     2.1200000000000001,
     3.1000000000000001,
     2.2799999999999998,
     2.1499999999999999,
     3.4100000000000001,
     1.5800000000000001,
     3.1099999999999999,
     2.1099999999999999,
     0.14000000000000001,
     0.01,
     0.0,
     0.0,
     2.1200000000000001,
     2.1099999999999999,
     2.21,
     0.070000000000000007,
     2.1299999999999999,
     0.050000000000000003,
     2.1099999999999999,
     0.01,
     2.1600000000000001,
     2.1099999999999999,
     0.20999999999999999,
     2.1899999999999999,
     2.3100000000000001,
     2.23,
     0.089999999999999997,
     2.1899999999999999,
     2.2200000000000002,
     0.080000000000000002,
     0.059999999999999998]




```python
fig1 = plt.figure()
ax1=fig1.add_subplot(111)
ax1.boxplot(y_data)
plt.show()
#fileName = "/home/mragy/AkamaiAcademy/project/graphs/boxplot1.png"
#fig1.savefig(fileName, format="png")
```


```python
fig2 = plt.figure()
ax2=fig2.add_subplot(111)
ax2.plot(y_data)
plt.show()
#fileName = "/home/mragy/AkamaiAcademy/project/graphs/plot1.png"
#fig2.savefig(fileName, format="png")
```

# PDF or Export Notebook
in order to make a pdf copy
sudo apt-get install pandoc
sudo apt-get install texlive-latex-base
or if that fails: just download as HTML and from the browser copy as pdf


# Python for Data Analysis, by Wes McKinney

haven't given up on pandas :)


```python
import pandas as pd
```


```python
data = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/l9.dat", sep=" ",names=["name", 'terminal','ip', 'DOW','month', 'date', 'total_time'])
```


```python
# corrects the replacement of ":" to "." in tr command

data['total_time']=data['total_time'].apply(lambda x : (np.floor(x)  + (x - np.floor(x))*(5/3)) 
```


```python
data.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>total_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>331.000000</td>
      <td>331.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>15.867069</td>
      <td>2.686589</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.503311</td>
      <td>1.661852</td>
    </tr>
    <tr>
      <th>min</th>
      <td>11.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>12.000000</td>
      <td>1.627778</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>15.000000</td>
      <td>2.827778</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>3.305556</td>
    </tr>
    <tr>
      <th>max</th>
      <td>27.000000</td>
      <td>10.361111</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.groupby('name')['total_time']
```


```python
data.groupby('name').total_time.sum()
```




    name
    mguser1     77.833333
    mguser10    44.650000
    mguser11    44.883333
    mguser12    62.800000
    mguser13    63.650000
    mguser14    79.883333
    mguser15    65.016667
    mguser17    63.066667
    mguser18    37.400000
    mguser19    62.750000
    mguser2     49.766667
    mguser20    66.566667
    mguser21    33.400000
    mguser29    85.866667
    mguser3     44.733333
    mguser4     71.200000
    mguser5     52.666667
    mguser6     38.233333
    mguser7     44.050000
    mguser8     63.633333
    mguser9     59.266667
    Name: total_time, dtype: float64




```python
data.groupby('name').total_time.max()
```




    name
    Apr   NaN
    Name: total_time, dtype: float64




```python
data.groupby('date').total_time.sum()
```




    date
    11     51.205556
    12    140.388889
    14    175.405556
    15    150.666667
    19    209.461111
    20    142.172222
    21     13.216667
    25      5.911111
    27      0.833333
    Name: total_time, dtype: float64




```python
data.groupby('DOW').total_time.sum()
```




    DOW
    Fri    150.666667
    Mon     57.116667
    Thu    188.622222
    Tue    349.850000
    Wed    143.005556
    Name: total_time, dtype: float64




```python

```


```python
data.total_time.std()
```




    1.6618522016109916




```python
users= data.sort_values(by='name')
users.index = range(1, len(users) + 1)
```


```python
users.groupby('name').total_time.sum()
```




    name
    mguser1     53.988889
    mguser10    36.016667
    mguser11    33.205556
    mguser12    46.000000
    mguser13    48.483333
    mguser14    54.205556
    mguser15    46.494444
    mguser17    46.444444
    mguser18    31.400000
    mguser19    43.783333
    mguser2     33.877778
    mguser20    49.077778
    mguser21    24.733333
    mguser29    57.777778
    mguser3     32.955556
    mguser4     52.533333
    mguser5     41.911111
    mguser6     28.522222
    mguser7     33.950000
    mguser8     46.322222
    mguser9     47.577778
    Name: total_time, dtype: float64




```python
users = users.sort('name')
```

    /home/mragy/anaconda3/lib/python3.5/site-packages/ipykernel/__main__.py:1: FutureWarning: sort is deprecated, use sort_values(inplace=True) for INPLACE sorting
      if __name__ == '__main__':



```python
time = data.sort_values(by='date')
```


```python
import matplotlib .pyplot as plt
```


```python
fig = plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

ax1.set_title("Historical Total Time")
ax1.set_xlabel('total_time')
ax1.plot(data.total_time)

ax2.set_title('Total Time by Index')
ax2.set_xlabel('name')
ax2.set_ylabel('Total Time CumSum')
ax2.plot(data.groupby('name').total_time.cumsum())

ax3.set_title('Historical Total Time')
ax3.set_xlabel('total_time')
ax3.hist(data.total_time, bins=10)

ax4.set_title("Total TIme vs Date")
ax4.set_xlabel('date')
ax4.set_ylabel('total time')
ax4.scatter(data.date, data.total_time)
plt.show()
```


```python
plt
plt.show()
```
# Munge who command
cat who.txt | tr -s " " > w1.dat
sed '/root/d' w1.dat > w2.dat
cat w2.dat | tr "-" " " > w3.dat
cat w3.dat | cut -d" " -f1,2,4,5,6,7 > w4.dat

```python
who = pd.read_csv("/home/mragy/AkamaiAcademy/project/data/phase2/who.dat", sep=" ",names=["name", 'terminal','month', 'date', 'total_time', 'ip'])
```


```python
# corrects replacement of ":" to "." in tr command

who['total_time']=who['total_time'].apply(lambda x : (np.floor(x) + (x - np.floor(x))*(5/3))) 
```


```python
who.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>month</th>
      <th>date</th>
      <th>total_time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.0</td>
      <td>6.0</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.328704</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.213305</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.083333</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.145833</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.347222</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.465278</td>
    </tr>
    <tr>
      <th>max</th>
      <td>4.0</td>
      <td>27.0</td>
      <td>8.611111</td>
    </tr>
  </tbody>
</table>
</div>




```python
who.groupby('name').total_time.max()
```




    name
    mguser14    22.305556
    mguser18    20.888889
    mguser2     22.333333
    mguser20    21.055556
    mguser4     22.472222
    mguser6     22.694444
    Name: total_time, dtype: float64




```python
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
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-44-0496da177f5c> in <module>()
         16 #plt.show()
         17 #save to file instead for longterm
    ---> 18 plt.savefig('/home/mragy/AkamaiAcademy/project/graphs/box_current_vs_historical.pdf')
    

    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/pyplot.py in savefig(*args, **kwargs)
        686 def savefig(*args, **kwargs):
        687     fig = gcf()
    --> 688     res = fig.savefig(*args, **kwargs)
        689     fig.canvas.draw_idle()   # need this if 'transparent=True' to reset colors
        690     return res


    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/figure.py in savefig(self, *args, **kwargs)
       1563             self.set_frameon(frameon)
       1564 
    -> 1565         self.canvas.print_figure(*args, **kwargs)
       1566 
       1567         if frameon:


    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/backends/backend_qt5agg.py in print_figure(self, *args, **kwargs)
        194 
        195     def print_figure(self, *args, **kwargs):
    --> 196         FigureCanvasAgg.print_figure(self, *args, **kwargs)
        197         self.draw()
        198 


    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/backend_bases.py in print_figure(self, filename, dpi, facecolor, edgecolor, orientation, format, **kwargs)
       2230                 orientation=orientation,
       2231                 bbox_inches_restore=_bbox_inches_restore,
    -> 2232                 **kwargs)
       2233         finally:
       2234             if bbox_inches and restore_bbox:


    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/backends/backend_pdf.py in print_pdf(self, filename, **kwargs)
       2526             file = filename._file
       2527         else:
    -> 2528             file = PdfFile(filename)
       2529         try:
       2530             file.newPage(width, height)


    /home/mragy/anaconda3/lib/python3.5/site-packages/matplotlib/backends/backend_pdf.py in __init__(self, filename)
        420         self.tell_base = 0
        421         if is_string_like(filename):
    --> 422             fh = open(filename, 'wb')
        423         elif is_writable_file_like(filename):
        424             try:


    FileNotFoundError: [Errno 2] No such file or directory: '/home/mragy/AkamaiAcademy/project/graphs/box_current_vs_historical.pdf'



```python
# what do I actually want to visualize here? 
# each use's individual current aggregate time against the historical spread
data.groupby('name').total_time.sum()
```




    name
    mguser1     46.70
    mguser10    26.79
    mguser11    26.93
    mguser12    37.68
    mguser13    38.19
    mguser14    47.93
    mguser15    39.01
    mguser17    37.84
    mguser18    22.44
    mguser19    37.65
    mguser2     29.86
    mguser20    39.94
    mguser21    20.04
    mguser29    51.52
    mguser3     26.84
    mguser4     42.72
    mguser5     31.60
    mguser6     22.94
    mguser7     26.43
    mguser8     38.18
    mguser9     35.56
    Name: total_time, dtype: float64



## End Phase2: Entering Phase2a



```python
import pandas as pd
import numpy as np
```


```python
data = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/l9.dat", sep=" ",names=["name", 'terminal','ip', 'DOW','month', 'date', 'total_time'])
```


```python
data['total_time']=data['total_time'].apply(lambda x : (np.floor(x)  + (x - np.floor(x))*(5/3)) 
```


```python
who = pd.read_csv("/home/mragy/AkamaiAcademy/project/phase2/data/who.dat", sep=" ",names=["name", 'terminal','month', 'date', 'total_time', 'ip'])
```


```python
who['total_time']
```




    0    7.52
    1    8.17
    2    8.09
    3    7.58
    4    8.03
    5    8.04
    Name: total_time, dtype: float64




```python
who['total_time']=who['total_time'].apply(lambda x : (np.floor(x) + (x - np.floor(x))*(5/3))) 
```


```python
who['total_time']
```




    0    8.444444
    1    8.472222
    2    8.250000
    3    8.611111
    4    8.083333
    5    8.111111
    Name: total_time, dtype: float64



# # Time Series Exploration
may need to import seaborn


```python
import seaborn as sns
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-120-ed9806ce3570> in <module>()
    ----> 1 import seaborn as sns
    

    ImportError: No module named 'seaborn'



```python
time = data.sort_values(by='date')
```


```python
who_time = who.sort_values(by='date')
```


```python
fig = plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

ax1.set_title("Historical Total Time")
ax1.set_xlabel('total_time')
ax1.plot(time.total_time)

ax2.set_title('Time by Index')
ax2.set_xlabel('name')
ax2.set_ylabel('Total Time CumSum')
ax2.plot(data.groupby('name').total_time.cumsum())

ax3.set_title('Total Time')
ax3.set_xlabel('total_time')
ax3.hist(time.total_time, bins=10)

ax4.set_title("Total TIme vs Date")
ax4.set_xlabel('date')
ax4.set_ylabel('total time')
ax4.scatter(time.date, time.total_time)
ax4.scatter(who_time.date, who_time.total_time, color='r')
plt.show()
```


```python

```


```python

```
