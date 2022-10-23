def sort(arr, direction="asc"):
    noMoreSwaps = False
    n = 1
    while not noMoreSwaps:
        noMoreSwaps = True
        for i in range(0, len(arr) - n):
            condition = (arr[i] > arr[i + 1]) if direction == 'asc' else (arr[i] < arr[i + 1])
            if condition:
                temp = arr[i]
                arr[i], arr[i + 1] = arr[i + 1], temp
                noMoreSwaps = False
        n += 1
    return arr


numbers = [3, 4, 5, 6, 2, 3, 1, 98, 4, 324, 13, 2, 3]
sort(numbers)
print("Sorted array -->", numbers)
