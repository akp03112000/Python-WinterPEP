def sum_subarray(a):
    s=0
    for i in range(len(a)):
        if(type(a[i])==int):
            s += a[i]
        else:
            for j in a[i]:
                s+=j
    print(s)
sum_subarray([1,2,3,[4,5,6],[4]])