#FINISHED

sample = int(input())
bar_size = 1
while bar_size < sample:
    bar_size *= 2

#lets do the breaks in a stack

breaks = 0
stack = [bar_size]
while sample != 0:
    top = stack[-1]  #top
    stack = stack[:-1]  #pop
    if top > sample:
        top /= 2    #this splits into 2
        breaks += 1  
        stack.append(top)   
        stack.append(top)    
    else:
        sample -= top

print(f'{bar_size} {breaks}')
    

