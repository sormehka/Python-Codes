#Uses Python2
# Given a set of n segments with integer coordinates on a line, the goal is to find the minimum number m of points such that each segment contains at least one point
# Input: First line contains the number n of segments. Each of the following n lines contains two integers (separated by space) defining the coordinates of the endpoints of each segment
# Output: First line is the minimum number of points, second line contains the integer coordinates of these points (separated by space)


n=int(input())
segments=[]
s=" "

for i in range(0,n):
    S=raw_input()
    segments.extend([S.split()])
    segments[i]=[int(x) for x in segments[i]]

segments.sort(key=lambda x: x[1])

points=[segments[0][1]]

for i in range(0,n):
    if points[len(points)-1]<segments[i][0]:
        points.extend([segments[i][1]])

print len(points)
print s.join(str(x) for x in points)
