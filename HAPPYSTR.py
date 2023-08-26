# cook your dish here
t=int(input(""))
for i in range(t):
    vowels=['a','e','i','o','u']
    flag=1
    string=input("")
    n=len(string)
    for j in range(n):
        if(j+2==n-1):
            break
        ch=string[j]
        if ch in vowels:
            ch1=string[j+1]
            if ch1 in vowels:
                ch2=string[j+2]
                if ch2 in vowels:
                    print("Happy")
                    flag=0
                    break
    if(flag==1):
        print("Sad")
        