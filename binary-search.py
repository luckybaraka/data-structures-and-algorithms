def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        guess = arr[mid]

        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid - 1
        else:
            return mid
    return None


print(binary_search([1, 2, 3, 4, 5, 6], 5))

# O(log n)