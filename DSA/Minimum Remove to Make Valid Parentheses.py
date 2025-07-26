def minRemoveToMakeValid(s: str) -> str:
    stack = []
    to_remove = []  # এখন set না, একটা list
    mapping = {')': '('}

    for i, ch in enumerate(s):
        if ch in mapping:  # closing bracket
            if stack and s[stack[-1]] == mapping[ch]:
                stack.pop()
            else:
                to_remove.append(i)  # unmatched closing
        elif ch in mapping.values():  # opening bracket
            stack.append(i)

    # unmatched opening brackets যোগ করি
    to_remove += stack

    # faster lookup এর জন্য set বানাই
    to_remove_set = set(to_remove)

    # valid character গুলা যোগ করি
    result = []
    for i, ch in enumerate(s):
        if i not in to_remove_set:
            result.append(ch)

    return "".join(result)

# ✅ Example usage
s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))  # Output: "lee(t(c)o)de"
