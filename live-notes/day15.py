import requests

# You will learn how to speak like me someday.
headers = {"X-Mashape-Key": "fuvOMXwTedmshhs0Yt5141FbNywIp1zi6NfjsnIjUgFSOLoEam",
           "Accept": "text/plain"}

sentence = input('Enter text to be translated to Yoda speak: ')

# print(sentence)
# print()
# print(sentence.replace(' ', '+'))
r = requests.get('https://yoda.p.mashape.com/yoda?sentence=' + sentence.replace(' ', '+'), headers=headers)

print(r.text)
