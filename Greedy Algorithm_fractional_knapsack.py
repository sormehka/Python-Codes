# Uses Python2
# The goal is to use greedy algorithm for the fractional knapsack problem
# Input: first line is the number n of items and the capacity of the knapsack. The next n lines define the values and the weights of the items
# Output: the maximal value of fractions of items that fit into the knapsack.

S=raw_input()
[n,W]=S.split()
n=int(n)
W=int(W)
v=[]
we=[]
Total = 0

for i in range(0,n):
   M=raw_input()
   [m1,m2]=M.split()
   v.append([float(int(m1))/int(m2),float(int(m2))])

def getkey(item):
   return item[0]

v.sort(key=getkey, reverse=True)

j=0
while W>0 and j<n:
   if W<=v[j][1]:
      Total += W*v[j][0]
      break
   else:
      W -= v[j][1]
      Total += v[j][0]*v[j][1]
      j += 1
      
print "%.4f" % Total   

