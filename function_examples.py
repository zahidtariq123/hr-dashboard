'''
def add():
    print('Enter Number1')
    num1 = int(input())
    print('Enter Number2')
    num2 = int(input())
    result = num1 + num2
    print(result)

def sub():
    print('Enter Number1')
    num1 = int(input())
    print('Enter Number2')
    num2 = int(input())
    result = num1 - num2
    print(result)

def mult():
    print('Enter Number1')
    num1 = int(input())
    print('Enter Number2')
    num2 = int(input())
    result = num1 * num2
    print(result)

def div():
    print('Enter Number1')
    num1 = int(input())
    print('Enter Number2')
    num2 = int(input())
    result = num1 / num2
    print(result)

print('Enter Any Operator')
opp = input()

if opp == '+':
    add()
elif opp == '-':
    sub()
elif opp == '*':
    mult()
elif opp == '/':
    div()
else:
    print('please enter valid operator')
'''


'''
function with parameters
'''

'''
def add(x,y):
    result = x+y
    print(result)



print('Enter number 1')
num1 = int(input())
print('Enter number 2')
num2 = int(input())
add(num1,num2)
'''
'''
def nat():
    for i in range(1,11):
        print(i)


def even():
    for i in range(1,11):
        if i%2==0:
             print(i)


def odd():
    for i in range(1,11):
        if i%2 !=0:
            print(i)


print('enter number')
num = int(input())
if num == 1:
    nat()
elif num == 2:
    even()
elif num == 3:
    odd()
else:
    print('please enter valid number')
'''
'''
def add():
    print('enter number')
    num1 = int(input())
    print("enter nnumber")
    num2 = int(input())
    results = num1+num2
    print(results)

print('enter operator')
opp = input()
if opp == '+':
    add()
elif opp == '-':
    sub()
else:
    print('wrong operator')
'''
# def add(x,y):
#     result = x+y
#     print('inside function',result)
#     return result
#
#
#
# output = add(10,20)
# print('outside ',output)
#
# print(2+2)

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32
#
#
# temperature_in_celsius = 30
# temperature_in_fahrenheit = celsius_to_fahrenheit(temperature_in_celsius)
# print(f"{temperature_in_celsius}°C is {temperature_in_fahrenheit}°F")

'''
def calculate_total_price(price, tax_rate):
    total_price = price + (price * tax_rate / 100)
    return total_price

# Example usage
price = 100
tax_rate = 8  # 8% tax
total = calculate_total_price(price, tax_rate)
print(f"The total price after {tax_rate}% tax is: ${total}")
'''
'''
def shutup(call_him, name):
    return name
call_him = 'shutup'
name = 'atiq'
output = shutup(call_him,name)
print(call_him+output)
'''
'''
def mul(x,y,z):
    results = x*y*z
    return results
output = mul(10,2,3)
print(output)
'''
'''
def add_numbers(a,b):
    return  a + b
results = add_numbers(2,3)
print(results)
'''
'''
def sub_numbers(x,y):
    return x+y
results = sub_numbers(10,20)
print(results)
'''
# def greet(name):
#     print(f"hello, {name}")
# greet('zahid')