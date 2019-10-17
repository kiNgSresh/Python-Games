import time,os
import pyfiglet, random
print (pyfiglet.figlet_format('Guess the number!'))
fname = 'rules_gg.txt'
fh = open(fname, 'rt')
for line in fh:
    print(line)

print('*******************************--------------------------*****************************---------------------')
n = random.randrange(0,10)
def wait():
    print('Computer is choosing the number, please wait......')
    time.sleep(1)
    print('Computer has chosen a number...')

def guess():
    print('What\'s your guess\n')
    try:
        g = int(input())
        if g in range(1,10):
            if g == n :
                print('Your guess is correct!')
                print(
                    '*******************************--------------------------*****************************---------------------')
                print(pyfiglet.figlet_format('YOU WON',font='slant'))
            elif g is not n:
                g = int(input('Nope,let\'s try once more\n'))
                if g == n:
                    print('Your guess is correct')
                    print(
                        '*******************************--------------------------*****************************---------------------')
                    print(pyfiglet.figlet_format('YOU WON', font='slant'))
                elif g is not n:
                    g = int(input('What\'s your last guess?\n'))
                    if g == n:
                        print('Your guess is correct!')
                        print(
                            '*******************************--------------------------*****************************---------------------')
                        print(pyfiglet.figlet_format('YOU WON', font='slant'))
                    else:
                        print(
                            '*******************************--------------------------*****************************---------------------')
                        print(pyfiglet.figlet_format('YOU LOST', font='slant'))
        else:
            print('Invalid Value')
    except:
        print('INVALID VALUE ! You have to enter numbers between 0 and 10')
        print('Read the rules again:')
        fname = 'rules_gg.txt'
        fh = open(fname, 'rt')
        for line in fh:
            print(line)














wait()

guess()
while True:
    play_again = input('Do you want to play again? Yes[y] or No[n]')
    if play_again == 'y' :
        n = random.randrange(0,10)
        guess()
        continue
    else :
        os.system('exit()')
        break

