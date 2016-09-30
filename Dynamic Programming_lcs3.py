# Uses Python2
# Goal is to compute the length of a longest common subsequence of three sequences. Given three sequences A = (a1, a2, . . . , an), B = (b1, b2, . . . , bm), and C = (c1, c2, . . . , cl), find the
# length of their longest common subsequence, i.e., the largest non-negative integer p such that there
# exist indices such that ai1 = bj1 = ck1, . . . , aip = bjp = ckp
# Input: First line: n. Second line: a1, a2, . . . , an. Third line: m. Fourth line: b1, b2, . . . , bm. Fifth
# line: l. Sixth line: c1, c2, . . . , cl
# Constraints. maximum length of sequences 100
# Output: maximum length

n1=input()
f1=raw_input()
a=f1.split()
n2=input()
f2=raw_input()
b=f2.split()
n3=input()
f3=raw_input()
c=f3.split()



common=[[[0 for j in range(0,len(b)+1)] for i in range(0,len(a)+1)] for z in range(0,len(c)+1)]

for z in range(1,len(c)+1):
	for i in range(1,len(a)+1):
		for j in range(1,len(b)+1):
			if (a[i-1]==b[j-1]==c[z-1]):
				common[z][i][j]=max(common[z-1][i-1][j-1]+1,common[z][i][j-1],common[z][i-1][j],common[z-1][i][j])
			else:
				common[z][i][j]=max(common[z-1][i-1][j-1],common[z][i][j-1],common[z][i-1][j],common[z-1][i][j])


print(common[z][i][j])