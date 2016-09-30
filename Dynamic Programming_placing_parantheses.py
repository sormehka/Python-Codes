# Uses Python2
# Goal is to add parentheses to a given arithmetic expression to maximize its value.
# Input: The only line of the input contains a string s of length 2n + 1 for some n, with symbols
# s0, s1, . . . , s2n. Each symbol at an even position of s is a digit (that is, an integer from 0 to 9) while
# each symbol at an odd position is one of three operations from +,- or *.
# Constraints. n equal or less than 14 (hence the string contains at most 29 symbols).
# Output: the maximum possible value of the given arithmetic expression among different orders of applying 
# arithmetic operations.

n=raw_input()
numb=[int(n[x]) for x in range(0,len(n),2)]
op=[str(n[x]) for x in range(1,len(n),2)]

maxval=[[0 for j in range(0,len(numb))] for i in range(0,len(numb))]
minval=[[0 for j in range(0,len(numb))] for i in range(0,len(numb))]

def minmax(i,j,maxval,minval):
	minij=10e10
	maxij=-10e10
	for k in range(i,i+j):
		a=eval(str(maxval[i][k])+op[k]+str(maxval[k+1][i+j]))
		b=eval(str(maxval[i][k])+op[k]+str(minval[k+1][i+j]))
		c=eval(str(minval[i][k])+op[k]+str(maxval[k+1][i+j]))
		d=eval(str(minval[i][k])+op[k]+str(minval[k+1][i+j]))
		valmax=max(a,b,c,d)
		valmin=min(a,b,c,d)
		if (valmax>maxij):
			maxij=valmax
		if (valmin<minij):
			minij=valmin
	return([maxij,minij])
i=0
j=1

for i in range(0,len(numb)):
	maxval[i][i]=numb[i]
	minval[i][i]=numb[i]

while j<(len(numb)):
	for i in range(0,len(numb)):
		if (i+j)<len(numb):
			val=minmax(i,j,maxval,minval)
			maxval[i][i+j]=val[0]
			minval[i][i+j]=val[1]
	j += 1
		
print(maxval[0][len(numb)-1])		