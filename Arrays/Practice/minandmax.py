def find_min_max(arr):
    if not arr:
        return None, None
    minval = arr[0]
    maxval = arr[0]
    for i in range(len(arr)):
        if arr[i] < minval:
            minval = arr[i]
        if arr[i] > maxval:
            maxval = arr[i]
    return minval, maxval
