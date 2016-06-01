# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance - amount > 0:
#             self.balance -= amount
#             print("Thanks {n}! You withdrew ${am}".format(n=self.name, am=amount))
#         else:
#             print('You don\'t have enough money to withdraw ${am} fool!'.format(am=amount))
#
# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, minimum_balance):
#         BankAccount.__init__(self, name, balance)
#         self.minimum_balance = minimum_balance
#
#     def withdraw(self, amount):
#         if self.balance - amount < self.minimum_balance:
#             print('Sorry, minimum balance must be maintained.')
#         else:
#             BankAccount.withdraw(self, amount)


'''
Create a simple dice game whith two players. Each player will take turns rolling
dice. Add the dice total to each players score. The first one to 20 wins. If a
player rolls a double 3 or 6 the score is reset. Use classes for the users.
'''
import random

class Person:
    def __init__(self, name):
        self.name = name
        self.health = 100

player1 = Person('Chris')
player2 = Person('Katie')


def fight(p1, p2):
    p1.health -= random.randint(1, 10)
    p2.health -= random.randint(1, 10)

fight(player1, player2)

print(player1.name, player1.health)
print(player2.name, player2.health)
