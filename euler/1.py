#!/usr/bin/python

# Project Euler #1;
# Sum of all 3/5 factorable integers below 1000

##Successful.

x=0
for i in range(1000):
    if (i % 3==0) or (i % 5==0):
        x += i
print x
