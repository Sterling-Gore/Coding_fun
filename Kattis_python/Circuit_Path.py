num_inputs = int(input())
inputs = list(map( lambda z: True if z=='T' else False, input().split()))
expression = input().split()

stack = []


operations = {
    '*': lambda: stack[-1] and stack[-2],
    '+': lambda: stack[-1] or stack[-2],
    '-': lambda: not stack[-1]
}

for i in expression:
    if i in operations:
        k = operations[i]()
        if i == '-':
            stack = stack[:-1]
        else:
            stack = stack[:-2]
        stack.append(k)
    else:
        stack.append(inputs[ord(i) - 65])

print('T' if stack[0] else 'F')


    
