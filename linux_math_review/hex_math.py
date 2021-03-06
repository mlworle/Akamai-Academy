# Akamai Academy Technical School
# Linux Command Line Review

# Review: hexidecimal math 

import random 

# Getting lazy. One RTFM for all.
def rtfm():
  print "Bummer. Check your notes and try again. I don\'t mean to be mean, but there are a lot of commands and I have limited attention span to write thes, so I\'m not going to put this in another loop and keep checking if the answe3rs are right or if they were typed correctly or case matters, blahblahblah. So just start the program over. Thanks!"


# 1st Gate: understand meaning of command
print "HI. Today we'll review of binary math.\r\n"
print "Remember, we count in the decimal system, which has place values as follows: \r"
print " ...  10,000    1,000   100     10    0 \r"
print " ...  10^4      10^3    10^2    10^1  10^0 \r\n"
print "Now it\'s your turn. Write the place values for base 16 or the binary system. Just go 4 places this time.\r"
place_values = raw_input(" ... ")

print "Bravo! You may continue.\r\n\n"


# Much practice
def conversion():
  decimal_number = random.randrange(0,100)
  answer = raw_input("Convert " + str(decimal_number) + " to hex: ")
  print("0x" + answer)
  print(hex(decimal_number))
  while "0x" + answer != str(hex(decimal_number)):
    answer = raw_input("Try again: ")
  print "Bravo!"


# Main
keep_trying = True
while keep_trying == True:
  conversion()
  keep_on = raw_input("Would you like to continue? y or n ")
  if keep_trying == "y": keep_trying = True
  else: keep_trying = False
print "Thank you for playing."
