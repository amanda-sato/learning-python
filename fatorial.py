def fatorial(n):
    acc = 1

    for i in range(n):
        acc *= i + 1

    return acc


print(fatorial(10))