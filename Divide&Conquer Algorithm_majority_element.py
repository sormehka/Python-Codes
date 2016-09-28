# Uses Python2
# Checks whether an input sequence contains a majority value or not
# Input: First line an integer n, second line a sequence of n non negative integers
# Output: 1 if the sequence has a majority value (occuring more than n/2 in the sequence) and 0 if the sequence does not have a majority

import sys
n=sys.stdin.readline()
input=sys.stdin.readline()

data=list(map(int,input.split()))

data.sort()

re=0
for i in range(0,int(n)-int(n)/2):
    if data[i]==data[i+int(n)/2]:
        re=1

print re
