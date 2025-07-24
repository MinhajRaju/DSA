def checkSubarraySum( nums, k):


    prefix_sum = 0
    remainder_index = {0: -1}

    for i, num in enumerate(nums):
        prefix_sum += num
        rem = prefix_sum % k
        
        if rem in remainder_index:
            if i - remainder_index[rem] > 1:
                return True
                break               
        else:
            remainder_index[rem] = i
    return False
print(checkSubarraySum(nums = [23, 2, 4, 6, 7], k = 6))