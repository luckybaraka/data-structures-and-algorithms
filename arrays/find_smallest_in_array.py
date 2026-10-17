def smallest(arr: list[int])-> int:
    smallest_elem = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_elem:
            smallest_elem = arr[i]
    return smallest_elem


arr = [4, 2, 3, 6, 7, 6, 2]
print(smallest(arr))


print(min(arr))
print(max(arr))