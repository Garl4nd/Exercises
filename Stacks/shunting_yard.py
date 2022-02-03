from PR_N import parser as prn_parser
import re
def shunting_yard(expr):
    op_stack=[]
    
    output_stack=[]
    operators=dict([("+",1),("*",4),("-",0),("/",3),("(",10),(")",10)])
    expr_list=[expr for expr in re.split("|".join("(\\"+key+")" for key in ["\s"]+list(operators.keys())),expr) if not expr  in [None," "]]
    print(expr_list)
    for expr in expr_list:
        if expr in operators:
        
            if expr==")":
                while op_stack[-1]!="(":
                    output_stack.append(op_stack.pop())    
                op_stack.pop()
            else:
                while op_stack and op_stack[-1]!="(" and operators[expr]<operators[op_stack[-1]]:
                    output_stack.append(op_stack.pop())
            
                op_stack.append(expr)
                
        else:
            output_stack.append(expr)
    
    while op_stack:
        output_stack.append(op_stack.pop())
    return " ".join(map(str,output_stack))


def op_func(op,num1,num2):
    if op=="+":
        return num1+num2
    if op=="-":
        return num2-num1
    if op=="*":
        return num1*num2
    if op=="/":
        return num2/num1
    raise ValueError("Invalid operator!")

prn=shunting_yard("1* (2 + 3 ) ")
print(f"{prn=}")
print(prn_parser(prn))
prn=shunting_yard("1 + 2 * 3 ")
print(prn_parser(prn))