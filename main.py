import requests

url ='https://jsonplaceholder.typicode.com/posts'

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, data=data)

print(f'\nСтатус-код ответа: {response.status_code} \n')

print(f"Ответ - {response.json()}")