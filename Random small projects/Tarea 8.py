def sumDigits(numbers):
    if numbers == 0:
        return 0
    else:
        return numbers % 10 + sumDigits(int(numbers / 10))

print(sumDigits(345))
