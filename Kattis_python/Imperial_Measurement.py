inputs = input().split(' ')
league = 190080000
mile = 63360000
furlong = 7920000
chain = 792000
yard = 36000
foot = 12000
inch = 1000
thou = 1

num = int(inputs[0])
top = inputs[1]
bot = inputs[3]

if top == 'thou' or top == 'th':
    top = thou
elif top == 'inch' or top == 'in':
    top = inch
elif top == 'foot' or top == 'ft':
    top = foot
elif top == 'yard' or top == 'yd':
    top = yard
elif top == 'chain' or top == 'ch':
    top = chain
elif top == 'furlong' or top == 'fur':
    top = furlong
elif top == 'mile' or top == 'mi':
    top = mile
elif top == 'league' or top == 'lea':
    top = league

if bot == 'thou' or bot =='th':
    bot = thou
elif bot == 'inch' or bot =='in':
    bot = inch
elif bot == 'foot' or bot =='ft':
    bot = foot
elif bot == 'yard' or bot =='yd':
    bot = yard
elif bot == 'chain' or bot =='ch':
    bot = chain
elif bot == 'furlong' or bot =='fur':
    bot = furlong
elif bot == 'mile' or bot =='mi':
    bot = mile
elif bot == 'league' or bot =='lea':
    bot = league


ans = num * (top / bot)
temp = str(ans)
if temp[temp.index('.')+1] == '0' and len(temp[temp.index('.'):])  < 3:
    ans = int(ans)
print(ans)