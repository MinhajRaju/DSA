def remove_element(nums, val):
    """
    Removes all instances of val from nums in-place and returns the new length.
    
    :param nums: List of integers
    :param val: Integer value to remove
    :return: New length of nums after removal
    """
    p =  0
    for i in range(len(nums)):
        if nums[i] != val:                
            nums[p] = nums[i]
            p += 1
    return p
            
print(remove_element([3, 2, 2, 3], 3))  # Output: 2