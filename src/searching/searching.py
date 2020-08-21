# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    midpoint = (end - start)//2
    try: arr[midpoint]
    except: return -1 #Array is empty

    if arr[midpoint] == target:
        return midpoint
    elif start == end:
        return -1 # not found
    elif target < arr[midpoint]:
        return binary_search(arr,target,start,midpoint)
    elif target > arr[midpoint]:
        return binary_search(arr,target,midpoint,end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    pass
