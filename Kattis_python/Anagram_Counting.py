#this question uses combinatorics, specifically the number of permutations
#   we will do (n!) / (a! * b! * c! * ...)
# n is the number of elements in a string, and a+b+c+... = n
#a represents the number of times a character appears
#therefore if every char in the string is unique, it would be (n! / 1 * 1 * 1 ...)
#which is just n!
import sys


cache = [0]*101
cache[0] = 1
cache[1] = 1
def factorial(n):
    if cache[n] == 0: #if item is not in the cache 
        cache[n] = n * factorial(n-1)
    return cache[n]



for inp in sys.stdin:
    characters = {}
    for i in inp:
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    numerator = factorial(len(inp) - 1)
    denominator = 1
    for i in characters.values():
        denominator *= factorial(i)
    print(numerator // denominator)
    

''''
inp = input()
while(inp):
    characters = {}
    #inp = input()
    #if inp == "":
    #    break

    for i in inp:
        if i not in characters:
            characters[i] = 1
        else:
            characters[i] += 1
    numerator = factorial(len(inp))
    denominator = 1
    for i in characters.values():
        denominator *= factorial(i)
    print(numerator // denominator)
    inp = input()
'''
