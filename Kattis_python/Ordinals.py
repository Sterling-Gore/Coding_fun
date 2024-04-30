
cache = {}
cache[0] = '{}'
num = int(input())



for i in range(1, num+1):
    temp = "{"
    for j in range(len(cache)):
        temp += cache[j]
        temp += ','
    temp = temp[:-1]
    temp += '}'
    cache[i] = temp

print(cache[num])
    



        