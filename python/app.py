import requests

data = requests.get(url='https://cat-fact.herokuapp.com/facts/random').json()

print(data['text'])
