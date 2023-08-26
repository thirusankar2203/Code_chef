# cook your dish here
a,b,x,y=map(int, input().split())
messi=(a*2)+(b*1)
ronaldo=(x*2)+(y*1)
if(messi>ronaldo):
    print("Messi")
elif(ronaldo>messi):
    print("Ronaldo")
else:
    print("Equal")