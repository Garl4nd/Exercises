from BinTree import BT,Node
def reconstruct(inorder,preorder):
    bt=BT(None)
    
    def _reconstruct(inorder,preorder):
        if inorder:
            #print(inorder,preorder)
            root_val=preorder[0]
            root_ind=inorder.index(root_val)
            node=Node(val=root_val)

            l_insubtree,r_insubtree=inorder[:root_ind],inorder[root_ind+1:]
            l_presubtree,r_presubtree=preorder[1:root_ind+1],preorder[root_ind+1:]
            if (l_node:=_reconstruct(l_insubtree,l_presubtree)):
                node.append(l_node,lr=0)
            if (r_node:=_reconstruct(r_insubtree,r_presubtree)):
                node.append(r_node,lr=1)
            return node
    bt.root=_reconstruct(inorder,preorder)
    return bt

def reconstruct_wnulls(preorder):
    bt=BT(None)
    
    def _reconstruct(preorder):
        root_val=preorder[0]
        node=Node(root_val)
        if root_val is None:
            return None,1
        left_node,ind1=_reconstruct(preorder[1:])
        right_node,ind2=_reconstruct(preorder[1+ind1:])
        if left_node is not None:
            node.append(left_node,lr=0)
        if right_node is not None:
            node.append(right_node,lr=1)
        return node,ind1+ind2+1

    bt.root=_reconstruct(preorder)[0]
    return bt
"""
origbt=BT(15)
origbt.multi_append(7,9,16,24,48,0,6,5,1)
origbt.sprint(xstep=20)
inorder=list(origbt.traverse("inorder"))
preorder=list(origbt.traverse("preorder"))
bt=reconstruct(inorder,preorder)
bt.sprint(xstep=20)
"""
bt=reconstruct_wnulls(("H", "B", "F", None, None, "E", "A", None, None, None, "C", None, "D", None, "G", "I", None, None, None))
bt.print_all("preorder")
bt.sprint(xstep=15)
