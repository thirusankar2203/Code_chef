t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    count=0
    if(list1[0]>=list2[0]):
        count+=1
    for j in range(1,n):
        diff1=abs(list1[j]-list1[j-1])
        diff2=list2[j]
        if(diff1>=diff2):
            count+=1
            
    print(count)