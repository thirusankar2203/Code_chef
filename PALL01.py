# cook your dish here
t=int(input(""))
for i in range(t):
    number=input("")
    number1=number[::-1]
    if(number==number1):
        print("wins")
    else:
        print("loses")