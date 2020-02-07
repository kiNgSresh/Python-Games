import random
import pyfiglet
import sys
def quit():
    sys.exit()


print(pyfiglet.figlet_format('Welcome', font='slant'))

fname = 'rules.txt'
fh = open(fname, 'rt')
for line in fh:
    print(line)

print(pyfiglet.figlet_format('Let\'s play'))

p1 = input('rock, paper or scissor?\n')
c = random.choice(['rock', 'paper', 'scissor'])
print('*-*-*-*-*-*-*-*-')
print('Computer has chosen',c)


def rpc(p1,c):
        l1 = ['rock', 'paper', 'scissor']
        while True:
                if p1 == l1[0] and c == l1[1]:
                    print('computer wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == l1[0] and c == l1[2]:
                    print('player wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == l1[1] and c == l1[0]:
                    print('player wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == l1[1] and c == l1[2]:
                    print('computer wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == l1[2] and c == l1[0]:
                    print('computer wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == l1[2] and c == l1[1]:
                    print('player wins')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 == c:
                    print('drawn')
                    print('*-*-*-*-*-*-*-*-')
                    break
                elif p1 not in ('rock','paper','scissor'):
                    print('Invalid Value')
                    break
rpc(p1,c)
while True:
    play_again = input('Do you want to play again, yes or no?\n')
    if play_again == 'yes':
        p1 = input('rock, paper or scissor?\n')
        c = random.choice(['rock', 'paper', 'scissor'])
        print('Computer has chosen',c)
        print('*-*-*-*-*-*-*-*-')
        rpc(p1,c)
        continue
    elif play_again== 'no':
        print(pyfiglet.figlet_format('Thank you for playing'))
        quit()





