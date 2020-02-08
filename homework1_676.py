#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 18:43:58 2020

@author: yuanyuanlin
"""

#question1
#(a)
list_1 = []
for i in range(1,21):
    list_1.append(i)
    
print(list_1)
    
#(b)
list_2 = []
for i in range(1,21):
    list_2.append(i)
list_2.sort(reverse=True)
print(list_2)


#(c)
list_3=list_1[0:19]+list_2
print(list_3)

#(d)
list=[4,6,3]
list_4=4*list
print(list_4)
del list_4[-2:]
print(list_4)

#(e)
list=[4,6,3]
list_5=11*list
print(list_5)
del list_5[-2:]
print(list_5)

#question2

import numpy as np
import math
number=np.arange(3,6.1,0.1)
list_6=[math.cos(x)*math.exp(x) for x in number]
print(list_6)

#question3
list_7=[]
for i in range(1,26):
    list_7.append(2**i/i)
    print(list_7)
  
#question4
#(a)
list_8=[]
for i in range(0:n+1):
    list_8=[a[i]-a[n-i]]

a=[i for i in range(1,21)]
listc=[a[i]-a[len(a)-i]for i in range(len(a))]
listd=[]



a = list_1
n = len(a)

# (a)
a_1st = a[0:n]

a_2nd = []
for i in a_1st:
    a_2nd.insert(0,i)
   
list_4a = []
for j in range(n):
    q4_a_value = a_1st[j] - a_2nd[j]
    list_4a.append(q4_a_value)

print(list_4a)



# (b)
list_4b = []   
for i in a:
    boolean_i = bool((i % 2) == 0)
    list_4b.append(boolean_i)

print(list_4b)


#question5
#(a)
output=open('lorem.txt','r')
text=''
for i in output:
    i=i.replace(",",'')
    i=i.replace('.','')
    text=text+i
text=text.split(' ')
ans=[]
for i in text:
    if 1<=len(i)<=4 or 4<=len(i)<=7 or len(i)>=8:
        ans.append(ans)
print("The number of strngs whose lenegths are: between 1 and 4, 4 and 7 and greater than or equal to 8 is:" + str(len(ans)))







# read the file
with open('lorem.txt','r') as lorem:
    # Read the contents into a string
    text = lorem.read()
    lorem.close()

# import the re module
import re

#specify the pattern
pat = re.compile('([a-zA-Z]{1,4})|\W([a-zA-Z]{4,7})\W|\W([a-zA-Z]{8,})\W')
print(pat)

# Use the findall method to find all matches.
match = pat.findall(text)
print(match)

# Create three lists to store the matches
one_four = []
four_seven = []
eight_longer = []

for m in match:
    # If this matched string's length is between 1 and 4
    if len(m[0]) > 0:
        one_four.append(m[0])
    # If this matched string's length is between 4 and 7
    elif len(m[1]) > 0:
        four_seven.append(m[1])
    else: # otherwise it's the other matched group (8 or greater)
        eight_longer.append(m[2])

#(b)        
Length=0
for i in text:
    for j in i:
        if j.isupper():
            Length+=1
print("Number of Capitalized characters is:"+' '+str(Length))
