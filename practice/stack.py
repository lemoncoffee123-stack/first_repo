icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

T = 10

for tc in range(1, T + 1):
    len_exp = int(input())
    in_exp = input()

    post_exp = ''

    stack = []

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

    for chr in in_exp:
        if chr not in '+-*/()':
            post_exp += chr

        else:
            if not stack:
                stack.append(chr)
            else:
                if chr == ')':
                    while stack and stack[-1] != '(':
                        post_exp += stack.pop()
                    stack.pop()

                elif icp[chr] > isp[stack[-1]]:
                    stack.append(chr)
                else:
                    while stack and isp[stack[-1]] >= icp[chr]:
                        post_exp += stack.pop()

                    stack.append(chr)
    while stack:
        post_exp += stack.pop()

    print(f"#{tc} {caculator(post_exp)}")