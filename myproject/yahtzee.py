from random import randint
print('Welcome to Wacky Yahtzee, the greatest dice game ever!!! Here are the rules: ')
rules = (''' 1. Each player gets to throw 5 dice up to three times
 2. player doesn't have to roll all 5 dice on the second and third round
 3. you can put as many dice to the side and can only throw the ones that you don't want''')
print(rules)
print('       ')
print(''' The objective of this game is to get as many points as possible
by rolling five dice and getting certain combonations. So have fun!!!''')
print('     ')
player1storage = {'ones':0, 'twos': 0, 'threes':0, 'fours':0,'fives':0, 'sixes':0,'YAHTZEE':0,'total':0}
player2storage = {'ones':0, 'twos': 0, 'threes':0, 'fours':0,'fives':0, 'sixes':0,'YAHTZEE':0,'total':0}
def play(rollnumber, diceleft, scard1, playernumber, allchoices= [], isplaying = True):
 if isplaying:
  options = []
  if (rollnumber == 1):
   fullplay = []
  else:
     fullplay = allchoices
  for x in range(diceleft):
   options.append(randint(1,6))
  print('It is player %s turn'%playernumber )
  print('Your options are:%s ' %options)
  doyouwannaplay = 'yes'
  if rollnumber == 2 or rollnumber == 3:
   doyouwannaplay = raw_input('do you wanna keep going? yes or no: ')
  if doyouwannaplay == 'yes':
   choiceofdice = raw_input('Which dice do you want to take out: ')
   
   playerkept = choiceofdice.split(',')
  
   for num in playerkept:
    fullplay.append(num)
   addtoscorecard(playerkept, scard1)
 
   if rollnumber < 3 and diceleft > 0:
     play(rollnumber + 1,diceleft - len(playerkept), scard1, playernumber, fullplay,isplaying)
   else:
    isyahtzee = yahtzee1(fullplay)
    scorecard(scard1,isyahtzee)
  else:
    print('ok')
    scorecard(scard1,False)

  
def yahtzee1(checklist):
 if len(checklist) < 5:
  return False
 if checklist[0] == checklist[4] and checklist[0]==checklist[1] and checklist[0] == checklist[2] and checklist[0] == checklist[3]:
  return True
 else:
  return False
 

  
def addtoscorecard(listofkept,scard):
  intkept = []
  for x in listofkept:
    intkept.append(int(x))
 
  for y in intkept:
    if y == 1:
      scard["ones"] = scard["ones"] + 1
    if y == 2:
      scard['twos'] = scard['twos'] + 2
    if y == 3:
      scard['threes'] = scard['threes'] + 3
    if y == 4:
      scard['fours'] = scard['fours'] + 4
    if y == 5:
      scard['fives'] = scard['fives'] + 5
    if y == 6:
      scard['sixes'] = scard['sixes'] + 6
  scard['total'] = scard["ones"] + scard['twos'] + scard['threes'] + scard['fours'] + scard['fives'] + scard['sixes']
 
def scorecard(storage,isityahtzee):
 if isityahtzee:
  storage['YAHTZEE'] = storage['YAHTZEE'] + 50
 total = 0
 for val in sorted(storage):
   print(val,storage[val])
   total = total + storage[val]
 print('this is your total: %d' %total)
 
 
def fullcategories(p1sc,p2sc):
 p1vals = p1sc.values()
 p2vals = p2sc.values()
 for value in p1vals:
  if value == 0:
   return False
 for values in p2vals:
  if values == 0:
   return False
  return True
  
 
full = fullcategories(player1storage,player2storage) 
while not full:
 
 play(1,5,player1storage,1)
 play(1,5,player2storage,2)
 full = fullcategories(player1storage,player2storage)
if player1storage['total'] > player2storage['total']:
 print('Player 1 wins!!!')
elif player2storage['total'] > player1storage['total']:
 print('Player 2 wins!!!')
elif player1storage['total']== player2storage['total']:
  print('It is a draw!!')