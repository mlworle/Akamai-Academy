# Lead architect, Mara Worle

Phase 2 of the ATA Capstone Project.

Phase 1 was to create a command line tool that will determine if 'systems', aka users, are online or offline depending on user input or file. Bonus to create a contab job to do this task at regular intervals. 

Goals: 
* create a python script to 
   - pull total time from the last column of last command to do the following stats:
      . mean, standard deviation: for each individual user and all users 
      . alert the console if a user if +2sd above their mean or the aggregate mean
   - create a graph of the user's current aggregate use against their historial usage. this could be a line graph x-axis is date, y-axis total time.
   - heat map of all users aggregate usage. x-value users, y value ??????

   - use matplotlib to create the graphs
* use Flask to upload to a website and showcase the ipython notebook
* as a bonus, write a testing suite with unittest


