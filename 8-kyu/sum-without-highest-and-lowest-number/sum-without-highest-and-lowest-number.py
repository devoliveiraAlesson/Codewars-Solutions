def sum_array(arr):
    if arr and len(arr) > 1:
        return sum(arr) - min(arr) - max(arr)
    else: return 0