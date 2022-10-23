def sort(arr, direction="asc"):
    if direction == 'asc':
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    else:
        for i in range(len(arr)-1, -1, -1):
            key = arr[i]
            j = i + 1
            while j <= len(arr) - 1 and (key < arr[j]):
                arr[j-1] = arr[j]
                j += 1
            arr[j-1] = key


numbers = [3, 4, 5, 6, 2, 3, 1, 98, 4, 324, 13, 2, 3]
sort(numbers, "desc")
print("Sorted array -->", numbers)
