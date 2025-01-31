def fun(arr,n):
    if (n==10):
     return arr[0]
return min(arr[n-1],fun(arr,n-1))
print(fun(arr=[1,2,3,4,5],n=5))