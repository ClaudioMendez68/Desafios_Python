import requests, json

def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get('https://reqres.in/api/users')

users_data = response['data']

# print(users_data)

for user in users_data:
    print(user)