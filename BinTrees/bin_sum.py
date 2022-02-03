from BinTree import BT

def all_paths(bt,order="inorder",rev=False):
    paths=[]
    def _traverse(order,root,path):
            
            left=root.left if not rev else root.right
            right=root.right if not rev else root.left
            if order=="inorder":
                if left is not None:
                    _traverse(order,left,path=path+[0])
                if right is not None:
                    _traverse(order,right,path=path+[1])
                if left is None and right is None:
                    paths.append(path)
            elif order=="preorder":
                _traverse(order,left,path=path+[0])
                _traverse(order,right,path+[1])
            elif order=="postorder":
                _traverse(order,left,path=path+[0])
                _traverse(order,right,path=path+[1])
                

    _traverse(order=order,root=bt.root,path=[])
    return paths

def sum_paths(bt,order="inorder",rev=False):
    global ts
    ts=0
    def _traverse(order,root,s):
            global ts
            left=root.left if not rev else root.right
            right=root.right if not rev else root.left
            
            if left is not None:
                _traverse(order,left,s=2*s)
            if right is not None:
                _traverse(order,right,s=2*s+1)
            if left is None and right is None:
                ts+=s
                

    _traverse(order=order,root=bt.root,s=0)
    return ts

def check_weight(bt,weight):
    def _check(node,rem=weight):
        if node is None:
            return False,None
        rem=rem-node.val
        if rem==0:
            return True, node
        else:
            
            
            lfound,where=_check(node.left,rem=rem)
            if lfound:
                return True, where
            rfound,where=_check(node.right,rem=rem)
            if rfound:
                return True,where
            return False,None

    return _check(bt.root)

bt=BT(10,mode="sorted")
bt.multi_append(5,4,3,9,20,30)
bt.sprint()
print(all_paths(bt))
print(sum_paths(bt))
print(check_weight(bt,22))
