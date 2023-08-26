# cook your dish here
t=int(input(""))
for i in range(t):
    n=int(input(""))
    number=input("")
    flag=1
    for j in number:
        if(j=='0' or j=='5'):
            flag=0
            break
    if(flag==0):
        print("Yes")
    else:
        print("No")