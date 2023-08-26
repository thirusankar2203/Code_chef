# cook your dish here

t=int(input())
for j in range(t):
    out=''
    hidden=input("")
    guess=input("")
    n=len(hidden)
    for i in range(n):
        x=hidden[i]
        y=guess[i]
        if(x==y):
            out+='G'
        else:
            out+='B'
            
    print(out)