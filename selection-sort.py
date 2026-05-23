def smallestElem(arr) -> int:
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestelem = smallestElem(arr)
        newArr.append(arr.pop(smallestelem))
    return newArr

print(selectionSort([3, 4, 2, 1, 5, 7, 8, 4, 0, 2]))

# O(n^2)