def  longest_common_prefix(strs):
    
    #Pattern: - Horizontal Scanning
    #This approach compares each string with the current prefix
    
    if not strs:
        return ""
    
    # Start with the first string as the prefix
    prefix = strs[0]
    
    for s in strs[1:]:
        # Compare the current string with the prefix
        while s[:len(prefix)] != prefix and prefix:
            # Shorten the prefix until it matches
            prefix = prefix[:-1]
    
    return prefix

print(longest_common_prefix([ 
"flower", "flow", "flight"
])  )