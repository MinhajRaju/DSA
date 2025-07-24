def pivotIndex( nums):
    if not nums:
        return -1
    total = sum(nums[:len(nums)])
    left_sum = 0

    for i in range(len(nums)):
        right = total - left_sum - nums[i]
        print(right , total , left_sum)
        if right == left_sum: 
            print("Found pivot at index:", i)           
            return i
        left_sum += nums[i]
    return -1
pivotIndex([1, 7, 3, 6, 5, 6])   