TEST_DATA = [1,2,[3,4],[5,6]]
sum = [0]
counter = 0
def summer(number, counter):
    
    if counter >= 3:
        return summer(TEST_DATA[counter[counter - 2]], counter)
    else:
        counter += 1
        return summer(TEST_DATA[counter], counter)


