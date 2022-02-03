from BinTree import BT

def LCA(bt,node1,node2):

    def _LCA(node):

        if node==None:
            return 0,"b"
        found_l,where=_LCA(node.left)
        if found_l==2:
            return 2,where
        found_r,where=_LCA(node.right)
        if found_r==2:
            return 2,where
        if found_l==found_r==1 or 1 in [found_l,found_r] and node in [node1,node2]:
            return 2,node
        if node==node1 or node==node2:
            return 1,None
        
        return found_l+found_r,None
    return _LCA(bt.root)[1]

def LCA_parent(bt,node1,node2):
    def get_height(node):
        height=0
        while node!=bt.root:
            height+=1
            node=node.parent
        return height
    height1,height2=get_height(node1),get_height(node2)
    if height1>height2: 
        height2,height1=height1,height2
        node2,node1=node1,node2
    for _ in range(height2-height1):
            node2=node2.parent
    while node1!=node2:
        node1=node1.parent
        node2=node2.parent
    return node1

bt=BT(10,mode="balanced")
bt.multi_append(*range(5,15))
bt.sprint(xstep=20)
l=LCA(bt,bt.get([0,0,0]),bt.get([0,1,1]))
g=LCA_parent(bt,bt.get([0,0,0]),bt.get([0,1,1]))
print(l.val,g.val)