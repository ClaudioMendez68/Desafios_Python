import requests, json

url ='https://reqres.in/api/users'

payload = json.dumps({'email': 'ignacio.morris@reqres.in',
                    'first_name': 'Ignacio',
                    'last_name': 'Morris',
                    'job': 'Profesor', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'})
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", 'https://reqres.in/api/users', headers=headers, data=payload)
created_user = response.text
print(created_user)