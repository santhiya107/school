operators = set(['+', '-', '*', '/', '(', ')', '^']) 
priority = {'+':1, '-':1, '*':2, '/':2, '^':3} 
def infixToPostfix(exp):
    stack = [] 
    post = ''    
    for c in exp:
        if c not in operators: 
            post+= c
        elif c=='(':  
            stack.append('(')
        elif c==')':
            while stack and stack[-1]!= '(':
                post+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priority[c]<=priority[stack[-1]]:
                post+=stack.pop()
            stack.append(c)
    while stack:
        post+=stack.pop()        
    return post
exp = input('Enter infix expression ')
print('postfix notation: ',infixToPostfix(exp))
