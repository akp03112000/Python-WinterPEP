def reverse_of_digits(n):
    if n==0:
        return 0

    return(n%10 +10*(reverse_of_digits(int(n/10))))
print(reverse_of_digits(123456))