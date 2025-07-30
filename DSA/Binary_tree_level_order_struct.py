class TreeNode:
    def __init__(self ,val):
        self.val = val;
        self.left = None;
        self.right = None;

    def __str__(self):
        return f"Node {self.val}"

def build_tree(arr):
    if not arr or  arr[0] is None:
        return None

    root = TreeNode(arr[0])
    stack = [root]
    i = 1

    while i <= len(arr):
       
        current = stack.pop(0)
        
        if i< len(arr) and arr[i] is not  None:
            
            current.left = TreeNode(arr[i])
            stack.append(current.left)
        i +=1
      
        if i< len(arr) and arr[i] is  not None:
       
            current.right = TreeNode(arr[i])
            stack.append(current.right)
        i += 1
       
   
    return root


def preoder(root):
    if not root:
        return []
    
    result = [root.val]
    result += preoder(root.left)
    result += preoder(root.right)
    
    return result


root = build_tree([3,9,20,None,None,15,7])
print(preoder(root))
