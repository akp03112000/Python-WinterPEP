def f(n):
    a=[["-"]*n for _ in range (n)]
    for i in range(n):
        if i%2==0 and j%2==0:
            a[i][j]="*"

    return a
    for i in f(5):
     print(i)