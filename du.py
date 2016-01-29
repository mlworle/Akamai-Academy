# Akamai Academy Technical School
# Linux Command Line Review

# Command: df

answer = raw_input("HI. Today we'll review the df command. First of all, can you tell me what df means?  ")
if answer == "disk free":
  print "Bravo! You may continue."
  print
  print "At the virtual command line prompt type the command to run disk free."
  dfcommand = raw_input('$ ')
  if dfcommand == "df" or "df ":
      print "Awesome! You Rock!"
      print "Go on to the next command."
  else:
      print "Bummer, check your notes and start again."
else:
  print "Bummer, check your notes and try again. I don't mean to be mean, but there are a lot of commands and I have a limited time to write these, so I'm not going to put this in another loop and keep checking if the answers are right, or if they were typed correctly, or case matters, blahblahblah. So just start the program over.  Thanks!"

