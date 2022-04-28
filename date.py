import datetime

today = datetime.date.today()
# print(today.day)
if str(today.day) == '28':
    print('success')
else:
    print('error')