from collections import deque
from linked_list import LL

def highlight(text,keywords): # nevyhoda: musi se pocitat minima, takze se plně nevyužije pořadí prvků - fronta, která ho ukládá, se jen využívá na kontrolu, zda se vyplatí vůbec porovnávat nový blok se starým. Ideálně bych chtěl duplicitní prvky mazat a nahrazovat novými. Viz highlight2
    posdict={}
    wnum=len(keywords)
    textwords=text.split()
    maxlen=len(textwords)
    entry_queue=deque()
    
    l,u=0,0
    comp=True 
    for ind,word in enumerate(textwords):
        
        if word in keywords:
            
            if entry_queue:
                
                while entry_queue and word==entry_queue[-1]:
                    entry_queue.pop()
                    
                if entry_queue and word==entry_queue[0]:
                    entry_queue.popleft()
                    comp=True
            entry_queue.append(word)
            if entry_queue:
                print(ind,entry_queue)
            posdict[word]=ind
            if len(posdict)==wnum:
                mx,mn=ind,min(posdict.values())


                if comp and (dif:=ind-mn)<maxlen:
                    comp=False
                    maxlen=dif
                    l,u=mn,mx
            
    return l,u

def highlight2(text,keywords): # Lepší než highlight, ale musí se používat hledání ve frontě. Vhondější je řešení přes linked list, kde se přímo trackuje node pro každé slovo, viz highlight3.
    posdict={}
    
    wnum=len(keywords)
    textwords=text.split()
    maxlen=len(textwords)
    entry_queue=deque()
    
    l,u=0,0
    comp=True 
    for ind,word in enumerate(textwords):
        
        if word in keywords:
            
            if entry_queue:
                if word in entry_queue:                
                    if word==entry_queue[0]:
                        comp=True
                    entry_queue.remove(word)
            entry_queue.append(word)
                
            posdict[word]=ind
            if len(posdict)==wnum:
                mx,mn=ind,posdict[entry_queue[0]]


                if comp and (dif:=ind-mn)<maxlen:
                    comp=False
                    maxlen=dif
                    l,u=mn,mx
            
    return l,u

def highlight3(text,keywords):
    posdict={}
    nodedict={}
    wnum=len(keywords)
    textwords=text.split()
    maxlen=len(textwords)
    ll=LL()    
    l,u=0,0
    comp=True 
    filled=False
    for ind,word in enumerate(textwords):
        
        if word in keywords:
            print(f"{word=}")
            if word in nodedict:
                if word==ll[0].val:
                    comp=True
                ll.delete_node(nodedict[word])
            
            nodedict[word]=ll.insert(word)
            ll.print_all()
            posdict[word]=ind
            if filled or len(posdict)==wnum:
                filled=True
                mx,mn=ind,posdict[ll[0].val]


                if comp and (dif:=ind-mn)<maxlen:
                    comp=False
                    maxlen=dif
                    l,u=mn,mx
            
    return l,u


print(highlight2("a b c e e  d b c d e e  a c b g e d c e e e e a b  ",["a","b","c","d"]))