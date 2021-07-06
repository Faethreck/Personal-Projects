numbers = [21, 4, 1, 3, 9, 20, 25]

# array creator

length = len(numbers)
counter = 0
array_counter = 0
for i in numbers[1:length]:
    counter += 1
    
    if counter == 2:
        array_counter += 1
        break
