#!/bin/bash
# takes user input and finds if users are online
# also finds offline users
# NOTE: check_file.sh takes file input and process the same way


echo 'Please enter the information'
read info

# split the string $info into usable pieces
arr=$(echo $info | tr "," "\n")
for x in $arr
do
   echo "> [$x]"
   # check if grep returns anything
   users | grep "$x" | cut -d" " -f1 > temp
   if [ -s /temp ]
   then
      echo "$x is a valid user."
      cat temp >> on
   else
      echo "$x not valid input."
   fi
done

# remove repitions
if [ -s on ]
then
   sort on | uniq > online
   echo;echo;echo "ONLINE: "
   cat online
else
   echo;echo;echo "No users with those specifications are online. "
fi

# access login file and compare this to the w command
grep -v -f online /etc/passwd | sed '/mguser/!d' | cut -d":" -f1 > offline
if [ -s offline ]
then 
   # display online systems
   echo;echo;echo "OFFLINE"
   cat offline
else
   echo;echo;echo "No users are offline. "
fi


