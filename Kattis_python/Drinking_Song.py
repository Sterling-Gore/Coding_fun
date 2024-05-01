#3 bottles of milk on the wall, 3 bottles of milk.
#Take one down, pass it around, 2 bottles of milk on the wall.

#2 bottles of milk on the wall, 2 bottles of milk.
#Take one down, pass it around, 1 bottle of milk on the wall.

#1 bottle of milk on the wall, 1 bottle of milk.
#Take it down, pass it around, no more bottles of milk.


num_bottles = int(input())
drink = input()

for i in range(num_bottles, 1, -1):
    print(f'{i} bottles of {drink} on the wall, {i} bottles of {drink}.')
    if i == 2:
        print(f'Take one down, pass it around, {i-1} bottle of {drink} on the wall.')
    else:
        print(f'Take one down, pass it around, {i-1} bottles of {drink} on the wall.')
    print()

print(f'1 bottle of {drink} on the wall, 1 bottle of {drink}.')
print(f'Take it down, pass it around, no more bottles of {drink}.')
