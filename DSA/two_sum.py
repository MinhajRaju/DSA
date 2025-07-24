def two_sum(nums , target):
    #Pattern : - Hashmap
    #Using a dictionary to store the indices of the numbers
    #This allows us to find the complement in O(1) time
    
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i   
                

print(two_sum([2,7,11,15]  ,  9 ))