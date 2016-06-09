# import requests
#
# # You will learn how to speak like me someday.
# headers = {"X-Mashape-Key": "fuvOMXwTedmshhs0Yt5141FbNywIp1zi6NfjsnIjUgFSOLoEam",
#            "Accept": "text/plain"}
#
# sentence = input('Enter text to be translated to Yoda speak: ')
#
# # print(sentence)
# # print()
# # print(sentence.replace(' ', '+'))
# r = requests.get('https://yoda.p.mashape.com/yoda?sentence=' + sentence.replace(' ', '+'), headers=headers)
#
# print(r.text)


'''
Write a function that prints out numbers to 100
but if that number is divisible by 3 instead of the number we print "Fizz"
if that number is divisible by 5 we print "Buzz"
and if that number is divisible by 5 and 3 we print "FizzBuzz"
'''

# 2 % 3 == 0  | False
# 3 % 3 == 0  | True



def fizzbuzz(n):
    nums = list(range(1, n+1))
    for num in nums:
        if num % 5 == 0 and num % 3 == 0:
            print('FizzBuzz')
        elif num % 5 == 0:
            print('Fizz')
        elif num % 3 == 0:
            print('Buzz')
        else:
            print(num)

fizzbuzz(100)
# def fizzbuzz(n):
#     nums = list(range(1, n+1))
#     for num in nums:
#         if num % 3 == 0:
#             print('FizzBuzz')
#         elif num % 5 == 0:
#             print('Fizz')
#         elif num % 5 == 0 and num % 3 == 0:
#             print('Buzz')
#         else:
#             print(num)
