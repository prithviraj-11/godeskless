import requests

word=input("Enter English word: ")
response=requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word+'')
data=response.json()
print(word+".",data[0]["meanings"][0]["partOfSpeech"]+".",data[0]["meanings"][0]["definitions"][0]["definition"])
