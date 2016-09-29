# Uses Python2
# The goal is to find the minumum number of operations to get an integer n. The operations are only multiply by 3, multiply by 2, and add 1
# Input: integer n
# Output: first line is the minumium number of operations k, the second line is the sequence of intermediate numbers

n=input()
ways=[0 for x in range(0,int(n)+1)]

def next(j):
	p1=j+1
	p2=j*2
	p3=j*3
	return([p1,p2,p3])

for i in range(1,n+1):
	p=next(i)
	if p[0]<=n:
		if ways[p[0]]==0 or ways[p[0]]>(ways[i]+1):
			ways[p[0]]=ways[i]+1	
	if p[1]<=n: 
		if ways[p[1]]==0 or ways[p[1]]>(ways[i]+1):
			ways[p[1]]=ways[i]+1
	if p[2]<=n: 
		if ways[p[2]]==0 or ways[p[2]]>(ways[i]+1):
			ways[p[2]]=ways[i]+1
		
print(ways[n])

out=[str(n)]
while n>1:
	if ways[n]==(ways[n-1]+1):
		out.extend([str(n-1)])
		n=n-1
	elif n%3==0 and ways[n]==(ways[n/3]+1):
		out.extend([str(n/3)])
		n=n/3
	elif n%2==0 and ways[n]==(ways[n/2]+1):
		out.extend([str(n/2)])
		n=n/2

print " ".join(out[::-1])
		