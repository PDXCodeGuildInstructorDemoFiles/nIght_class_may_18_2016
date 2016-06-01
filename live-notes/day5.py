# phonebook = {
#     'chris': {'name': 'Chris', 'phone': "503-277-9710"},
#     'sam': {'name': 'Sam', 'phone': "503-277-9710"}
# }
#
# def search():
#     pass
#
# def add_entry():
#     pass
#
# def chage_entry():
#     pass
#
# def delete_entry():

import datetime
s = '2013-07-01'
mydate = datetime.datetime.strptime(s, '%Y-%m-%d')
print(mydate.strftime('%B %d, %Y'))
