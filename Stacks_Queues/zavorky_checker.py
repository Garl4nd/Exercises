def check_zavorky(expression):
    ps=[]
    bs=[]
    cs=[]
    stack=[]
    match_dict={"(":")","{":"}","[":"]"}
    rbracks=list(match_dict.values())
    for s in expression:
        if s in match_dict:
            #stack_dict[s].append(1)
            stack.append(s)
        elif s in rbracks:
            try:
                q=stack.pop()
                if s!=match_dict[q]:
                    return False
            except IndexError:
                return False
        else:
            continue
    if stack:
        return False
    else:
        return True

print(check_zavorky("{(456)}"))