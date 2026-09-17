square=lambda n:n*n
print(square(10))


def factorial(n):
    if n ==0:
        return 1
    else:
     return n*factorial(n-1)

    