def remove_duplicate(nums):
    """
    Removes duplicates from nums in-place and returns the new length.
    
    :param nums: List of integers
    :return: New length of nums after removing duplicates
    """
    if not nums:
        return 0

    pointer = 0
    for i in range(1, len(nums)):
        if nums[pointer] != nums[i]:
            pointer += 1
            nums[pointer] = nums[i]
    
    return pointer + 1  

print(remove_duplicate([0,0,1,1,1,2,2,3,3,4]))  # Output: 2