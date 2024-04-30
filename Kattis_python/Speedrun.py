inputs = input().split(' ')
tasks = int(inputs[0])
choices = int(inputs[1])
days = []
for i in range(choices):
    inputs = input().split(' ')
    start = int(inputs[0])
    end = int(inputs[1])
    days.append([start, end])

for i in days:
    i = i



print(days)