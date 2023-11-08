"""
Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:
If the number has an integer square root, take this, otherwise square the number.
"""
import math
def square_or_square_root(arr):
    for x in range(0, len(arr)):
        num = math.isqrt(arr[x])
        
        if(num * num == arr[x]):
            arr[x] = num
        else:
            arr[x] = math.pow(arr[x],2)
    return arr