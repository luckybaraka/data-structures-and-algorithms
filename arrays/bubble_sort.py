def bubble_Sort(arr: list[int]) -> list[int]:
    length_of_array = len(arr)
    for i in range(length_of_array-1):
        swapped = False
        for j in range(length_of_array-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [7, 3, 9, 12, 11]
print("Sorted array: ", bubble_Sort(arr))



# Bubbble sort time complexity is O(n^2)