
def twosub(a, k):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[j] - a[i] == k:
                print(a[i], a[j])

twosub(a=[1,2,3,4,5,6,7,8,9], k=3)