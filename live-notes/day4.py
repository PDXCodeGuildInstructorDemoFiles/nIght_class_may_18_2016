'''
Create a program that uses a dictionary to store phonebook
entries. Must have user interaction.
Include ability to:
1. Search
2. Add Entry
3. Chage Entry
4. Delete Entry
5. Exit Program
'''

phonebook = {
    'chris': {'name': 'Chris', 'phone': "503-277-9710"},
    'sam': {'name': 'Sam', 'phone': "503-277-9710"}
}

# How to look someone up in a dictionary
# try:
#     search = input('Who are you looking for? ')
#     print(phonebook[search.lower()])
#     print(phonebook[search.lower()]['name'])
#     print(phonebook[search.lower()]['phone'])
# except KeyError:
#     print('There is no entry of {}'.format(search))

# Add to a dictionary
# name = input('What is the name? ')
# phone = input('What is the phone? ')
# phonebook[name.lower()] = {'name': name.capitalize(), 'phone': phone}
# print(phonebook)

# Delete something from a dictionary
# phonebook['chris']['phone'] = '555 1234 567'
# print(phonebook)

def search():
    name = input('who change')
    print(name)
    nc = False
    name_change = input('name change?')
    if name_change.lower() == 'yes':
        new_name = input('new name?')
        nc = True
    phone_change = input('phone change?')
    if phone_change == 'yes' and nc == True:
        new_phone = input('new phone?')
        del phonebook[name.lower()]
        phonebook[new_name.lower()] = {'name': new_name, 'phone': }
    elif phone_change == 'yes':
        new_phone = input('new phone?')
        phonebook[name.lower()]['phone'] = new_phone
    elif nc:
        new_phone = phonebook[name.lower()]['phone']
        del phonebook[name.lower()]
        phonebook[new_name.lower()] = {'name': new_name, 'phone': new_phone}

# User input loop fuction
def phone_book():
    print("Welcome to the Phone Book!")
    while True:
        print("-" * 40)
        print("Press 1 to search.")
        print("Press 2 to add.")
        print("Press 3 to change an entry.")
        print("Press 4 to remove.")
        print("Press 5 to exit.")
        print("-" * 40)
        try:
            choice = int(input('> '))
            if choice == 1:
                search()
            elif choice == 2:
                add()
            elif choice == 3:
                change()
            elif choice == 4:
                remove()
            elif choice == 5:
                exit()
        except ValueError:
            print("That is not a valid entry. Please try again.")

phone_book()    
