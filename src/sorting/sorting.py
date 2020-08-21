# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    idxA = 0
    idxB = 0
    i = 0
    while i < len(merged_arr):
        if idxA == len(arrA):
            merged_arr[i:] = arrB[idxB:]
            break
        elif idxB == len(arrB):
            merged_arr[i:] = arrA[idxA:]
            break
        elif arrA[idxA] > arrB[idxB]:
            merged_arr[i] = arrB[idxB]
            idxB += 1
            i += 1
        elif arrA[idxA] <= arrB[idxB]:
            merged_arr[i] = arrA[idxA]
            idxA += 1
            i += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) > 1:
        halfSize = len(arr) // 2
        arr = merge(merge_sort(arr[:halfSize]), merge_sort(arr[halfSize:]))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

