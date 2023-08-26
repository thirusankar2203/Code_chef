# cook your dish here
t=int(input(""))
for i in range(t):
    x, y=input("").split()
    sum=int(x)+int(y)
    if(sum>6):
        print("YES")
    else:
        print("NO")