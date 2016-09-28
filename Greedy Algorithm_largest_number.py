# Uses Python2
# The goal is to compose the largest number out of a set of integers
# Input: The first line contains an integer 0<n<=100, the second line contains n integers (between 1 and 1000)
# Output: The largest number that can be composed of the n integers


n=input()
S=raw_input()
ss=S.split(' ')

all=[]
s=''
salary=''
sorted=[]

for i in range(0,len(ss)):
    all.extend([int(ss[i])])

while len(all)>0:
    max=all[0]
    for i in range(1,len(all)):
        number1=str(max)+str(all[i])
        number2=str(all[i])+str(max)
        if int(number2)>int(number1):
            max=all[i]
    sorted.extend([max])
    all.remove(max)

for i in range(0,len(ss)):
    salary += str(sorted[i])
print salary


