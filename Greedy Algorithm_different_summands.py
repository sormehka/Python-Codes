# Uses Python2
# The goal is to represent a given positive integer n as a sum of as many pairwise distinct positive integers as possible. That is, to find the maximum k such that n can be written as a sum of k integers a1, . . . , ak 
# Input: Single integer n
# Output: first line, maximum number k, second line, k pairwise distinct positive integers that sum up to n


n=int(input())
i=1

while n>2*i:
    n -= i
    i += 1
    
  
print i
if i==1:
    print n
else:
    print ' '.join(str(x) for x in range(1,i))+' '+str(n)
