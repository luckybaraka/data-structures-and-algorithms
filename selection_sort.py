def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)
    return arr



arr = [3, 7, 8, 1, 4, 2, 9, 0, 7]
res = selection_sort(arr)
print(res)

