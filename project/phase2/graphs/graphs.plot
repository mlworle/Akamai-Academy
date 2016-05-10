#!/bin/gnuplot
set datafile separator ","
set autoscale fix
set key outside right center
set title "Total CPU Usage Over Time"
set output 'agg_cpu.png'
plot 'data.dat' using 1 title "Aggregate CPU Time" with line

