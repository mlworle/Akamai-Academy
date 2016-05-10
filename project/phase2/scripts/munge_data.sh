#!/bin/bash
# Phase 2 of Capstone Project
# Munge last command 
# Munge who command 
# Script to be used in cron to generate data for graphs
# This really uses up too much mem and is too clunky!
# Use awk
# Mworle 5/9/16

last > l1.dat
cat l1.dat | tr -s " " > l2.dat
#sed '/23.79.236.14/!d' l2.dat > l3.dat
cp l2.dat l3.dat
sed '/still logged/d' l3.dat > l4.dat
sed '/(/d' l4.dat > l5.dat
sed '/)/d' l5.dat > l6.dat
cat l6.dat | tr ":" "."  > data.dat # really bad, must *5/3
#rm l*.dat

# Munge who command
who > who.txt
cat who.txt | tr -s " " > wh1.dat
sed '/root/d' wh1.dat > wh2.dat
cat wh2.dat | tr "-" " " > wh3.dat

cat wh3.dat | cut -d" " -f1,2,4,5,6,7 > wh4.dat
cat wh4.dat | tr ":" "." > who.dat
rm wh*.dat
