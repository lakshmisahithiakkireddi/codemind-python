def count_odd_subarrays(L, R):
    result = 0
    
    # Loop through all possible subarrays in the given range
    for i in range(L, R+1):
        for j in range(i, R+1):
            subarray_sum = sum(range(i, j+1))
            if subarray_sum % 2 != 0:
                result += 1
    
    return result

# Input
L = int(input())
R = int(input())

# Output
result = count_odd_subarrays(L, R)
print(result)
