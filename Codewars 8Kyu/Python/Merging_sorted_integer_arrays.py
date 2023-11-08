"""
Write a function that merges two sorted arrays into 
a single one. The arrays only contain integers. Also, the
 final outcome must be sorted and not have any duplicate.
"""
def merge_arrays(first, second): 
    arr = []
    for x in first:
        if x not in arr:
            arr.append(x)
    for y in second:
        if y not in arr:
            arr.append(y)
    return sorted(arr)