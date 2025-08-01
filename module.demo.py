'''
import random as rd
symbols = 'qwerbjfnjivjojfejcn133986854'
otp=''
for i in range(5):
    otp=otp+symbols[rd.randrange(len(symbols))]
print(otp)
'''


# import math

# print(math.pi)
# print(math.sqrt(36))
# print(math.cbrt(27))
# print(math.ceil(12.1))
# print(math.floor(12.99))
# print(math.factorial(4))
# print(math.sin(90))
# print(math.cos(0))
# print(math.pow(2,4))

# import random as rd
#
# num = rd.random()*10
# print(math.ceil(num))
'''
while True:
    print('Enter Number1')
    num1 = int(input())
    print('Enter Number2')
    num2 = int(input())
    print('Enter operator + - * /')
    opp = input()

    if opp == '+':
        print(num1+num2)
    elif opp == '-':
        print(num1-num2)
    elif opp == '*':
        print(num1*num2)
    elif opp == '/':
        print(num1/num2)
    else:
        print('enter valid operator')

    print('do you want to continue press y else for exit any key')
    choice = input()
    if choice == 'y':
        continue
    else:
        print('thank you')
        break
'''
'''
while True:
    p1=0
    p2=0
    for i in range(1,21):
        i=1
        if p1==20:
         print('player1 won')
        elif p2==20:
            print('player2won')
        else:
            print(")
'''
#jump statements
'''
for i in range(1,11):
    if i==5:
        break
    print(i)
'''
'''
for i in range(1,11):
    if i==5:
        continue
    print(i)
'''
'''
def add():
    print('enter number')
    num1 = int(input())
    print('enter number')
    num2 = int(input())
    results = num1+num2
    print(results)
add()
'''
'''
def sub():
    print('enter number')
    num1 = int(input())
    print('enter number')
    num2 = int(input())
    results = num1-num2
    print(results)
sub()
'''
'''
def div():
    print('enter number')
    num1 = int(input())
    print('enter number')
    num2 = int(input())
    results = num1%num2
    print(results)
div()
'''
'''
def mul():
    print('enter number')
    num1 = int(input())
    print('enter number')
    num2 = int(input())
    results = num1*num2
    print(results)
mul()
'''
