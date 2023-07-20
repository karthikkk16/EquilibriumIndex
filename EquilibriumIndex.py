def EquilibriumIndex(array):
    n=len(array)
    prefix=[0]*n
    prefix[0]=array[0]

    for i in range(1,n):
        prefix[i]=prefix[i-1]+array[i]

    for i in range(1,n):
        if prefix[i-1]==prefix[n-1]-prefix[i]:
            return i
    return -1

array=list(map(int,input().split()))
print(EquilibriumIndex(array))