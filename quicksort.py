def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(high)
    
    # O(n log n)

print(quicksort([3, 5, 1, 0, 8, 7, 5]))