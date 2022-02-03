class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        self.parent=None

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
    
    def __bool__(self):
        return self.num>0
    
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
            cur_node=Node(val=val)
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
    
    def traverse(self,order="inorder",rev=False):

        def _traverse(order,root):
            if root is None:
                return
            left=root.left if not rev else root.right
            right=root.right if not rev else root.left
            if order=="inorder":
                yield from _traverse(order,left)
                yield root.val
                yield from _traverse(order,right)
            elif order=="preorder":
                yield root.val
                yield from _traverse(order,left)
                yield from _traverse(order,right)
            elif order=="postorder":
                yield from _traverse(order,left)
                yield from _traverse(order,right)
                yield root.val

        yield from _traverse(order=order,root=self.root)
        
    def enh_traverse(self,order="inorder",x0=50,xstep=5,ystep=1):
        def _traverse(order,root,x,y,xstep):
            if root is None:
                return
            if order=="inorder":
                yield from _traverse(order,root.left,x-xstep,y+ystep,xstep//2)
                yield root.val,x,y
                yield from _traverse(order,root.right,x+xstep,y+ystep,xstep//2)
            elif order=="preorder":
                yield root.val,x,y
                yield from _traverse(order,root.left,x-xstep,y+ystep,xstep//2)
                yield from _traverse(order,root.right,x+xstep,y+ystep,xstep//2)
            elif order=="postorder":
                yield from _traverse(order,root.left,x-xstep,y+ystep,xstep//2)
                yield from _traverse(order,root.right,x+xstep,y+ystep,xstep//2)
                yield root.val,x,y

        yield from _traverse(order=order,root=self.root,x=x0,y=0,xstep=xstep)
        
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
    
    def print_all(self,order="inorder"):
        print(", ".join(str(val) for val in self.traverse(order=order)))
        

    def sprint(self,x0=50,xstep=10,ystep=1):
        vals_pos=sorted(self.enh_traverse(order="inorder",x0=x0,xstep=xstep,ystep=ystep),key=lambda x:x[2])
        #print(vals_pos)
        lasty=0
        print_queue=[]
        for val,x,y in vals_pos:
            
            if lasty==y:
                print_queue.append([val,x])
            else:
                x0=0
                for pval,px in print_queue:
                    print(" "*(px-x0)+str(pval),end="")
                    x0=px
                print_queue=[[val,x]]            
                for _ in range(y-lasty):
                    print("\n")
            #print(print_queue,val,lasty,y)
            lasty=y
        
        x0=0
        
        for val,x in print_queue:
            print(" "*(x-x0-1)+str(val),end="")
            x0=x
        print()