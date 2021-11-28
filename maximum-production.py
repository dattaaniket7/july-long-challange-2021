t=int(input())
for _ in range(t):
    d,x,y,z = map(int, input().split())
    a= x*7
    b= (y*d + (7-d)*z)
    print(max(a,b))