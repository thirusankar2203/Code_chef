# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    if(k>n):
        print("NO")
    elif(n==k):
        if(n==1):
            print("YES")
        else:
            print("NO")
    else:
        sum=0
        for j in range(k+1):
            sum+=j
        if(sum>n):
            print("NO")
        else:
            print("YES")