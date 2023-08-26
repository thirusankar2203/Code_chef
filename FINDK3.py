# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int, input().split())
    if((y*z)%x==0):
        print((y*z),x)
    elif((x*z)%y==0):
        print((x*z),y)
    elif((x*y)%z==0):
        print((x*y),z)
    else:
        print("-1")