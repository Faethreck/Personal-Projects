numbers = [21, 4, 1, 3, 9, 20, 25]

for times in range(3):
    for i, number in enumerate(numbers):
        if i >= 6:
            break
        elif number > numbers[i + 1]:
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = number
            

print(numbers)     