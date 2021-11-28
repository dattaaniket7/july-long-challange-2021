for i in range(int(input())):
    n,k = map(int, input().split( ))
    arr = list(map(int, input().split( )))
    
    binary = []
    for i in range(0,11):
        binary.append(0)
        for j in range(n):
            if arr[j]%2!=0:
                binary[i]+=1
            arr[j] = arr[j]//2
    
    ans = 0
    for i in range(0,11):
        if binary[i]%k==0:
            ans+= binary[i]//k
        else:
            ans+= binary[i]//k + 1
            
    print(ans)