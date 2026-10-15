def add_arrays(n, a, b):
    result = []

    for i in range(n):
        result.append(a[i] + b[i])

    return result

a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

print(add_arrays(len(a), a, b))