from random import randint
print('welcome to Yahtzee, the greatest dice game ever!!! Here are the rules: ')
rules = (''' 1. EAch player gets to throw 5 dice up to three times
 2. player doesn't have to roll all 5 dice on the second and third round
 3. you can put as many dice to the side and can only throw the ones that you don't want''')
print(rules)
pl1r1 = randint(1,6)
pl2r1 = randint(1,6)
pl1r2 = randint(1,6)
pl2r2 = randint(1,6)
pl1r3 = randint(1,6)
pl2r3 = randint(1,6)
pl1r4 = randint(1,6)
pl2r4 = randint(1,6)
pl1r5 = randint(1,6)
pl2r5 = randint(1,6)
print('Player 1 rolled ',pl1r1,pl1r2,pl1r3,pl1r4,pl1r5)
print('Player 2 rolled ',pl2r1,pl2r2,pl2r3,pl2r4,pl2r5)
choiceofdice1 = raw_input('Which dice do you want to keep player 1? ')
#category1 = raw_input('What category do you want to put your dice in player 1? ')
choiceofdice2 = raw_input('Which dice do you want to keep player 2? ')
#category2 = raw_input('Which category do you want to put you dice in player 2? ')
player1options = []
player2options = []
player1kept = choiceofdice1.split(',')
player2kept = choiceofdice2.split(',')
print(player1kept)
print(player2kept)

