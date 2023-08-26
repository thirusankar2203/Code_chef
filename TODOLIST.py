t=int(input(""))
for i in range(t):
    n=int(input())
    list1=list(map(int, input().split()))
    count=0
    for j in list1:
        if(j>=1000):
            count+=1
    print(count)