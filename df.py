# Akamai Academy Technical School
# Linux Command Line Review

# Command: df

# Getting lazy. One RTFM for all.
def rtfm():
  print "Bummer. Check your notes and try again. I don\'t mean to be mean, but there are a lot of commands and I have limited attention span to write thes, so I\'m not going to put this in another loop and keep checking if the answe3rs are right or if they were typed correctly or case matters, blahblahblah. So just start the program over. Thanks!"


# 1st Gate: understand meaning of command
answer = raw_input("HI. Today we'll review the df command. First of all, can you tell me what df means?  ")
if answer == "disk free":
  print "Bravo! You may continue.\r\n\n"

# 2nd Gate: basic df command
  print "At the virtual command line prompt type the command to run disk free. THis is the basic no-frills command. We'll get into more fancy stuff in a second.\r\n"
  dfcommand = raw_input('$ ')
  if dfcommand == "df" or "df ":
      print "Awesome! You Rock!\r"
      print "Go on to the next command.\r"

# 3rd Gate: human readable form
      print "Now type in the command for running disk free with more easily understood output. (Hint: read this if you really want to because you are a human not a computer.) \r\n"
      df_h_command = raw_input('$ ')
      if df_h_command == "df -h":
        print "Awesome! You Rock and Roll! We are done. Go on to the next command, or not. \r\n"

# 4th Gate: all others are false
      else: rtfm()
  else: rtfm()
else: rtfm()
