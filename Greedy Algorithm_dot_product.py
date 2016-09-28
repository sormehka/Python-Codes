# Uses Python2
# There are n ads to be placed on a popular Internet page. For each ad, you know how much is the advertiser willing to pay for one click on this ad. You have set up n slots on your page and estimated the expected number of clicks per day for each slot. Now, the  goal is to distribute the ads among the slots to maximize the total revenue.
# Input: the first line is an integer n, second line is a sequence of n integers (the profit per click of each ad) and the third line is a sequence of n integers (the average number of clicks per day of each slot)
# Output: maximum revenue

n=int(input())
Sc=raw_input()
Sb=raw_input()
c=Sc.split()
b=Sb.split()

mult=0

if len(c)<>n or len(b)<>n:
    print('wrong input')
else:
    for i in range(0,n):
        c[i]=int(c[i])
        b[i]=int(b[i])
    c.sort()
    b.sort()
    for i in range(0,n):
        mult += c[i]*b[i]
print mult
