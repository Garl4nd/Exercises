class Node:
    def __init__(self,val=None,left=None,right=None,parent=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent
    def append(self,node,lr=0):
        if lr==0:
            self.left=node
        else:
            self.right=node
        node.parent=self

class BT:


    def __init__(self,val=None,mode="sorted"):
        self.root=Node(val=val)
        self._mode=mode
        self.num=1
        self.lowest=1
        self.height=0
    
    def append(self,val):

        if self._mode=="balanced":
            #print(self.num,self.lowest)
            if self.num==2*self.lowest-1:
                self.lowest=1
                self.height+=1
            else:
                self.lowest+=1
            
            #print(self.lowest)
            path=[int(b) for b in str(bin(self.lowest-1))[2:]]
            path=[0]*(self.height-len(path))+path
            #print(f"{path=}",self.lowest)
            self.append_at(path,val)
            self.num+=1
        
        if self._mode=="sorted":
            cur_node=self.root
            parent=None
            ind=0
            while cur_node is not None:
                ind+=1
                parent=cur_node
                if val<cur_node.val:
                    cur_node=cur_node.left
                    lr=0
                else:
                    cur_node=cur_node.right
                    lr=1
            cur_node=Node(val=val,parent=parent)
            parent.append(cur_node,lr=lr)
            self.num+=1
            if ind==self.height:
                self.lowest+=1
            elif ind==self.height+1:
                self.height=ind
                self.lowest=1
    def multi_append(self,*vals):
        for val in vals:
            self.append(val)
    def traverse(self,order="inorder"):
        def _traverse(order,root):
            if root is None:
                return
            if order=="inorder":
                yield from _traverse(order,root.left)
                yield root.val
                yield from _traverse(order,root.right)
            elif order=="preorder":
                yield root.val
                yield from _traverse(order,root.left)
                yield from _traverse(order,root.right)
            elif order=="postorder":
                yield from _traverse(order,root.left)
                yield from _traverse(order,root.right)
                yield root.val

        yield from _traverse(order=order,root=self.root)

    def enh_traverse(self,order="inorder"):
        def _traverse(order,root,x,y):
            if root is None:
                return
            if order=="inorder":
                yield from _traverse(order,root.left,x-1,y+1)
                yield root.val,x,y
                yield from _traverse(order,root.right,x+1,y+1)
            elif order=="preorder":
                yield root.val,x,y
                yield from _traverse(order,root.left,x-1,y+1)
                yield from _traverse(order,root.right,x+1,y+1)
            elif order=="postorder":
                yield from _traverse(order,root.left,x-1,y+1)
                yield from _traverse(order,root.right,x+1,y+1)
                yield root.val,x,y

        yield from _traverse(order=order,root=self.root)
        
    def __iter__(self):
        yield from self.traverse()
    def append_at(self,path,val):
        node=self.get(path[:-1])
        new_child=Node(val=val)
        #print("appending to parrent with val:",node.val)
        node.append(new_child,lr=path[-1])
    
    def get(self,path=[],cur_node=None):
        if cur_node is None:
            cur_node=self.root
        #print(cur_node)
        if not path:
            return cur_node
        else:
            next=cur_node.left if path[0]==0 else cur_node.right
            return self.get(path=path[1:],cur_node=next)

    