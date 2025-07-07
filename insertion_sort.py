def insertion_sort_desc(arr):
    """
    Sorts the array in-place in descending order using the Insertion Sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [10, 3, 7, 4, 8, 2]
    print("Original array:", arr)
    sorted_arr = insertion_sort_desc(arr)
    print("Sorted array (descending):", sorted_arr)
