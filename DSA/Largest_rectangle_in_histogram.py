def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # sentinel

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

print(largestRectangleArea( [2, 1, 5, 6, 2, 3]))  # Output: 10   