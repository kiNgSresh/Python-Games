import os
def clear() :
    os.system('cls')
print ('Welcome to hand cricket\n')
handle = open('handcricket rules.txt')
rules = input('Do you want to read the rules?')
for line in handle:
    if rules == 'YES':
        print(line)
    else :
        print ('Enjoy the game\n')
        break
Player1 = input('Enter your name:\n')
Player2 = input('Enter your name:\n')

def batting():
    sum1=0
    num1 = 2
    num2 = 3
    if num1 and num2 <= 6:
        while num1 != num2 :
            num1 = int(input('Enter the shot number Batsman\n'))
            clear()
            num2 = int(input('Bowl the ball !\n'))
            sum1 = sum1 + num1
        print ('OUT !, Your score is', sum1-num1)
    else:
        print ('Number greater than six is not allowed\n')

def tossing():
    toss = input('ODD OR EVEN? '+ Player1 +'\n')
    t1 = int(input('Enter the number\n'))
    clear()
    t2 = int(input('Enter the number\n'))
    if toss == 'ODD':
        if t1+t2%2 is 0:
            what=input(Player2 + ' bat or ball ?\n')
            batting()
            #player 2 will win the toss.
        else:
            what=input(Player1 +' bat or ball?\n')
            batting()
            #player 1 wins the toss.
    else:
        if t1+t2%2 is 0:
            what=input(Player1 +' bat or ball?\n')
            batting()
        else:
            what=input(Player2 +' bat or ball?\n')
            batting()
tossing()

print ('Now 2nd Innings will begin')
batting()

score1= input('Enter your runs'+ Player1)
score2 = input('Enter your runs' +Player2)
if score1 > score2 :
    print (Player1, 'wins!\n')
elif score1 < score2:
    print (Player2, 'wins!\n')
else :
    print ('Match drawn!\n')
