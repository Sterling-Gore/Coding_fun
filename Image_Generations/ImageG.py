#Image Generation

import numpy as np

from PIL import Image

import matplotlib as mplt

from matplotlib import pyplot as plt

import random

import math

#displays 6 pixels
#Blue Green Red
#White Grey Black
#(R, G, B)
# x-->255 == white
# x--> 0  == black
'''
M = [
    [(0,0,255), (0,255,0), (255,0,0)],
    [(255,255,255), (128,128,128), (0,0,0)]
    
]


plt.imshow(np.array(M), interpolation='none')
plt.show()
print(np.array(M))
'''



img = Image.open('origimg.png')
img.thumbnail((128,128))
img = np.asarray(img)
img_row = len(img)
img_col = len(img[0])



noise = np.random.randint(0, 256, (img_row,img_col,3), dtype='int64')


n = int(input("Give a number of generations: \n") )

fig = plt.figure(figsize = (10,7))
rows = 2
columns = math.ceil((n / 2) + 1)



def child_creater(parent):
    parent
    for i in range(img_row):
        for j in range(img_col):
            for k in range(3):
                val = parent[i][j][k]
                disparity = abs(img[i][j][k] - val)
                children = [random.randint(val-50, val+50),random.randint(val-50, val+50),random.randint(val-50, val+50),random.randint(val-50, val+50)]
                for c in children:
                    if c > 255:
                        c = 255
                    if c < 0:
                        c = 0
                    if disparity > abs(img[i][j][k] - c):
                        parent[i][j][k] = c
                        disparity = abs(img[i][j][k] - c)

    return parent

def generations(n, child):
    while(n > 0):
        child = child_creater(child)
        fig.add_subplot(rows, columns, n+3) 
        plt.imshow(child) 
        plt.axis('off') 
        plt.title(f"Generation {n+1}") 
        n -= 1
    return child


        


fig.add_subplot(rows, columns, 1)
plt.imshow(img)
plt.axis('off')
plt.title('Original')

fig.add_subplot(rows, columns, 2) 
plt.imshow(noise) 
plt.axis('off') 
plt.title("Noise")



for i in range(n):  
    noise = child_creater(noise)
    fig.add_subplot(rows, columns, i+3) 
    plt.imshow(noise) 
    plt.axis('off') 
    plt.title(f"Generation {i+1}") 




#imgplot = plt.imshow(arr)
plt.show()





