class LL:
    
    class Node:
        def __init__(self,val,next,prev):
            self.val=val
            self.next=next
            self.prev=prev
    
    class Boundary:
        def __init__(self,val,next,prev):
            self.val=val
            self.next=next
            self.prev=prev

    def __init__(self):
        self.beg=LL.Boundary(None,None,None)
        self.end=LL.Boundary(None,None,None)
        self.beg.next=self.end
        self.end.prev=self.beg
        self.cur=self.beg
        self.len=0
    
    def __iter__(self):
        cur=self.beg.next
        while cur!=self.end:
            yield cur
            cur=cur.next
    
    def get(self,at_ind,start=None,reverse=False):
        if start is None:
            start=self.cur
        at=start
        i=0
        if reverse:
            end=self.beg
            at_ind=-at_ind-1
        else:
            end=self.end

        while i<at_ind:
            i+=1
            if reverse:
                at=at.prev
            else:
                at=at.next

            if at==end:
                raise ValueError("The input index exceeds the length of the list!")
        return at

    def __getitem__(self,ind):
        if ind>=0:
            return self.get(ind,start=self.beg.next)
        else:
            return self.get(ind,start=self.end.prev,reverse=True)
        
    def reverse(self,fr=0,to=None):
        if to is None:
            to=self.len
        
        fr_node=node=self.get(fr,start=self.beg)
        to_node=self.get(to-fr,start=fr_node).next
        i=fr
        node=first_node=node.next
        while i<to:
            next=node.next
            node.next=node.prev
            node.prev=next
            node=next
            i+=1
        last_node=node.prev
        fr_node.next=last_node
        last_node.prev=fr_node
        to_node.prev=first_node
        first_node.next=to_node
        
        
        

    def insert(self,val,at_ind=None):
        at=self.beg
        if at_ind==None:
            at=self.end.prev
        else:
            at=self.get(at_ind,self.beg)
            
            
        orig_next=at.next
        at.next=self.Node(val,orig_next,at)
        orig_next.prev=at.next
        if at.next.next==self.end:
            self.end.prev=at.next 
        self.cur=at.next
        self.len+=1
        
        return at.next


    def delete(self,at_ind=None):

        if at_ind is None:
            at=self.cur
        else:
            at=self.get(at_ind,self.beg)
        try:
            at.prev.next=at.next
        except AttributeError:
            raise ValueError("Can't delete an element from an empty list")
        at.next.prev=self.cur.prev
        if at_ind is None:
            self.cur=at.prev
        self.len-=1

    def delete_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        self.len-=1

    def cyclic_shift(self,k=1):
        if k%self.len==0:
            return
        new_head=self.get(self.len-k%self.len,self.beg.next)
        old_head=self.beg.next
        old_tail=self.end.prev
        pre_new_head=new_head.prev

        pre_new_head.next=self.end
        self.end.prev=pre_new_head

        old_tail.next=old_head
        old_head.prev=old_tail
        
        self.beg.next=new_head
        new_head.prev=self.beg
        
        

    def clear_list(self):
        self.beg.next=self.end
        self.end.prev=self.beg
        self.cur=self.beg
        self.len=0

    def multi_insert(self,*vals):
        for val in vals:
            self.insert(val) 

    def print_all(self,rev=False):
        fs=[]
        if not rev:
            node=self.beg
            node=node.next
            while node!=self.end:
                
                fs+=[node.val]
                node=node.next
        else:
            node=self.end
            node=node.prev
            while node!=self.beg:
                fs+=[node.val]
                node=node.prev
        print(", ".join(str(val) for val in fs))

    def sorted(self,rev=False):
        ll=LL()
        ll.multi_insert(*sorted(node.val for node in iter(self)))
        return ll



def merge_sorted_lists(l1,l2):
    ll=LL()
    it1=iter(l1)
    it2=iter(l2)
    node1=next(it1)
    node2=next(it2)
    fin1,fin2=False,False
    while not (fin1 and fin2):
        
        if not fin1 and (node1.val<node2.val or fin2):
            ll.insert(node1.val)
            try:
                node1=next(it1)
            except StopIteration:
                fin1=True

        if not fin2 and (node2.val<node1.val or fin1):
            ll.insert(node2.val)
            try:
                node2=next(it2)
            except StopIteration:
                fin2=True
                 
        
            
    return ll

