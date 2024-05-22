#im assuming that this has to deal with duplicates
word = input()
cache = {}
ans = 1
for i in word:
    if i not in cache:
        cache[i]= 0
    else:
       ans = 0
print(ans)