# Akamai Academy Technical School
# Linux Command Line Review

# Command: cat 

# Getting lazy. One RTFM for all.
def rtfm():
  print "Bummer. Check your notes and try again. I don\'t mean to be mean, but there are a lot of commands and I have limited attention span to write thes, so I\'m not going to put this in another loop and keep checking while the answe3rs are right or if they were typed correctly or case matters, blahblahblah. So just try again. Thanks!"


# 1st Gate: basic cat command
def cat():
  print "At the virtual command line prompt type the command to run disk usage. THis is the basic no-frills command. We'll get into more fancy stuff in a second.\r\n"
  catcommand = raw_input('$ ')
  while catcommand != "du":
    rtfm()
  print "Awesome! You Rock! Go on to the next command.\r"


# 2nd Gate: human readable form
def cat():
  print "Now type in the command for running disk usage with more easily understood output. (Hint: read this while you really want to because you are a human not a computer.) \r\n"
  cat_h_command = raw_input('$ ')
  while cat_h_command != "du -h":
    rtfm()
  print "Awesome! You Rock and Roll! We are done. Go on to the next command, or not. \r\n"


# 4th Gate: -f files only
def cat_f():
  print "Please type the command for disk usage for files."
  cat_f_command = raw_input('$ ')
  while cat_f_command != "du -f":
    rtfm()
  print "Fantastic. Move on.\r\n"

Main
definition()
cat()
cat_h()

