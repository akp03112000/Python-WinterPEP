def twosum(a, k):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == k:
                print(a[i], a[j])

twosum(a=[1, 2, 3, 4, 5, 6, 7], k=11)


