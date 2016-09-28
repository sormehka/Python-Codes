# Uses Python2
# Binary search algorithm that allows searching very efficiently even huge lists, provided that the list is sorted
# Input: two sets of arrays: First array starts with an integer n, followed by a sorted sequence of n integers. Second array starts with integer k, followed by a sequence of k integers
# Output: for each i in range of 0 and k, return the index j in range 0 and n such that a[j]=b[i] or -1 if there is no such index. 

def binarysearch(a,array,left,right):
    re=-1
    if a==array[right]:
        re=right
    if a==array[left]:
        re=left
    while (a<array[right]) and (a>array[left]):
        mid=(right-left)/2
        if a<array[left+mid]:
            right=left+mid
        elif a>array[left+mid]:
            left += mid
        elif a==array[left+mid]:
            re=left+mid 
            break
        if mid==0:
            break
    return re


import sys
data=[]
for i in range(0,2):
    readdata=sys.stdin.readline()
    data += list(map(int,readdata.split()))

array1=data[1:data[0]+1]
array2=data[data[0]+2:]

out=''
for j in range(0,len(array2)):
    x=binarysearch(array2[j],array1,0,len(array1)-1)
    out += (str(x)+' ')
print out
    
