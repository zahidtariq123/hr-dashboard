# def add(x,y):
#     print(x,y)
#
# add(2,3)


# def add(x,*n):
#     sum=0
#     for i in n:
#         sum = sum+i
#
#     print(sum)
#
# add(2)
# add('tom',2,6)
# add('john',2,6,6,8,1)
'''
def details(**x):
    print(x)


details(name='zahid',address='srinagar',age=21)
details(name='zahid',address='srinagar',age=21,city='srinagar')
'''
'''
mystring = "hello baby"
length_of_string = len(mystring)
print(length_of_string)
'''
'''
def greet(name, **kwargs):
    print(f"Hello, {name}!")
    if 'age' in kwargs:
        print(f"You are {kwargs['age']} years old.")
    if 'city' in kwargs:
        print(f"You live in {kwargs['city']}.")

greet("Bob", age=25, city="Los Angeles")
'''
'''
def emmhmm(name, **x):
    print(f'hello, {name}')
    if 'age' in x:
        print(f'you are {x['age']} years old')
    if 'city' in x:
        print(f'you live in {x['city']}')
emmhmm(name = "koopi", age = 21, city="norway")
'''
'''
def configure_settings(**kwargs):
    settings = {
        'theme': 'light',
        'font_size': 12,
        'notifications': True
    }
    settings.update(kwargs)  # Update default settings with provided kwargs
    return settings

user_settings = configure_settings(theme='dark', font_size=14)
print(user_settings)
'''
# def example_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
#
# example_function(1,2,3, name='pogal',age=30)