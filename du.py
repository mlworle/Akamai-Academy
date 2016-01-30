# Akamai Academy Technical School
# Linux Command Line Review

# Command: du

# Getting lazy. One RTFM for all.
def rtfm():
  print "Bummer. Check your notes and try again. I don\'t mean to be mean, but there are a lot of commands and I have limited attention span to write thes, so I\'m not going to put this in another loop and keep checking if the answe3rs are right or if they were typed correctly or case matters, blahblahblah. So just start the program over. Thanks!"


# 1st Gate: understand meaning of command
answer = raw_input("HI. Today we'll review the du command. First of all, can you tell me what du means?  ")
if answer == "disk usage":
  print "Bravo! You may move_on.\r\n\n"
else: rtfm()

# 2nd Gate: basic du command
print "At the virtual command line prompt type the command to run disk usage. THis is the basic no-frills command. We'll get into more fancy stuff in a second.\r\n"
ducommand = raw_input('$ ')
if ducommand == "du" or "du ":
  print "Awesome! You Rock! Go on to the next command.\r"
else: rtfm()

# 3rd Gate: human readable form
print "Now type in the command for running disk usage with more easily understood output. (Hint: read this if you really want to because you are a human not a computer.) \r\n"
du_h_command = raw_input('$ ')
if du_h_command == "du -h":
  print "Awesome! You Rock and Roll! We are done. Go on to the next command, or not. \r\n"
else: rtfm()

# 4th Gate: -f files only
print "Please type the command for disk usage for files."
du_f_command = raw_input('$ ')
if du_f_command == "du -f":
  print "Fantastic. Move on.\r\n"
else: rtfm()

# 5th Gate: -a all files and directories
print "What would you type to see all the files and directories?\r"
du_a_command = raw_input('$ ')
if du_a_command == "du -a":
  print "Great, keep going.\r\n"
else: rtfm()

# 6th Gate: -s all files and directories
print "What would you type to see only the last line?\r"
du_s_command = raw_input('$ ')
if du_s_command == "du -s":
  print "That\'s it. We\'re done. Check out another command.\r\n"
else: rtfm()
