# cook your dish here
t=int(input())
for i in range(t):
    l,r=map(int, input().split())
    c=0
    for j in range(l,r+1):
        rem=j%10
        if(rem==2 or rem==3 or rem==9):
            c=c+1
            
    print(c)