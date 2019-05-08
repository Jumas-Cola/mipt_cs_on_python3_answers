def stack_str_valid(string):
    stack = []
    for i in string:
        if i in '([{':
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return True

string = '{(())[()]}'
print(stack_str_valid(string))
