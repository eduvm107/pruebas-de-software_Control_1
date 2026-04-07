def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + middle + quicksort(right)



if __name__ == "__main__":
    valores = [64, 34, 25, 12, 22, 11, 90, 3, 47, 58]
    print("Array original:  ", valores)

    resultado = quicksort(valores[:])
    print("Quicksort simple:", resultado)

    array_inplace = valores[:]
    quicksort_inplace(array_inplace, 0, len(array_inplace) - 1)
    print("Quicksort in-place:", array_inplace)
