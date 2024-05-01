import requests
url = 'https://api.openai.com/v1/chat/completions'
headers = {'Content-Type': 'application/json','Authorization':'Bearer sk-proj-fkHkeOkzFW3ABGs3DmjRT3BlbkFJSBvtmMqMlafW0jFNxQbm'}
data = {"model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "What is 15 + 15?"}],
     "temperature": 0.7}
response = requests.post(url, headers=headers, json=data)
print(response.text)