import math
data = input().split(' ')
num_houses = int(data[0])
capacity = int(data[1])
negatives = []
positives = []

for i in range(num_houses):
    data = input().split(' ')
    if int(data[0]) > 0:
        positives.append((int(data[0]), int(data[1])))
    else:
        negatives.append((int(data[0]), int(data[1])))

positives.sort()
negatives.sort(reverse = True)

total = 0
resid = False
for i, j in positives:
    if resid:
        
        
    if j % capacity != 0:
        resid = True
    else:
        resid = False
    

for i,j in negatives:

    

print(f'THIS IS THE TOTAL: {total}')



