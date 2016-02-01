# Akamai Academy Technical School
# Linux Command Line Review

# Command: du

# Getting lazy. One RTFM for all.
def rtfm():
  print "Bummer. Check your notes and try again. I don\'t mean to be mean, but there are a lot of commands and I have limited attention span to write thes, so I\'m not going to put this in another loop and keep checking while the answe3rs are right or if they were typed correctly or case matters, blahblahblah. So just try again. Thanks!"


# 1st Gate: understand meaning of command
def definition():
  answer = raw_input("HI. Today we'll review the du command. First of all, can you tell me what du means?  ")
  while answer != "disk usage":
    rtfm()
  print "Bravo! You may move_on.\r\n\n"


# 2nd Gate: basic du command
def du():
  print "At the virtual command line prompt type the command to run disk usage. THis is the basic no-frills command. We'll get into more fancy stuff in a second.\r\n"
  ducommand = raw_input('$ ')
  while ducommand != "du":
    rtfm()
  print "Awesome! You Rock! Go on to the next command.\r"


# 3rd Gate: human readable form
def du_h():
  print "Now type in the command for running disk usage with more easily understood output. (Hint: read this while you really want to because you are a human not a computer.) \r\n"
  du_h_command = raw_input('$ ')
  while du_h_command != "du -h":
    rtfm()
  print "Awesome! You Rock and Roll! We are done. Go on to the next command, or not. \r\n"


# 4th Gate: -f files only
def du_f():
  print "Please type the command for disk usage for files."
  du_f_command = raw_input('$ ')
  while du_f_command != "du -f":
    rtfm()
  print "Fantastic. Move on.\r\n"


# 5th Gate: -a all files and directories
def du_a():
  print "What would you type to see all the files and directories?\r"
  du_a_command = raw_input('$ ')
  while du_a_command != "du -a":
    rtfm()
  print "Great, keep going.\r\n"


# 6th Gate: -s all files and directories
def du_s():
  print "What would you type to see only the last line?\r"
  du_s_command = raw_input('$ ')
  while du_s_command != "du -s":
    rtfm()
  print "That\'s it. We\'re done. Check out another command.\r\n"

# Main
definition()
du()
du_h()
du_f()
du_a()
du_s()
