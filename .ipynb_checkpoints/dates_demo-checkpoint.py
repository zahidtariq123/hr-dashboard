import datetime as dt

current = dt.datetime.now()
# print(current)
# print(current.time())
# print(current.date())
# print(current.day)
# print(current.month)
# print(current.year)
#
# print(current.minute)
# print(current.hour)
# print(current.second)
# print(current)
#print(current.strftime('%d-%m-%Y %H:%M:%S'))

##print('current datetime',current_datetime)
current_datetime = dt.datetime.now()
formatted_datetime = current_datetime.strftime('%d-%m-%y %H:%M:%S')
print('formatted date time', formatted_datetime)