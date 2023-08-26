# cook your dish here
import math
t=int(input())
for i in range(t):
    x,y,r=map(int, input().split())
    extra_ate=r//30
    total_ate=extra_ate+x
    plates=total_ate/y
    print(math.ceil(plates))