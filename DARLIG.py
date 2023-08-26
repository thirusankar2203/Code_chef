# cook your dish here
t=int(input())
for i in range(t):
    n,k=map(int, input().split())
    if(n%4==0 and k==0):
        print("Off")
    elif(n%4==0 and k==1):
        print("On")
    elif(n%4!=0 and k==0):
        print("On")
    else:
        print("Ambiguous")
        