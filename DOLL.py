# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    list1=list(map(int, input().split()))
    c=0
    for j in list1:
        if(j>k):
            c+=1
    print(c)