#Uses Python2
# The goal is to find the mimimum number of coins needed to change the input value into coins with denominations 1, 5 and 10 using greedy algorithm
# The input is a single integer
# The output is the minimum number of coins with denominations 1, 5 and 10


n=int(input())
tens=n/10
n=n%10
fives=n/5
n=n%5
ones=n
total=tens+fives+ones

print total


