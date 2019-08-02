import requests
url = 'http://0.0.0.0:5000/api'
file = open("conversation.txt","r")
text = file.read()
# Removing \n at the end
text = text.split('\n')[0]
r = requests.post(url,json={'text':text})
print(r.json())

