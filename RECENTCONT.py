t=int(input())
for i in range(t):
    n=int(input())
    a1=0
    a2=0
    list1=input().split()
    for j in list1:
        if(j=="START38"):
            a1+=1
        elif(j=="LTIME108"):
            a2+=1
        else:
            continue
        
    print(a1,a2)