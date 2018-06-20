option1 = ('In the future you will gain much wealth')
option2 = ('I see a big fluffy ball of happiness coming your way')
option3 = ('Sorry to tell you this, but it is going to rain on your birthday')
option4 = ('You could you possibly have bad traffic')
option5 = ('I sense lots of food in your future')
option6 = ('honestly your future is blank')

ans = raw_input('would you like to know your future? y or n: ')
if ans == 'y':
    print('''Hello, my name is zulo.
Welcome to my game where I get to tell your fortune.
Hope you enjoy!!!''')
    number = int(raw_input('pick a number between 1 - 6: '))
    if number == 1:
        print(option1)
    elif number == 2:
        print(option2)
    elif number == 3:
        print(option3)
    elif number == 4:
        print(option4)
    elif number == 5:
        print(option5)
    elif number == 6:
        print(option6)
    else:
        print('that was not an option')
elif ans == 'n':
   print(':( well thanks for your time') 



      
