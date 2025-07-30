# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
root = build_tree([3,9,20,None,None,15,7])


def levelOrder( root):

    if not root:
        return []

    result = []
    queue = [root]


    while queue:
        level = []
        size = len(queue)
       

        for _ in range(size):
            node = queue.pop(0)
          
            level.append(node.val)


            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



        result.append(level)
    return result #For bottom to top [::-1] or using reverse fucniton or insert funciton
print(levelOrder(root))