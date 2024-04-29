numbers = input().split(' ')
n = int(numbers[0])
s = int(numbers[1])
m = int(numbers[2])
board = input().split(' ')

count = 0
game = True
visited = {}
while game:
    if s < 1:
        print("left")
        game = False
    elif s > n:
        print("right")
        game = False
    elif s in visited:
        print("cycle")
        game = False
    elif int(board[s-1]) == m:
        print("magic")
        game = False
    else:
        count += 1
        visited[s] = True
        s += int(board[s-1])
print(count)



