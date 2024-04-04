import requests, json

url = "https://reqres.in/api/users/5"

payload = json.dumps({
  "id": 5,
  "email": "morpheus@reqres.in",
  "first_name": "Morpheus",
  "residence": "Zion",
  "avatar": "https://reqres.in/img/faces/5-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)
updated_user = response.text

print(updated_user)
