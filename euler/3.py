#!/usr/bin/python

# Project Euler #
# Largest Prime Factor of 600851475143

# Solved!

x=600851475143
lpf=2

while (x>lpf):
    if (x%lpf==0):
        x=x/lpf
        lpf=2
    else:
        lpf+=1
print x
