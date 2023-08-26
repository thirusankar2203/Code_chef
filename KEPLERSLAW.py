t=int(input())
for i in range(t):
    t1,t2,r1,r2=map(int, input().split())
    cons1=(t1**2)/(r1**3)
    cons2=(t2**2)/(r2**3)
    if(cons1==cons2):
        print("Yes")
    else:
        print("No")