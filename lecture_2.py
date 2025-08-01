'''
print("enter your id")
id = input()
print('age')
age = int(input())
if (id=='y')  and (age>=18):
    print('welcome')
else:
    print('not allowed')
'''
'''
print('enter name')
name = input()
print('enter age')
age = int(input())
if name=="indian" and age>=18:
    print('welcome')
else:
    print('not allowed')
'''
'''
print('enter number')
number = int(input())
if (number>=20) and (number<=50):
    print('welcome')
else:
    print('not allowed')
'''
'''
print('enter day')
day = input()
if day=='sunday' or day=='saturday':
    print('its weekend')
else:
    print('go to work')
'''
# print('enter number')
# number = int(input())
# if (number==0):
#     print('number is 0')
# elif (number>0):
#     print('positive')
# else:
#     print("negative")
#num=[1,2,3,4,5]
#for i in num:
 #   if i%2!=0:
  #    print(i)
'''
num=[1,2,3,4,5]
for i in num:
    print(i*i)
'''
'''
print('enter number')
num = int(input())
for i in range(1,11):
    print(f'{num}x{i}={num*i}')
'''
'''
vov=['a','e','i','o','u']
names=['zahid','atiq','oopi','lala','cheeki']
for i in names:
    if i[0] in vov:
        print(i)
'''
'''
print('enter name')
name = input()
names = ['zahid','atiq','hanan']
if name in names:
        print('welcome')
else:
     print('not welcome')
'''


'''
for i in range(7,1,-1):
    for j in range(1,i-1):
        print(j,end=' ')
    print()
'''
'''
for i in range(1,5):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()
'''
'''
for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print()
'''
'''
i=1
while i<=6:
    j=0
    while j <=i:
        print(i,end=' ')
        j=j+1
    print()
    i=i+1
'''
'''
i=1
for i in range(30,50):
    if i%2!=0:
        print(i)
'''
'''
i=1
for i in range(1,11):
    print(i)
'''
'''
print('enter number')
num=int(input())
for i in range(1,11):
    print(f'{num}*{i}={num*i}')
'''
'''
import random as rd
symbols = '129dd93eedodwo-220kdw,dw2'
otp = ''
for i in range(5):
    otp = otp+symbols[rd.randrange(len(symbols))]
print(otp)
'''



