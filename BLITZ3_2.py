# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int, input().split())
    total_time=2*(180+n)
    time_left=a+b
    duration=total_time-time_left
    print(duration)