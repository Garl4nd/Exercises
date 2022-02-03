import itertools as it
def grouper(iterable,num):
    return zip(*([iter(iterable)]*num))
def parser(expression,reverse=True):
    res_stack=[]
    
    expr_queue=expression.split()
    print(expression)
    if reverse==False:
        expr_queue=reversed(expr_queue)
    for expr in expr_queue:
        try:
            expr=float(expr)
            res_stack.append(expr)
        except ValueError:
            res_stack.append(op_func(expr,res_stack.pop(),res_stack.pop()))
    return res_stack[-1]

def op_func(op,num1,num2):
    if op=="+":
        return num1+num2
    if op=="-":
        return num1-num2
    if op=="*":
        return num1*num2
    if op=="/":
        return num1/num2
    raise ValueError("Invalid operator!")

        
res=parser("* 4 + 2 3",reverse=False)
print(res)