#Binary tree zig zag

class TreeNode:
    def __init__(self , val):
        self.val = val;
        self.left= None;
        self.right = None

    def __str__(self):
        return f'Node {self.val}'

def BuildTree(values):
   
    if not values or values[0] is  None :
        return None

    root = TreeNode(values[0])
    
    stack = [root]

    i = 1
    while i < len(values):
        
        print([node.val for  node in stack ])
        current = stack.pop(0)
       

        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            stack.append(current.left)

        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            stack.append(current.right)
        i +=1
        
   

    return root
            
        
def zig_zag(root):


    result  = []
    stack = [root]
    left_to_right = True 
    while stack:
        level = []
        size = len(stack)   

        for _  in range(size):        
            
       
            node = stack.pop()  
            level.append(node.val)
            
            if node.right:
                stack.append(node.right)

              
            if node.left:
                stack.append(node.left)

        
  
        if left_to_right:
            left_to_right = False
        else:
            left_to_right = True
            level.reverse()

        result.append(level)
        
    return result
             
        
        



root = BuildTree( [3,9,20,None,None,15,7])
print(zig_zag(root))
# Output: [[3], [20, 9], [15, 7]]
# Explanation: The first level has one node (3), the second level has two nodes (20 and 9), and the third level has two nodes (15 and 7). The zigzag order is achieved by alternating the direction of traversal at each level.# Explanation: The first level has one node (3), the second level has two nodes (20 and 9), and the third level has two nodes (15 and 7). The zigzag