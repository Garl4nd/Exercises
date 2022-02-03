from BinTree import BT

def inorder(bt):
    node=bt.root
    stack=[]
    res=[]
    while node or stack:
        if node:
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            res.append(node.val)
            node=node.right
    return res
def preorder(bt):
    node=bt.root
    stack=[]
    res=[]
    while node or stack:
        if node:
            res.append(node.val)
            stack.append(node)
            node=node.left
        else:
            node=stack.pop()
            node=node.right
    return res

def preorder_traversal(bt): 
    path, result = [bt.root], [] 
    while path: 
        curr = path.pop() 
        if curr: 
            result.append(curr.val) 
            path += [curr.right, curr.left] 
    return result 


bt=BT(50)
bt.multi_append(7,55,60,51)
bt.sprint()
print(inorder(bt))
print(preorder(bt))
print(preorder_traversal(bt))
