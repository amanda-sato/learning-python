numbers = [0, 0, 0]
numbers[0] = float(input("1º número: "))
numbers[1] = float(input("2º número: "))
numbers[2] = float(input("3º número: "))

sortedlist = sorted(numbers)

print(f"menor: {sortedlist[0]}, maior: {sortedlist[2]}")

numbers = [0, 0, 0]
numbers[0] = float(input("1º número: "))
numbers[1] = float(input("2º número: "))
numbers[2] = float(input("3º número: "))

acc_min = numbers[0]
acc_max = numbers[0]

for n in numbers:
    if n < acc_min:
        acc_min = n

    if n > acc_max:
        acc_max = n

print(f"Maior: {acc_max}\nMenor: {acc_min}")

numbers = [0, 0, 0]
numbers[0] = float(input("1º número: "))
numbers[1] = float(input("2º número: "))
numbers[2] = float(input("3º número: "))

min = numbers[0]
max = numbers[0]

for n in numbers:
    if n < min:
        min = n

    if n > max:
        max = n

print(f"Maior: {max}\nMenor: {min}")

numbers = [0, 0, 0]
numbers[0] = float(input("1º número: "))
numbers[1] = float(input("2º número: "))
numbers[2] = float(input("3º número: "))

print(f"Maior: {max(numbers)}\nMenor: {min(numbers)}")