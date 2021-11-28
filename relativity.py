for i in range(int(input())):
    g,c = map(int, input().split( ))
    v = c*c
    height = int(v/(2*g))
    print(height)