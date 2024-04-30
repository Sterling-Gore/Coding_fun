inputs = input().split()
for i in range(4):
    inputs[i] = int(inputs[i])

left = []
right = []
left.append(inputs[0] * inputs[1])
left.append(inputs[0] + inputs[1])
left.append(inputs[0] - inputs[1])
left.append(int( inputs[0] / inputs[1]))
right.append(inputs[2] * inputs[3])
right.append(inputs[2] + inputs[3])
right.append(inputs[2] - inputs[3])
right.append(int( inputs[2] / inputs[3]))

answers = []

for i in range(4):
    for j in range(4):
        if left[i] == right[j]:
            temp = ''
            if i == 0:
                temp += f'{inputs[0]} * {inputs[1]}'
            if i == 1:
                temp += f'{inputs[0]} + {inputs[1]}'
            if i == 2:
                temp += f'{inputs[0]} - {inputs[1]}'
            if i == 3:
                temp += f'{inputs[0]} / {inputs[1]}'
            
            if j == 0:
                temp += f' = {inputs[2]} * {inputs[3]}'
            if j == 1:
                temp += f' = {inputs[2]} + {inputs[3]}'
            if j == 2:
                temp += f' = {inputs[2]} - {inputs[3]}'
            if j == 3:
                temp += f' = {inputs[2]} / {inputs[3]}'

            answers.append(temp)


if len(answers) == 0:
    print('problems ahead')
else:
    for i in answers:
        print(i)

        

