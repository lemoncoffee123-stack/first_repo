post_exp = '6528-*2/+'

def caculator(exp):
    stack = []
    for chr in exp:
        if chr in '+*/-':
            num2 = stack.pop()
            num1 = stack.pop()
            if chr == '+':
                stack.append(num1 + num2)
            elif chr == '-':
                stack.append(num1 - num2)
            elif chr == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num1//num2)
        else:
            stack.append(int(chr))

    return stack[-1]

print(caculator(post_exp))