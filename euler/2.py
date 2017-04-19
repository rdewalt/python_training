#!/usr/bin/python

# Project Euler #2
# Sum of all even fibbonachi numbers below 4 millon. 

# Success!

Sum=0
La=1 #Last Number A
Lb=1 #Last Number B
Goal = 4000000
Cs=La + Lb # Current Sum

while ( Cs < Goal) :
 Cs = La + Lb
 if Cs % 2 ==0: 
   Sum += Cs
 La=Lb
 Lb=Cs
print Sum
