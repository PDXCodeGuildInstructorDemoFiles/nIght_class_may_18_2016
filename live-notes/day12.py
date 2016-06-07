# lst = [1, 2, 3, 4]
#
# lst2 = lst[::-1]
#
# print(lst2)
#
#
# lst = ['A', 'B', 'C', 'D', 'E']
#
#
# number = 0
# while number < len(lst):
#     print(lst[number])
#     number += 1
#
# for i in lst:
#     print(i)
#
#
# def add(x, y):
#     num1 = int(input("first number? "))
#     num2 = int(input("second number? "))
#     return x + y
#
# def sub(x, y):
#     return x - y
#
#
# def calc():
#     query = input("Would you like to use (ad)dition (sub)traction? ")
#     if query =='ad':
#
#         answer = add()
#     elif query == 'sub':
#         num1 = int(input("first number? "))
#         num2 = int(input("second number? "))
#         answer = sub()
#     else:
#         print("I don't understand that...")
#     print("Your answer is {}".format(answer))
#
# calc()

# def greeting():
#     return "Hello"
'''

# possible classes
room
- doors / exit
- desctiption
player
- health
- backpack
* move thrugh exit
subclass player for monsters
dungeon
- rooms
items
- type
- value
- durability

'''

class Room:
    def __init__(self, name, description, doors):
        self.name = name
        self.description = description
        self.doors = doors
        self.visited = False


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

tr1 = Room('Test Room One', "This room is very small. You barely fit here. \
You're like Alice in that crazy-tiny-room thing.", {})

tr2 = Room('Test Room Two', "This room is very small. You barely fit here. \
You're like Alice in that crazy-tiny-room thing.", {})

tr1.doors = {'east': tr1, 'west': tr1}
tr2.doors['west'] = tr1

print(tr1)
# print(tr1.name)
# print(tr1.description)
# print(tr1.doors)
