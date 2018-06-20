choice = raw_input('rock(r), paper(p),scissors(s), lizard(l), or spock(sp)? ')
from random import randint
com_choice = randint(1,5)
if com_choice == 1:
    computer = 'r'
elif com_choice == 2:
   computer = 'p'
elif com_choice == 3:
    computer = 's'
elif com_choice == 4:
    computer = 'l'
elif com_choice == 5:
    computer = 'sp'
#DRAW
if choice == computer:
    print('We have a draw')
#ROCK
elif choice == 'r' and computer == 's':
    print('''Rock crushes scissors
  you win  ''')
  
elif choice == 'r' and computer == 'p':
    print('''paper covers rock
    you lose''')
    
elif choice == 'r' and computer == 'l':
    print('''rock crushes lizard
    you win''')
    
elif choice == 'r' and computer == 'sp':
    print('''Spock vaporizes rock
    you lose''')
#SCISSORS
elif choice == 's'and computer == 'r':
    print('''Rock crushes scissors
    you lose''')
    
elif choice == 's' and computer == 'p':
    print('''Scissors cuts paper
    you win''')
    
elif choice == 's' and computer == 'l':
    print('''Scissors decapitates lizard
    you win''')
elif choice == 's' and computer == 'sp':
    print('''Spock smashes scissors
    you lose''')
#PAPER
elif choice == 'p' and computer == 's':
    print('''Scissors cuts paper
    you lose''')
    
elif choice == 'p' and computer == 'r':
    print('''Paper covers rock
    you win''')
    
elif choice == 'p' and computer == 'l':
    print('''Lizard eats paper
    you lose''')

elif choice == 'p' and computer == 'sp':
    print('''paper disproves spock
    you win''')
#LIZARD
elif choice == 'l' and computer == 'r':
    print('''Rock crushes lizard
    you lose''')

elif choice == 'l' and computer == 'p':
    print('''Lizard eats paper
    you win''')

elif choice == 'l' and computer == 's':
    print('''Scissors decapitates lizard
    you lose''')
    
elif choice == 'l' and computer == 'sp':
    print('''Lizard poisons spock
    you win''')
#SPOCK
elif choice == 'sp' and computer == 'r':
    print('''Spock vaporizes rock
    you win''')
    
elif choice == 'sp' and computer == 'p':
    print('''Spock disproves paper
    you lose''')
    
elif choice == 'sp' and computer == 's':
    print('''Spock crushes scissors
    you win''')

elif choice == 'sp'and computer == 'l':
    print('''Lizard poisons spock
    you lose''')






    
    
    
  