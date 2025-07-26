

def dailyTemperatures(temperatures):
    n = len(temperatures)   
    answer = [0] * n         
    stack = []           

    for i in range(n):
        
        current_temp = temperatures[i]   
        
        while stack and current_temp > temperatures[stack[-1]]:
            prev_index = stack.pop()  
            answer[prev_index] = i - prev_index              
    
        stack.append(i)
    
    return answer

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))