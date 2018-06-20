myfavicecream = raw_input('what is your favorite icecream? ')
if myfavicecream == 'chocolate':
    print('thst is also my favorite icecream!!!')
elif myfavicecream in ['vanilla', 'carmel', 'fudge brownie', 'rocky road']:
    print('I like that flavor to :)')
else:
    print('you have terrible taste')
myname = raw_input('what is your name? ')
myinfo = ['Angel', 'Bob', 'Marcus','Serenity']
myinfo.append(myname)
for name in myinfo:
    if name == 'Bob':
        print('Sup Bob')
        break
    if name != 'Bob':
        print('Ew you are not bob')  
        break
x = int(raw_input('please give me a whole number: '))
if x > 0:
    print(x)
else:
    print(-x)