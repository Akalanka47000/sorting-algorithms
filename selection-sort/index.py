def sort(arr, direction="asc"):
    for i in range(len(arr)) if direction == 'asc' else range(len(arr) - 1, -1, -1):
        minIndex = i
        for j in range(i + 1, len(arr)) if direction == 'asc' else range(i - 1, -1, -1):
            if arr[minIndex] > arr[j]:
                minIndex = j
        temp = arr[i]
        arr[i], arr[minIndex] = arr[minIndex], temp


numbers = [3, 4, 5, 6, 2, 3, 1, 98, 4, 324, 13, 2, 3]
sort(numbers)
print("Sorted array -->", numbers)
