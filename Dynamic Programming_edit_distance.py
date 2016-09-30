# Uses Python2
# The edit distance between two strings is the minimum number of insertions, deletions, and mismatches in
# an alignment of two strings. The goal of this problem is to implement the algorithm for computing 
# the edit distance between two strings.
# Input: Each of the two lines of the input contains a string consisting of lower case latin letters.
# Constraints: The length of both strings is at least 1 and at most 100.
# Output: The edit distance between the given two strings

first=raw_input()
second=raw_input()


distance=[[0 for j in range(0,len(second)+1)] for i in range(0,len(first)+1)]
distance[0][:]=[x for x in range(0,len(second)+1)]

for i in range(1,len(first)+1):
	distance[i][0]=i
	for j in range(1,len(second)+1):
		if (first[i-1]==second[j-1]):
			distance[i][j]=min(distance[i-1][j-1],distance[i][j-1]+1,distance[i-1][j]+1)
		else:
			distance[i][j]=min(distance[i-1][j-1]+1,distance[i][j-1]+1,distance[i-1][j]+1)

print (distance[i][j])		
			