# cook your dish here
list1=list(map(int , input().split()))
count=0
for i in list1:
    if(i>=10):
        count+=1
        
print(count)