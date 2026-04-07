def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort_inplace(array, low, pivot_index - 1)
        quicksort_inplace(array, pivot_index + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


if __name__ == "__main__":
    valores = [64, 34, 25, 12, 22, 11, 90, 3, 47, 58]
    print("Array original:  ", valores)

    resultado = quicksort(valores[:])
    print("Quicksort simple:", resultado)

    array_inplace = valores[:]
    quicksort_inplace(array_inplace, 0, len(array_inplace) - 1)
    print("Quicksort in-place:", array_inplace)
